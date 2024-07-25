import random
from typing import List
from matplotlib import pyplot as plt, animation
from matplotlib.animation import Animation
from Maze import Maze, MazeGenerator
from settings import Structures


class EllersMazeGenerator(MazeGenerator):
    """
    A maze generator algorithm that generates mazes by Eller's algorithm.
    Eller's algorithm works row by row, connecting and merging sets of cells to ensure the maze is fully connected.
    """

    def __init__(self, maze: Maze) -> None:
        super().__init__(maze)

    def generate(self) -> None:
        self.maze.reset()
        current_row = [0] * self.maze.width
        next_set = 1
        sets = {}

        for y in range(self.maze.height):
            # Assign sets to the current row
            for x in range(self.maze.width):
                if current_row[x] == 0:
                    current_row[x] = next_set
                    sets[next_set] = [x]
                    next_set += 1

            # Randomly create horizontal connections
            for x in range(self.maze.width - 1):
                if current_row[x] != current_row[x + 1] and random.choice([True, False]):
                    self.maze.grid[2 * x + 2, 2 * y + 1] = Structures.EMPTY
                    self._merge_sets(current_row, current_row[x + 1], current_row[x], sets)

            # Create vertical connections for each set
            if y != self.maze.height - 1:
                next_row = [0] * self.maze.width
                vertical_connections = set()

                for s in sets.values():
                    if len(s) > 0:
                        x = random.choice(s)
                        self.maze.grid[2 * x + 1, 2 * y + 2] = Structures.EMPTY
                        next_row[x] = current_row[x]
                        vertical_connections.add(current_row[x])

                for x in range(self.maze.width):
                    if next_row[x] == 0 and random.choice([True, False]):
                        self.maze.grid[2 * x + 1, 2 * y + 2] = Structures.EMPTY
                        next_row[x] = current_row[x]
                        vertical_connections.add(current_row[x])

                current_row = next_row
                sets = {k: [i for i, v in enumerate(current_row) if v == k] for k in vertical_connections}
            else:
                for x in range(self.maze.width - 1):
                    if current_row[x] != current_row[x + 1]:
                        self.maze.grid[2 * x + 2, 2 * y + 1] = Structures.EMPTY
                        self._merge_sets(current_row, current_row[x + 1], current_row[x], sets)

    def _merge_sets(self, row: List[int], set_to_replace: int, replacement_set: int, sets: dict) -> None:
        for x in range(len(row)):
            if row[x] == set_to_replace:
                row[x] = replacement_set
                sets[replacement_set].append(x)
        sets[set_to_replace] = []

    def animate(self) -> Animation:
        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])
        ims = []

        self.maze.reset()
        current_row = [0] * self.maze.width
        next_set = 1
        sets = {}

        for y in range(self.maze.height):
            for x in range(self.maze.width):
                if current_row[x] == 0:
                    current_row[x] = next_set
                    sets[next_set] = [x]
                    next_set += 1

            for x in range(self.maze.width - 1):
                if current_row[x] != current_row[x + 1] and random.choice([True, False]):
                    self.maze.grid[2 * x + 2, 2 * y + 1] = Structures.EMPTY
                    self._merge_sets(current_row, current_row[x + 1], current_row[x], sets)
                    im = ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL,
                                   animated=True)
                    ims.append([im])

            if y != self.maze.height - 1:
                next_row = [0] * self.maze.width
                vertical_connections = set()

                for s in sets.values():
                    if len(s) > 0:
                        x = random.choice(s)
                        self.maze.grid[2 * x + 1, 2 * y + 2] = Structures.EMPTY
                        next_row[x] = current_row[x]
                        vertical_connections.add(current_row[x])

                for x in range(self.maze.width):
                    if next_row[x] == 0 and random.choice([True, False]):
                        self.maze.grid[2 * x + 1, 2 * y + 2] = Structures.EMPTY
                        next_row[x] = current_row[x]
                        vertical_connections.add(current_row[x])
                        im = ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY,
                                       vmax=Structures.WALL, animated=True)
                        ims.append([im])
                current_row = next_row
                sets = {k: [i for i, v in enumerate(current_row) if v == k] for k in vertical_connections}
            else:
                for x in range(self.maze.width - 1):
                    if current_row[x] != current_row[x + 1]:
                        self.maze.grid[2 * x + 2, 2 * y + 1] = Structures.EMPTY
                        self._merge_sets(current_row, current_row[x + 1], current_row[x], sets)
                        im = ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY,
                                       vmax=Structures.WALL, animated=True)
                        ims.append([im])

        return animation.ArtistAnimation(fig, ims, interval=100, blit=True)
