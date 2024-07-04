import heapq
from settings import Structures
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation


class AStarSolver:
    """
    A solver that uses the A* algorithm to find the shortest path in a maze.
    
    A* keeps track of two different factors. First, how expensive it was to get to a given node from the origin.
    Second, the minimum predicted cost of getting from that node to the goal. A* predicts the cost of traveling through
    a given node based on a heuristic function we provide it, which is based on the structure of our maze.
    
    In this case, we set the heuristic function to calculate the manhattan distance between the current node and the
    target node, so that our search will be encouraged to go as directly toward the goal as possible.
    """
    def __init__(self, maze):
        self.ims = None
        self.maze = maze
        self.visited = np.zeros_like(maze.grid, dtype=bool)
        self.path = []
        self.maze.grid[self.maze.grid == Structures.SELECTED] = Structures.EMPTY

    def solve(self, start, end, animate=False, animation_filename="", manhattan=False):
        """
        Solve the maze using the A* algorithm.
        :param manhattan: Should we use manhattan distance or Euclidean ? (manhattan if true Euclidean distance else)
        (the Euclidean distance is calculated without the square root to give more weight to the distances)
        :param start: Tuple[int, int], the starting point of the maze.
        :param end: Tuple[int, int], the ending point of the maze.
        :return: List[Tuple[int, int]], the path from start to end.
        """
        self.visited.fill(False)
        self.path = []
        self.ims = []
        if not animate:
            self._a_star(start, end, manhattan=manhattan)
            return self.path

        print("generating animation")
        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])

        self._a_star(start, end, animate=True, manhattan=manhattan)

        self.maze.grid[2 * end[0] + 1, 2 * end[1] + 1] = Structures.SELECTED
        im = plt.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL,
                        animated=True)
        self.ims.append([im])

        im = ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL)

        path = self.path[::-1]
        for i in range(1, len(path) + 1):
            # Plot the path
            cur_path = path[:i]
            path_y, path_x = zip(*cur_path)
            path_graph, = ax.plot(path_x, path_y, marker='o', color='red', markersize=5, linewidth=2)

            green_dot, = ax.plot(
                cur_path[-1][1], cur_path[-1][0],
                marker='o',
                color='green',
                markersize=5,
                animated=True
            )
            self.ims.append([im, path_graph, green_dot])

        print("saving animation")
        ani = ArtistAnimation(fig, self.ims, interval=100, blit=True)
        ani.save(animation_filename, writer='ffmpeg')
        plt.close()
        return self.path

    def _a_star(self, start, end, animate=False, manhattan=False):
        """
        The A* algorithm function.
        :param start: Tuple[int, int], the starting position in the maze.
        :param end: Tuple[int, int], the ending position in the maze.
        :param animate: bool, whether to animate the solving process.
        """
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))
        parent = {start: None}
        g_cost = {start: 0}
        start_x, start_y = start
        self.visited[start_x, start_y] = True
        self.maze.grid[2 * start_x + 1, 2 * start_y + 1] = Structures.SELECTED

        while priority_queue:
            current_cost, (x, y) = heapq.heappop(priority_queue)
            cell_x, cell_y = 2 * x + 1, 2 * y + 1

            if (x, y) == end:
                self._construct_path(parent, end)
                return True

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                new_g_cost = g_cost.get((x, y)) + 1  # Uniform cost for each step

                if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and  \
                        not self.visited[nx, ny] and self.maze.grid[2*nx+1-dx, 2*ny+1-dy] != Structures.WALL:
                    if (nx, ny) not in g_cost or new_g_cost < g_cost[(nx, ny)]:
                        g_cost[(nx, ny)] = new_g_cost
                        if manhattan:
                            h_cost = abs(nx - end[0]) + abs(ny - end[1])  # Manhattan distance
                        else:
                            h_cost = abs(nx - end[0]) ** 2 + abs(ny - end[1]) ** 2  # Euclidian distance without sqrt
                        f_cost = new_g_cost + h_cost
                        heapq.heappush(priority_queue, (f_cost, (nx, ny)))
                        parent[(nx, ny)] = (x, y)
                        self.visited[nx, ny] = True
                        self.maze.grid[2 * nx + 1, 2 * ny + 1] = Structures.SELECTED
                        self.maze.grid[cell_x + dx, cell_y + dy] = Structures.SELECTED

                        if animate:
                            im = plt.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL, animated=True)
                            self.ims.append([im])

        return False

    def _construct_path(self, parent, end):
        """
        Construct the path from start to end using the parent dictionary.
        :param parent: Dict[Tuple[int, int], Tuple[int, int]], the parent dictionary.
        :param end: Tuple[int, int], the ending position in the maze.
        """
        current = end
        while current is not None:
            self.path.append((2 * current[0] + 1, 2 * current[1] + 1))
            current = parent[current]
        self.path.reverse()