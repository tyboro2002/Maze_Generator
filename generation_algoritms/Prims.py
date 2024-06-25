import random
from typing import List, Tuple

import numpy as np
from matplotlib import pyplot as plt, animation
from matplotlib.animation import Animation

from Maze import MazeGenerator
from settings import Structures


class PrimsMazeGenerator(MazeGenerator):
    """
    A class to generate mazes using Randomized Prim's Algorithm.

    The algorithm works as follows:
    1. Start with a grid full of walls.
    2. Choose a random cell, mark it as part of the maze. Add the walls of the cell to the wall list.
    3. While there are walls in the list:
       a. Pick a random wall from the list.
       b. If the cell on the opposite side isn't in the maze yet:
          i. Make the wall a passage and mark the cell on the opposite side as part of the maze.
          ii. Add the neighboring walls of the cell to the wall list.
       c. Remove the wall from the list.

    This process ensures that the maze is fully connected and each cell is reachable from any other cell.
    """

    def __init__(self, maze):
        super().__init__(maze)
        self.visited = np.zeros((maze.height, maze.width), dtype=np.bool_)
        self.walls = []

    def get_neighbors(self, x: int, y: int) -> List[Tuple[int, int, int, int]]:
        """
        Get all neighbors and walls for the cell at (x, y).

        Returns:
        --------
        neighbors : list of tuple
            A list of tuples representing the coordinates of neighboring cells and the walls.
        """
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for (dx, dy) in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and not self.visited[nx, ny]:
                neighbors.append((nx, ny, dx, dy))
        return neighbors

    def generate(self) -> None:
        """
        Generates a maze using Prim's algorithm.
        """
        self.maze.reset()

        # Start with a random cell
        start_x, start_y = random.randint(0, self.maze.width - 1), random.randint(0, self.maze.height - 1)
        self.visited[start_x, start_y] = True
        self.maze.grid[2 * start_x + 1, 2 * start_y + 1] = Structures.SELECTED  # Start cell
        self.walls.extend(self.get_neighbors(start_x, start_y))

        while self.walls:
            rand_wall = random.choice(self.walls)
            x, y, wx, wy = rand_wall
            if not self.visited[x, y]:
                self.visited[x, y] = True
                self.maze.grid[2 * x + 1 - wx, 2 * y + 1 - wy] = Structures.SELECTED  # Remove the wall
                self.maze.grid[2 * x + 1, 2 * y + 1] = Structures.SELECTED  # Mark the cell as part of the maze

                # Add the neighboring walls of the cell to the wall list
                self.walls.extend(self.get_neighbors(x, y))

            self.walls.remove(rand_wall)

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
        start_x, start_y = random.randint(0, self.maze.width - 1), random.randint(0, self.maze.height - 1)
        self.visited[start_x, start_y] = True
        self.maze.grid[2 * start_x + 1, 2 * start_y + 1] = Structures.SELECTED  # Start cell
        self.walls.extend(self.get_neighbors(start_x, start_y))

        # Calculate marker size based on maze dimensions
        base_size = 10
        marker_size = base_size * min(1, base_size / max(self.maze.width, self.maze.height))

        while self.walls:
            rand_wall = random.choice(self.walls)
            x, y, wx, wy = rand_wall
            if not self.visited[x, y]:
                self.visited[x, y] = True
                self.maze.grid[2 * x + 1 - wx, 2 * y + 1 - wy] = Structures.SELECTED  # Remove the wall
                self.maze.grid[2 * x + 1, 2 * y + 1] = Structures.SELECTED   # Mark the cell as part of the maze

                # Create the image for the current frame
                im = ax.imshow(
                    self.maze.grid.copy(),
                    cmap='binary',
                    vmin=Structures.EMPTY,
                    vmax=Structures.WALL,
                    animated=True
                )
                red_dot, = ax.plot(2*y+1, 2*x+1, marker='o', color='red', markersize=marker_size, animated=True)

                # Append the image and the current cell marker to the frame
                ims.append([im, red_dot])

                # Add the neighboring walls of the cell to the wall list
                self.walls.extend(self.get_neighbors(x, y))

            self.walls.remove(rand_wall)

        return animation.ArtistAnimation(fig, ims, interval=100, blit=True)
