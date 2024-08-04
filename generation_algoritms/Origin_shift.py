import random
from typing import List, Tuple

import numpy as np
from matplotlib import pyplot as plt, animation
from matplotlib.animation import Animation

from Maze import MazeGenerator
from settings import Structures, origin_shift_iterations


class Node:
    def __init__(self):
        self.direction = None  # This will be a tuple representing the direction (dx, dy)


class OriginShiftGenerator(MazeGenerator):
    def __init__(self, maze):
        super().__init__(maze)
        self.grid = [[Node() for _ in range(maze.width)] for _ in range(maze.height)]
        self.origin = (0, 0)

    def initialize_perfect_maze(self):
        """
        Initialize the grid with all horizontal paths connected by one vertical path.
        """
        # Initialize the visited array
        self.visited = np.zeros((self.maze.height, self.maze.width), dtype=np.bool_)

        # Create horizontal paths
        for y in range(self.maze.height):
            for x in range(self.maze.width - 1):
                self.grid[y][x].direction = (0, 1)
                self.visited[y][x] = True

        # Create vertical path connecting horizontal paths
        for y in range(self.maze.height - 1):
            self.grid[y][self.maze.width - 1].direction = (1, 0)
            self.visited[y][self.maze.width - 1] = True

        # Set the last cell in the bottom right to point nowhere and mark it visited
        self.visited[self.maze.height - 1][self.maze.width - 1] = True

        # Set the origin to be the last cell in the bottom right
        self.origin = (self.maze.height - 1, self.maze.width - 1)

    def get_unvisited_neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        """
        Get all unvisited neighbors of the cell at (x, y).
        """
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for (dx, dy) in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and not self.visited[nx][ny]:
                neighbors.append((nx, ny))
        return neighbors

    def iterate(self):
        """
        Perform one iteration of the algorithm.
        """
        x, y = self.origin
        neighbors = self.get_neighbors(x, y)
        if neighbors:
            nx, ny = random.choice(neighbors)
            self.grid[x][y].direction = (nx - x, ny - y)
            self.grid[nx][ny].direction = None
            self.origin = (nx, ny)

    def get_neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        """
        Get all neighbors of the cell at (x, y).
        """
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for (dx, dy) in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height:
                neighbors.append((nx, ny))
        return neighbors

    def generate(self, iterations: int = origin_shift_iterations) -> None:
        """
        Generate the maze with the given number of iterations.
        """
        self.initialize_perfect_maze()
        for _ in range(iterations):
            self.iterate()
        self.update_maze_grid()

    def update_maze_grid(self):
        """
        Update the maze grid based on the node directions.
        """
        self.maze.reset()
        for x in range(self.maze.width):
            for y in range(self.maze.height):
                if self.grid[x][y].direction is not None:
                    dx, dy = self.grid[x][y].direction
                    nx, ny = x + dx, y + dy
                    self.maze.grid[2 * x + 1, 2 * y + 1] = Structures.EMPTY
                    self.maze.grid[2 * nx + 1, 2 * ny + 1] = Structures.EMPTY
                    self.maze.grid[2 * x + 1 + dx, 2 * y + 1 + dy] = Structures.EMPTY

    def animate(self, iterations: int = origin_shift_iterations) -> Animation:
        """
        Generate an animation of the maze generation.
        :return: The animation of the maze generation.
        """
        # Adjust figure size based on maze dimensions
        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])

        ims = []

        self.initialize_perfect_maze()

        # Create the image for the initial grid
        im = ax.imshow(
            self.maze.grid.copy(),
            cmap='binary',
            vmin=Structures.EMPTY,
            vmax=Structures.WALL,
            animated=True
        )
        ims.append([im])

        # Iteratively update the grid and capture each step
        for _ in range(iterations):
            self.iterate()
            self.update_maze_grid()
            im = ax.imshow(
                self.maze.grid.copy(),
                cmap='binary',
                vmin=Structures.EMPTY,
                vmax=Structures.WALL,
                animated=True
            )
            ims.append([im])

        return animation.ArtistAnimation(fig, ims, interval=100, blit=True)
