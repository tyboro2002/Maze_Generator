import random
from typing import List, Tuple

import numpy as np
from matplotlib import pyplot as plt, animation
from matplotlib.animation import Animation

from Maze import MazeGenerator
from settings import Structures


class DFSMazeGenerator(MazeGenerator):
    """
    A maze generator algorithm that generates mazes by the DFS algorithm.
    The DFS algorithm works as follows:
    1. Start with an initial cell and mark it as visited.
    2. Push the initial cell onto the stack.
    3. While there are cells in the stack:
       a. Peek at the cell on top of the stack (current cell).
       b. Find all unvisited neighbors of the current cell.
       c. If there are unvisited neighbors:
          i. Choose a random unvisited neighbor.
          ii. Remove the wall between the current cell and the chosen neighbor.
          iii. Mark the chosen neighbor as visited.
          iv. Push the chosen neighbor onto the stack.
       d. If there are no unvisited neighbors:
          i. Pop the current cell from the stack.

    This process ensures that the maze is fully connected and each cell is reachable from any other cell.
    """
    def __init__(self, maze, optimize_no_unvisited=False) -> None:
        super().__init__(maze)
        self.visited = np.zeros((maze.height, maze.width), dtype=np.bool_)
        self.stack = []
        self.unvisited_cells = maze.width * maze.height  # Total number of cells
        self.optimize_no_unvisited = optimize_no_unvisited

    def generate(self) -> None:
        """
        Generates a maze with the DFS algorithm.
        """
        self.maze.reset()
        start_x, start_y = 0, 0
        self.stack.append((start_x, start_y))
        self.visited[start_y, start_x] = True
        self.unvisited_cells -= 1

        loop = True

        while self.stack and loop:
            if self.optimize_no_unvisited and self.unvisited_cells <= 0:
                loop = False
            x, y = self.stack[-1]
            cell_x, cell_y = 2 * x + 1, 2 * y + 1
            self.maze.grid[cell_y, cell_x] = Structures.SELECTED

            # Get unvisited neighbors
            neighbors = self.get_unvisited_neighbors(x, y)
            if neighbors:
                next_x, next_y = random.choice(neighbors)
                wall_x, wall_y = cell_x + (next_x - x), cell_y + (next_y - y)
                self.maze.grid[wall_y, wall_x] = Structures.SELECTED
                self.stack.append((next_x, next_y))
                self.visited[next_y, next_x] = True
                self.unvisited_cells -= 1
            else:
                self.stack.pop()

    def get_unvisited_neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        """
        Get a list of unvisited neighbors of a cell in the maze.
        :param x: The x coordinate of the cell.
        :param y: The y coordinate of the cell.
        :return: A list of the cells neighbors.
        """
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and not self.visited[ny, nx]:
                neighbors.append((nx, ny))
        return neighbors

    def animate(self) -> Animation:
        """
        Generate an animation of the maze generation.
        :return: The animation of the maze generation.
        """
        # Adjust figure size based on maze dimensions
        fig, ax = plt.subplots(figsize=(max(self.maze.width / 5, 10), max(self.maze.height / 5, 10)))
        ax.set_xticks([]), ax.set_yticks([])

        ims = []

        self.maze.reset()
        self.stack = [(0, 0)]
        self.visited = np.zeros((self.maze.height, self.maze.width), dtype=np.bool_)
        self.visited[0, 0] = True
        self.unvisited_cells -= 1

        # Calculate marker size based on maze dimensions
        base_size = 10
        marker_size = base_size * min(1, base_size / max(self.maze.width, self.maze.height))

        loop = True

        while self.stack and loop:
            if self.optimize_no_unvisited and self.unvisited_cells <= 0:
                loop = False
            x, y = self.stack[-1]
            cell_x, cell_y = 2 * x + 1, 2 * y + 1
            self.maze.grid[cell_y, cell_x] = Structures.SELECTED

            # Create the image for the current frame
            im = ax.imshow(
                self.maze.grid.copy(),
                cmap='binary',
                vmin=Structures.EMPTY,
                vmax=Structures.WALL,
                animated=True
            )
            # Plot the current cell
            red_dot, = ax.plot(cell_x, cell_y, marker='o', color='red', markersize=marker_size, animated=True)

            # Append the image and the current cell marker to the frame
            ims.append([im, red_dot])

            neighbors = self.get_unvisited_neighbors(x, y)
            if neighbors:
                next_x, next_y = random.choice(neighbors)
                wall_x, wall_y = cell_x + (next_x - x), cell_y + (next_y - y)
                self.maze.grid[wall_y, wall_x] = Structures.SELECTED
                self.stack.append((next_x, next_y))
                self.visited[next_y, next_x] = True
                self.unvisited_cells -= 1
            else:
                self.stack.pop()

        im = ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL, animated=True)
        ims.append([im])

        # Return the animation object for further use if needed
        return animation.ArtistAnimation(fig, ims, interval=100, blit=True, repeat_delay=1000)
