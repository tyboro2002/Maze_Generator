from collections import deque
from settings import Structures
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation


class BFSSolver:
    """
    Start at the root.
    Shift the first (i.e. least recently added) element out of the queue.
    Check for a match. If found, return the target node.
    Add each of the current node's children to the stack.
    Repeat until a match is found, or the stack is empty.
    """
    def __init__(self, maze):
        self.maze = maze
        self.visited = np.zeros_like(maze.grid, dtype=bool)
        self.path = []
        self.maze.grid[self.maze.grid == 1] = 0

    def solve(self, start, end, animate=False, animation_filename=""):
        """
        Solve the maze using BFS.
        :param start: Tuple[int, int], the starting point of the maze.
        :param end: Tuple[int, int], the ending point of the maze.
        :return: List[Tuple[int, int]], the path from start to end.
        """
        self.visited.fill(False)
        self.path = []
        self.ims = []
        if not animate:
            self._bfs(start, end)
            return self.path

        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])

        self._bfs(start, end, animate=True)

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

        ani = ArtistAnimation(fig, self.ims, interval=100, blit=True)
        ani.save(animation_filename, writer='ffmpeg')
        return self.path

    def _bfs(self, start, end, animate=False):
        """
        The BFS function.
        :param start: Tuple[int, int], the starting position in the maze.
        :param end: Tuple[int, int], the ending position in the maze.
        :param animate: bool, whether to animate the solving process.
        """
        queue = deque([start])
        parent = {start: None}
        self.visited[start[0], start[1]] = True
        self.maze.grid[2 * start[0] + 1, 2 * start[1] + 1] = Structures.SELECTED

        while queue:
            x, y = queue.popleft()
            cell_x, cell_y = 2 * x + 1, 2 * y + 1

            if (x, y) == end:
                self._construct_path(parent, end)
                return True

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and not self.visited[nx, ny] and self.maze.grid[2*nx+1-dx, 2*ny+1-dy] != Structures.WALL:
                    queue.append((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    self.visited[nx, ny] = True
                    self.maze.grid[2 * nx + 1, 2 * ny + 1] = Structures.SELECTED

                    if animate:
                        self.maze.grid[2 * x + 1 + dx, 2 * y + 1 + dy] = Structures.SELECTED
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