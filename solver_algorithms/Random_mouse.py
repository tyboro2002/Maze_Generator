import random

import matplotlib.pyplot as plt

from Maze import Solver
from settings import Structures


class RandomMouseSolver(Solver):
    """
    This simple method can be implemented by a very unintelligent robot or perhaps a mouse, because it does not
    require any memory. The robot proceeds following a random decision about the next direction to follow.
    """
    def __init__(self, maze):
        super().__init__(maze)
        self.maze.grid[self.maze.grid == Structures.SELECTED] = Structures.EMPTY

    def solve_step(self, start, end, animate):
        self._random_mouse(start, end, animate=animate)

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
                # If no valid move found, backtrack to previous position
                self.path.pop()
                if not self.path:
                    # If path is empty, maze has no solution
                    break
                current = ((self.path[-1][0] - 1) // 2, (self.path[-1][1] - 1) // 2)

        if current == end:
            self.path.append((2 * end[0] + 1, 2 * end[1] + 1))
