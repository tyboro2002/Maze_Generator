import random
from typing import List, Tuple

import numpy as np
from matplotlib import pyplot as plt, animation
from matplotlib.animation import Animation

from Maze import MazeGenerator
from settings import Structures


class UnicursalMazeGenerator(MazeGenerator):
    """
    A class to generate unicursal mazes (mazes with a single continuous path).

    The algorithm works as follows:
    1. Start with an empty grid.
    2. Create a simple closed curve (e.g., a serpentine path).
    3. Use a variation of the wall-following algorithm to carve out the path.
    4. Ensure the maze has no branches or dead ends.
    """

    def __init__(self, maze):
        super().__init__(maze)
        self.visited = np.zeros((maze.height, maze.width), dtype=np.bool_)
        self.path = []

    def create_path(self) -> List[Tuple[int, int]]:
        """
        Create a simple closed curve (serpentine path) that visits each cell once.

        Returns:
        --------
        path : list of tuple
            A list of tuples representing the coordinates of the path.
        """
        path = []
        direction = 1
        for y in range(self.maze.height):
            if direction == 1:
                for x in range(self.maze.width):
                    path.append((x, y))
            else:
                for x in range(self.maze.width - 1, -1, -1):
                    path.append((x, y))
            direction *= -1
        return path

    def generate(self) -> None:
        """
        Generates a unicursal maze.
        """
        self.maze.reset()

        # Create the path
        self.path = self.create_path()

        # Carve the path into the maze
        for i in range(len(self.path) - 1):
            x1, y1 = self.path[i]
            x2, y2 = self.path[i + 1]
            self.maze.grid[2 * x1 + 1, 2 * y1 + 1] = Structures.EMPTY
            self.maze.grid[2 * x2 + 1, 2 * y2 + 1] = Structures.EMPTY
            self.maze.grid[(2 * x1 + 1 + 2 * x2 + 1) // 2, (2 * y1 + 1 + 2 * y2 + 1) // 2] = Structures.EMPTY

    def animate(self) -> Animation:
        """
        Generate an animation of the maze generation.
        :return: The animation of the maze generation.
        """
        # Adjust figure size based on maze dimensions
        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])

        ims = []

        self.maze.reset()
        self.path = self.create_path()

        # Calculate marker size based on maze dimensions
        base_size = 10
        marker_size = base_size * min(1, base_size / max(self.maze.width, self.maze.height))

        for i in range(len(self.path) - 1):
            x1, y1 = self.path[i]
            x2, y2 = self.path[i + 1]
            self.maze.grid[2 * x1 + 1, 2 * y1 + 1] = Structures.EMPTY
            self.maze.grid[2 * x2 + 1, 2 * y2 + 1] = Structures.EMPTY
            self.maze.grid[(2 * x1 + 1 + 2 * x2 + 1) // 2, (2 * y1 + 1 + 2 * y2 + 1) // 2] = Structures.EMPTY

            # Create the image for the current frame
            im = ax.imshow(
                self.maze.grid.copy(),
                cmap='binary',
                vmin=Structures.EMPTY,
                vmax=Structures.WALL,
                animated=True
            )
            red_dot, = ax.plot(2 * y1 + 1, 2 * x1 + 1, marker='o', color='red', markersize=marker_size, animated=True)

            # Append the image and the current cell marker to the frame
            ims.append([im, red_dot])

        return animation.ArtistAnimation(fig, ims, interval=100, blit=True)
