import random
from typing import List, Tuple

import numpy as np
from matplotlib import pyplot as plt, animation
from matplotlib.animation import Animation
from Maze import Maze, MazeGenerator
from settings import Structures


class SpiralBacktrackerMazeGenerator(MazeGenerator):
    def __init__(self, maze: Maze) -> None:
        super().__init__(maze)
        self.visited = np.zeros((maze.height, maze.width), dtype=bool)
        self.stack = []

    def generate(self) -> None:
        self.maze.reset()
        cx, cy = self.maze.width // 2, self.maze.height // 2
        self.stack.append((cx, cy))
        self.visited[cx, cy] = True

        while self.stack:
            x, y = self.stack[-1]
            neighbors = self.get_unvisited_neighbors(x, y)

            if neighbors:
                nx, ny, wall_x, wall_y = random.choice(neighbors)
                self.maze.grid[2 * nx + 1, 2 * ny + 1] = Structures.EMPTY
                self.maze.grid[wall_x, wall_y] = Structures.EMPTY
                self.visited[nx, ny] = True
                self.stack.append((nx, ny))
            else:
                self.stack.pop()

        self.spiral(cx, cy)

    def spiral(self, x, y):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        length = 1
        dx, dy = directions[0]
        dir_index = 0

        while True:
            for _ in range(2):
                for _ in range(length):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and not self.visited[nx, ny]:
                        self.maze.grid[2 * nx + 1, 2 * ny + 1] = Structures.EMPTY
                        self.visited[nx, ny] = True
                    x, y = nx, ny
                dir_index = (dir_index + 1) % 4
                dx, dy = directions[dir_index]
            length += 1
            if x < 0 or x >= self.maze.width or y < 0 or y >= self.maze.height:
                break

    def get_unvisited_neighbors(self, x, y) -> List[Tuple[int, int, int, int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and not self.visited[nx, ny]:
                neighbors.append((nx, ny, 2 * x + 1 + dx, 2 * y + 1 + dy))
        return neighbors

    def animate(self) -> Animation:
        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])
        ims = []

        self.maze.reset()
        cx, cy = self.maze.width // 2, self.maze.height // 2
        self.stack.append((cx, cy))
        self.visited[cx, cy] = True

        while self.stack:
            x, y = self.stack[-1]
            neighbors = self.get_unvisited_neighbors(x, y)

            if neighbors:
                nx, ny, wall_x, wall_y = random.choice(neighbors)
                self.maze.grid[2 * nx + 1, 2 * ny + 1] = Structures.EMPTY
                self.maze.grid[wall_x, wall_y] = Structures.EMPTY
                self.visited[nx, ny] = True
                self.stack.append((nx, ny))
                im = ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL,
                               animated=True)
                ims.append([im])
            else:
                self.stack.pop()

        self.spiral(cx, cy)

        return animation.ArtistAnimation(fig, ims, interval=100, blit=True)
