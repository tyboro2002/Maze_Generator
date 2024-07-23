import heapq

from Maze import Solver
from settings import Structures
import matplotlib.pyplot as plt


class DijkstraSolver(Solver):
    """
    A solver that uses Dijkstra's algorithm to find the shortest path in a maze.

    min-heap priority queue
    In spanning trees like ours, Dijkstra's proceeds like BFS, with changes to step 2:

    Remove the minimum entry from the priority queue.
    and step 4:

    Insert each of the current node's children into the priority queue.
    """
    def __init__(self, maze):
        super().__init__(maze)
        self.maze.grid[self.maze.grid == 1] = 0

    def solve_step(self, start, end, animate):
        self._dijkstra(start, end, animate=animate)

    def _dijkstra(self, start, end, animate=False):
        """
        The Dijkstra's algorithm function.
        :param start: Tuple[int, int], the starting position in the maze.
        :param end: Tuple[int, int], the ending position in the maze.
        :param animate: bool, whether to animate the solving process.
        """
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))
        parent = {start: None}
        cost = {start: 0}
        self.visited[start[0], start[1]] = True
        self.maze.grid[2 * start[0] + 1, 2 * start[1] + 1] = Structures.SELECTED

        while priority_queue:
            current_cost, (x, y) = heapq.heappop(priority_queue)
            cell_x, cell_y = 2 * x + 1, 2 * y + 1

            if (x, y) == end:
                self._construct_path(parent, end)
                return True

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                new_cost = current_cost + 1  # Uniform cost for each step

                if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and \
                        not self.visited[nx, ny] and self.maze.grid[2*nx+1-dx, 2*ny+1-dy] != Structures.WALL:
                    if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                        cost[(nx, ny)] = new_cost
                        priority = new_cost
                        heapq.heappush(priority_queue, (priority, (nx, ny)))
                        parent[(nx, ny)] = (x, y)
                        self.visited[nx, ny] = True
                        self.maze.grid[2 * nx + 1, 2 * ny + 1] = Structures.SELECTED
                        self.maze.grid[cell_x + dx, cell_y + dy] = Structures.SELECTED

                        if animate:
                            im = plt.imshow(
                                self.maze.grid.copy(),
                                cmap='binary',
                                vmin=Structures.EMPTY,
                                vmax=Structures.WALL,
                                animated=True
                            )
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
