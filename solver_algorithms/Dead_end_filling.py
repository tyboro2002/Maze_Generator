import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

from Maze import Solver
from settings import Structures


class DeadEndFiller(Solver):
    def __init__(self, maze):
        super().__init__(maze)
        self.maze.grid[self.maze.grid == Structures.SELECTED] = Structures.EMPTY

    def fill_dead_ends(self, start, end, ax, animate=False):
        """
        Fill all dead-ends in the maze.
        """
        if animate:
            im = plt.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY,
                            vmax=Structures.WALL, animated=True)
            self.ims.append([im])
        startX, startY = start
        endX, endY = end
        dead_ends = True
        while dead_ends:
            dead_ends = 0
            # print(self.maze.grid)
            for x in range(1, self.maze.width * 2, 2):
                for y in range(1, self.maze.height * 2, 2):
                    if self.maze.grid[x, y] == Structures.EMPTY:
                        # print(x, y)
                        dead_end = self.maze.is_dead_end(x, y)
                        if (dead_end and (x, y) != (startX * 2 + 1, startY * 2 + 1)
                                and (x, y) != (endX * 2 + 1, endY * 2 + 1)):
                            dead_end_x, dead_end_y = dead_end
                            self.maze.grid[x, y] = Structures.WALL-1
                            self.maze.grid[x+dead_end_x, y+dead_end_y] = Structures.WALL-1
                            dead_ends += 1
                            if animate:
                                im = plt.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY,
                                                vmax=Structures.WALL, animated=True)
                                self.ims.append([im])

    def solve_setup(self, start=None, end=None, ax=None, animate=False):
        self.fill_dead_ends(start, end, ax, animate=animate)

    def solve_step(self, start, end, animate):
        self._dfs(start, end, animate=animate)
        # self.path = [start, end]

    def _dfs(self, start, end, animate=False):
        """
        The DFS function.
        :param start: Tuple[int, int], the starting position in the maze.
        :param end: Tuple[int, int], the ending position in the maze.
        """
        stack = [(start, [start])]
        start_x, start_y = start
        self.visited[start_x, start_y] = True
        self.maze.grid[2 * start_x + 1, 2 * start_y + 1] = Structures.SELECTED

        if animate:
            im = plt.imshow(
                self.maze.grid.copy(),
                cmap='binary',
                vmin=Structures.EMPTY,
                vmax=Structures.WALL,
                animated=True
            )
            self.ims.append([im])

        while stack:
            (x, y), path = stack.pop()
            cell_x, cell_y = 2 * x + 1, 2 * y + 1

            if (x, y) == end:
                self.path = [(2 * px + 1, 2 * py + 1) for px, py in path]
                return True

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < self.maze.width and 0 <= ny < self.maze.height and
                        not self.visited[nx, ny] and
                        self.maze.grid[2 * nx + 1 - dx, 2 * ny + 1 - dy] == Structures.EMPTY):
                    stack.append(((nx, ny), path + [(nx, ny)]))
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
