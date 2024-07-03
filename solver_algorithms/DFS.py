from settings import Structures
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation, FuncAnimation


class DFSSolver:
    def __init__(self, maze):
        self.maze = maze
        self.visited = np.zeros_like(maze.grid, dtype=bool)
        self.path = []
        self.maze.grid[self.maze.grid == 1] = 0

    def solve(self, start, end, animate=False, animation_filename=""):
        """
        Solve the maze using DFS.
        :param start: Tuple[int, int], the starting point of the maze.
        :param end: Tuple[int, int], the ending point of the maze.
        :return: List[Tuple[int, int]], the path from start to end.
        """
        self.visited.fill(False)
        self.path = []
        self.ims = []
        if not animate:
            self._dfs(start, end)
            return self.path
        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])

        self._dfs(start, end, animate=True)

        self.maze.grid[2 * end[0] + 1, 2 * end[1] + 1] = Structures.SELECTED
        im = plt.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL,
                        animated=True)
        # red_dot, = plt.plot(2 * end[1] + 1, 2 * end[0] + 1, marker='o', color='red', markersize=5, animated=True)
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

    def _dfs(self, current, end, animate=False):
        """
        The recursive DFS function.
        :param current: Tuple[int, int], the current position in the maze.
        :param end: Tuple[int, int], the ending point of the maze.
        :return: bool, True if the end is found, otherwise False.
        """
        x, y = current
        if current == end:
            self.path.append((2*x+1, 2*y+1))
            return True

        self.visited[x, y] = True
        self.maze.grid[2*x+1, 2*y+1] = Structures.SELECTED
        self.path.append((2*x+1, 2*y+1))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        if animate:
            im = plt.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL,
                            animated=True)
            # red_dot, = plt.plot(2 * y + 1, 2 * x + 1, marker='o', color='red', markersize=5, animated=True)
            self.ims.append([im])

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and not self.visited[nx, ny] and self.maze.grid[2*nx+1-dx, 2*ny+1-dy] != Structures.WALL:
                self.maze.grid[2 * x + 1+dx, 2 * y + 1+dy] = Structures.SELECTED
                if self._dfs((nx, ny), end, animate=animate):
                    return True

        self.path.pop()
        return False
