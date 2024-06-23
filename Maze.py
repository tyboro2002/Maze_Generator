import numpy as np
import matplotlib.pyplot as plt


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Create a grid with walls (2) and cells (0)
        self.grid = np.zeros((2 * height + 1, 2 * width + 1), dtype=np.int8)
        self.grid[1::2, 1::2] = 0  # Paths
        self.grid[0::2, :] = 2  # Horizontal walls
        self.grid[:, 0::2] = 2  # Vertical walls

    def reset(self):
        self.grid.fill(2)
        self.grid[1::2, 1::2] = 0

    def display(self):
        plt.imshow(self.grid, cmap='binary', vmin=0, vmax=2)
        plt.xticks([]), plt.yticks([])
        # plt.show()


class MazeGenerator:
    def __init__(self, maze):
        self.maze = maze

    def generate(self):
        raise NotImplementedError("You should implement this method in subclasses.")

    def animate(self):
        raise NotImplementedError("You should implement this method in subclasses.")