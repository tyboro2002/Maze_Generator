import random

import numpy as np
from matplotlib import pyplot as plt, animation

from Maze import MazeGenerator


class DFSMazeGenerator(MazeGenerator):
    def __init__(self, maze):
        super().__init__(maze)
        self.visited = np.zeros((maze.height, maze.width), dtype=np.bool_)
        self.stack = []

    def generate(self):
        self.maze.reset()
        start_x, start_y = 0, 0
        self.stack.append((start_x, start_y))
        self.visited[start_y, start_x] = True

        while self.stack:
            x, y = self.stack[-1]
            cell_x, cell_y = 2 * x + 1, 2 * y + 1
            self.maze.grid[cell_y, cell_x] = 1

            # Get unvisited neighbors
            neighbors = self.get_unvisited_neighbors(x, y)
            if neighbors:
                next_x, next_y = random.choice(neighbors)
                wall_x, wall_y = cell_x + (next_x - x), cell_y + (next_y - y)
                self.maze.grid[wall_y, wall_x] = 1
                self.stack.append((next_x, next_y))
                self.visited[next_y, next_x] = True
            else:
                self.stack.pop()

    def get_unvisited_neighbors(self, x, y):
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and not self.visited[ny, nx]:
                neighbors.append((nx, ny))
        return neighbors

    def animate(self):
        fig, ax = plt.subplots()
        ax.set_xticks([]), ax.set_yticks([])

        ims = []

        self.maze.reset()
        self.stack = [(0, 0)]
        self.visited = np.zeros((self.maze.height, self.maze.width), dtype=np.bool_)
        self.visited[0, 0] = True

        while self.stack:
            x, y = self.stack[-1]
            cell_x, cell_y = 2 * x + 1, 2 * y + 1
            self.maze.grid[cell_y, cell_x] = 1
            # ax.plot(cell_x, cell_y, marker='o', color='red', markersize=10)  # Highlight current cell
            im = ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=0, vmax=2, animated=True)
            ims.append([im])
            neighbors = self.get_unvisited_neighbors(x, y)
            if neighbors:
                next_x, next_y = random.choice(neighbors)
                wall_x, wall_y = cell_x + (next_x - x), cell_y + (next_y - y)
                self.maze.grid[wall_y, wall_x] = 1
                self.stack.append((next_x, next_y))
                self.visited[next_y, next_x] = True
            else:
                self.stack.pop()

        ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True, repeat_delay=1000)
        # plt.show()
        return ani  # Return the animation object for further use if needed