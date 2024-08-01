import random

import numpy as np
from matplotlib import pyplot as plt, animation
from matplotlib.animation import Animation
from Maze import Maze, MazeGenerator
from settings import Structures


class HuntAndKillMazeGenerator(MazeGenerator):
    def __init__(self, maze: Maze) -> None:
        super().__init__(maze)
        self.visited = np.zeros((maze.height, maze.width), dtype=bool)

    def generate(self) -> None:
        self.maze.reset()
        current_x, current_y = random.randint(0, self.maze.width - 1), random.randint(0, self.maze.height - 1)
        self.visited[current_x, current_y] = True

        while not np.all(self.visited):
            neighbors = self.get_unvisited_neighbors(current_x, current_y)
            if neighbors:
                next_x, next_y, wall_x, wall_y = random.choice(neighbors)
                self.maze.grid[2 * next_x + 1, 2 * next_y + 1] = Structures.EMPTY
                self.maze.grid[wall_x, wall_y] = Structures.EMPTY
                self.visited[next_x, next_y] = True
                current_x, current_y = next_x, next_y
            else:
                current_x, current_y = self.hunt()

    def hunt(self):
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                if not self.visited[x, y] and any(self.visited[nx, ny] for nx, ny, _, _ in self.get_neighbors(x, y)):
                    # Connect the new cell to an adjacent visited cell
                    connected = False
                    for nx, ny, wall_x, wall_y in self.get_neighbors(x, y):
                        if self.visited[nx, ny]:
                            self.maze.grid[2 * x + 1, 2 * y + 1] = Structures.EMPTY
                            self.maze.grid[wall_x, wall_y] = Structures.EMPTY
                            self.visited[x, y] = True
                            connected = True
                            break
                    if connected:
                        return x, y
        return None

    def get_unvisited_neighbors(self, x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and not self.visited[nx, ny]:
                neighbors.append((nx, ny, 2 * x + 1 + dx, 2 * y + 1 + dy))
        return neighbors

    def get_neighbors(self, x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height:
                neighbors.append((nx, ny, 2 * x + 1 + dx, 2 * y + 1 + dy))
        return neighbors

    def animate(self) -> Animation:
        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])
        ims = []

        self.maze.reset()
        current_x, current_y = random.randint(0, self.maze.width - 1), random.randint(0, self.maze.height - 1)
        self.visited[current_x, current_y] = True

        while not np.all(self.visited):
            neighbors = self.get_unvisited_neighbors(current_x, current_y)
            if neighbors:
                next_x, next_y, wall_x, wall_y = random.choice(neighbors)
                self.maze.grid[2 * next_x + 1, 2 * next_y + 1] = Structures.EMPTY
                self.maze.grid[wall_x, wall_y] = Structures.EMPTY
                self.visited[next_x, next_y] = True
                current_x, current_y = next_x, next_y
                im = ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL,
                               animated=True)
                ims.append([im])
            else:
                current_x, current_y = self.hunt()

        return animation.ArtistAnimation(fig, ims, interval=100, blit=True)
