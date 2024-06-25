import random
from typing import List, Tuple

import numpy as np
from matplotlib import pyplot as plt, animation
from matplotlib.animation import Animation

from Maze import MazeGenerator
from settings import Structures


class Aldous_Broder(MazeGenerator):
    """
    A maze generator algorithm that generates mazes by the Aldous broder algorithm.
    The Aldous broder algorithm works as follows:
        Pick a random cell as the current cell and mark it as visited.
        While there are unvisited cells:
            Pick a random neighbour.
            If the chosen neighbour has not been visited:
                Remove the wall between the current cell and the chosen neighbour.
                Mark the chosen neighbour as visited.
            Make the chosen neighbour the current cell.

    This process ensures that the maze is fully connected and each cell is reachable from any other cell.
    """
    def __init__(self, maze) -> None:
        super().__init__(maze)
        self.visited = np.zeros((maze.height, maze.width), dtype=bool)
        self.unvisited_cells = maze.width * maze.height

    def generate(self) -> None:
        """
        Generates a maze with the Aldous_Broder algorithm.
        """
        self.maze.reset()

        # Pick a random starting cell
        current_x, current_y = random.randint(0, self.maze.width - 1), random.randint(0, self.maze.height - 1)
        self.visited[current_x, current_y] = True
        self.maze.grid[2 * current_x + 1, 2 * current_y + 1] = Structures.SELECTED  # Mark the cell as part of the maze
        self.unvisited_cells -= 1

        while self.unvisited_cells > 0:
            neighbors = self.get_neighbors(current_x, current_y)
            next_x, next_y, wall_x, wall_y = random.choice(neighbors)

            if not self.visited[next_x, next_y]:
                self.visited[next_x, next_y] = True
                self.maze.grid[2 * next_x + 1 - wall_x, 2 * next_y + 1 - wall_y] = Structures.SELECTED  # Remove the wall
                self.maze.grid[2 * next_x + 1, 2 * next_y + 1] = Structures.SELECTED  # Mark the cell as part of the maze
                self.unvisited_cells -= 1

            # Move to the chosen neighbor
            current_x, current_y = next_x, next_y

    def get_neighbors(self, x: int, y: int) -> List[Tuple[int, int, int, int]]:
        """
        Get all neighboring cells and walls for the cell at (x, y).

        Returns:
        --------
        neighbors : list of tuples
            A list of tuples representing the coordinates of neighboring cells and the walls.
        """
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for (dx, dy) in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height:
                neighbors.append((nx, ny, dx, dy))
        return neighbors

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
        current_x, current_y = random.randint(0, self.maze.width - 1), random.randint(0, self.maze.height - 1)
        self.visited[current_x, current_y] = True
        self.maze.grid[2 * current_x + 1, 2 * current_y + 1] = Structures.SELECTED  # Start cell
        self.unvisited_cells -= 1

        # Calculate marker size based on maze dimensions
        base_size = 10
        marker_size = base_size * min(1, base_size / max(self.maze.width, self.maze.height))

        while self.unvisited_cells > 0:
            neighbors = self.get_neighbors(current_x, current_y)
            next_x, next_y, wall_x, wall_y = random.choice(neighbors)

            if not self.visited[next_x, next_y]:
                self.visited[next_x, next_y] = True
                self.maze.grid[2 * next_x + 1 - wall_x, 2 * next_y + 1 - wall_y] = Structures.SELECTED  # Remove the wall
                self.maze.grid[2 * next_x + 1, 2 * next_y + 1] = Structures.SELECTED  # Mark the cell as part of the maze
                self.unvisited_cells -= 1

            # Create the image for the current frame
            im = ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL, animated=True)
            red_dot, = ax.plot(2 * next_y + 1, 2 * next_x + 1, marker='o', color='red', markersize=marker_size, animated=True)

            # Append the image and the current cell marker to the frame
            ims.append([im, red_dot])

            # Move to the chosen neighbor
            current_x, current_y = next_x, next_y

        return animation.ArtistAnimation(fig, ims, interval=100, blit=True)
