import random
from typing import List, Tuple

import numpy as np
from matplotlib import pyplot as plt, animation
from matplotlib.animation import Animation

from Maze import MazeGenerator
from settings import Structures


class RandomizedKruskalSetMazeGenerator(MazeGenerator):
    """
    A class to generate mazes using the randomized Kruskal's Algorithm.

    The algorithm works as follows:
        Create a list of all walls, and create a set for each cell, each containing just that one cell.
        For each wall, in some random order:
          If the cells divided by this wall belong to distinct sets:
             Remove the current wall.
             Join the sets of the formerly divided cells.

    This process ensures that the maze is fully connected and each cell is reachable from any other cell.
    """

    def __init__(self, maze):
        super().__init__(maze)
        self.sets = [set([(x, y)]) for x in range(maze.width) for y in range(maze.height)]
        self.walls = self._initialize_walls()

    def _initialize_walls(self) -> List[Tuple[int, int, int, int]]:
        """
        Initialize all the walls in the maze.
        """
        walls = []
        for x in range(self.maze.width):
            for y in range(self.maze.height):
                if x < self.maze.width - 1:
                    walls.append((x, y, x + 1, y))  # Vertical wall
                if y < self.maze.height - 1:
                    walls.append((x, y, x, y + 1))  # Horizontal wall
        random.shuffle(walls)
        return walls

    def find_set(self, cell: Tuple[int, int]) -> set | None:
        """
        Find the set that contains the given cell.
        """
        for s in self.sets:
            if cell in s:
                return s
        return None

    def generate(self) -> None:
        """
        Generates a maze using the iterative randomized Kruskal's algorithm.
        """
        self.maze.reset()

        while self.walls:
            x1, y1, x2, y2 = self.walls.pop()
            set1 = self.find_set((x1, y1))
            set2 = self.find_set((x2, y2))

            if set1 != set2:
                fx = 2 * x1 + 1
                fy = 2 * y1 + 1
                sx = 2 * x2 + 1
                sy = 2 * y2 + 1
                # Remove the wall between the cells
                wall_x = (fx + sx) // 2
                wall_y = (fy + sy) // 2
                self.maze.grid[wall_x, wall_y] = Structures.SELECTED
                self.maze.grid[fx, fy] = Structures.SELECTED
                self.maze.grid[sx, sy] = Structures.SELECTED

                # Merge the sets
                self.sets.remove(set1)
                set1.update(set2)
                self.sets.append(set1)
                self.sets.remove(set2)

    def animate(self) -> Animation:
        """
        Generate an animation of the maze generation.
        :return: The animation of the maze generation.
        """
        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])

        ims = []

        self.maze.reset()
        walls = self._initialize_walls()
        self.sets = [set([(x, y)]) for x in range(self.maze.width) for y in range(self.maze.height)]

        # Calculate marker size based on maze dimensions
        base_size = 10
        marker_size = base_size * min(1, base_size / max(self.maze.width, self.maze.height))

        while walls:
            x1, y1, x2, y2 = walls.pop()
            set1 = self.find_set((x1, y1))
            set2 = self.find_set((x2, y2))

            if set1 != set2:
                fx = 2 * x1 + 1
                fy = 2 * y1 + 1
                sx = 2 * x2 + 1
                sy = 2 * y2 + 1
                # Remove the wall between the cells
                wall_x = (fx + sx)//2
                wall_y = (fy + sy)//2
                self.maze.grid[wall_x, wall_y] = Structures.SELECTED
                self.maze.grid[fx, fy] = Structures.SELECTED
                self.maze.grid[sx, sy] = Structures.SELECTED

                # Merge the sets
                self.sets.remove(set1)
                set1.update(set2)
                self.sets.append(set1)
                self.sets.remove(set2)

                # Create the image for the current frame
                im = ax.imshow(
                    self.maze.grid.copy(),
                    cmap='binary',
                    vmin=Structures.EMPTY,
                    vmax=Structures.WALL,
                    animated=True
                )
                red_dot1, = ax.plot(fy, fx, marker='o', color='red', markersize=marker_size, animated=True)
                red_dot2, = ax.plot(sy, sx, marker='o', color='red', markersize=marker_size, animated=True)

                # Append the image and the current cell marker to the frame
                ims.append([im, red_dot1, red_dot2])

        return animation.ArtistAnimation(fig, ims, interval=100, blit=True)
