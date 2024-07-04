import random

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

from settings import Structures


class RandomMouseSolver:
    """
    This simple method can be implemented by a very unintelligent robot or perhaps a mouse, because it does not
    require any memory. The robot proceeds following a random decision about the next direction to follow.
    """
    def __init__(self, maze):
        self.ims = None
        self.maze = maze
        self.visited = np.zeros_like(maze.grid, dtype=bool)
        self.path = []
        self.maze.grid[self.maze.grid == Structures.SELECTED] = Structures.EMPTY

    def solve(self, start, end, animate=False, animation_filename=""):
        """
        Solve the maze using Random Mouse Search.
        :param start: Tuple[int, int], the starting point of the maze.
        :param end: Tuple[int, int], the ending point of the maze.
        :return: List[Tuple[int, int]], the path from start to end.
        """
        self.visited.fill(False)
        self.path = []
        self.ims = []

        if not animate:
            self._random_mouse(start, end)
            self.maze.grid[2 * end[0] + 1, 2 * end[1] + 1] = Structures.SELECTED
            return self.path
        print("generating animation")
        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])

        self._random_mouse(start, end, animate=True)

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

    def _random_mouse(self, start, end, animate=False):
        """
        The random mouse search function.
        :param start: Tuple[int, int], the starting position in the maze.
        :param end: Tuple[int, int], the ending position in the maze.
        :param animate: bool, whether to animate the solving process.
        """
        current = start
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        while current != end:
            # print(current, end, len(self.path), self.path)
            x, y = current
            cell_x, cell_y = 2 * x + 1, 2 * y + 1
            self.visited[x, y] = True
            self.maze.grid[cell_x, cell_y] = Structures.SELECTED
            self.path.append((cell_x, cell_y))

            if animate:
                im = plt.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL,
                                animated=True)
                # Plot the current cell
                red_dot, = plt.plot(cell_y, cell_x, marker='o', color='red', markersize=5, animated=True)

                # Append the image and the current cell marker to the frame
                self.ims.append([im, red_dot])

            random.shuffle(directions)
            moved = False

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and \
                        self.maze.grid[2 * nx + 1 - dx, 2 * ny + 1 - dy] != Structures.WALL:
                    # print((dx, dy))
                    self.maze.grid[cell_x + dx, cell_y + dy] = Structures.SELECTED
                    current = (nx, ny)
                    moved = True
                    break

            if not moved:
                # print("we go back")
                # If no valid move found, backtrack to previous position
                self.path.pop()
                if not self.path:
                    # If path is empty, maze has no solution
                    break
                current = ((self.path[-1][0] - 1) // 2, (self.path[-1][1] - 1) // 2)

        if current == end:
            self.path.append((2 * end[0] + 1, 2 * end[1] + 1))
