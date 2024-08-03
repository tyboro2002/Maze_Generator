import random

from matplotlib import pyplot as plt, animation
from matplotlib.animation import Animation

from Maze import MazeGenerator
from settings import Structures


class BinaryTreeMazeGenerator(MazeGenerator):
    """
    A class to generate mazes using the Binary Tree algorithm.

    The algorithm works as follows:
    1. For each cell in the grid, randomly choose to remove either the north or west wall (or both).
    2. This creates a maze with a strong diagonal bias, but is very efficient to generate.
    """

    def __init__(self, maze):
        super().__init__(maze)

    def generate(self) -> None:
        """
        Generates a maze using the Binary Tree algorithm.
        """
        self.maze.reset()

        for x in range(self.maze.width):
            for y in range(self.maze.height):
                if x > 0 and y > 0:
                    direction = random.choice(['north', 'west'])
                elif x > 0:
                    direction = 'west'
                elif y > 0:
                    direction = 'north'
                else:
                    continue

                if direction == 'north':
                    self.maze.grid[2 * x + 1, 2 * y] = Structures.EMPTY
                elif direction == 'west':
                    self.maze.grid[2 * x, 2 * y + 1] = Structures.EMPTY

                self.maze.grid[2 * x + 1, 2 * y + 1] = Structures.EMPTY

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

        # Calculate marker size based on maze dimensions
        base_size = 10
        marker_size = base_size * min(1, base_size / max(self.maze.width, self.maze.height))

        for x in range(self.maze.width):
            for y in range(self.maze.height):
                if x > 0 and y > 0:
                    direction = random.choice(['north', 'west'])
                elif x > 0:
                    direction = 'west'
                elif y > 0:
                    direction = 'north'
                else:
                    continue

                if direction == 'north':
                    self.maze.grid[2 * x + 1, 2 * y] = Structures.EMPTY
                elif direction == 'west':
                    self.maze.grid[2 * x, 2 * y + 1] = Structures.EMPTY

                self.maze.grid[2 * x + 1, 2 * y + 1] = Structures.EMPTY

                # Create the image for the current frame
                im = ax.imshow(
                    self.maze.grid.copy(),
                    cmap='binary',
                    vmin=Structures.EMPTY,
                    vmax=Structures.WALL,
                    animated=True
                )
                red_dot, = ax.plot(2 * y + 1, 2 * x + 1, marker='o', color='red', markersize=marker_size, animated=True)

                # Append the image and the current cell marker to the frame
                ims.append([im, red_dot])

        return animation.ArtistAnimation(fig, ims, interval=100, blit=True)
