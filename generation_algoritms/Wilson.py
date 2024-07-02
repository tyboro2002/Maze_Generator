import random
from typing import List, Tuple
from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation
from Maze import MazeGenerator
from settings import Structures


class WilsonMazeGenerator(MazeGenerator):
    """
    A class to generate mazes using Wilson's Algorithm.

    We begin the algorithm by initializing the maze with one cell chosen arbitrarily.
    Then we start at a new cell chosen arbitrarily, and perform a random walk until we reach a cell already
    in the maze—however, if at any point the random walk reaches its own path, forming a loop, we erase the loop from the
    path before proceeding. When the path reaches the maze, we add it to the maze. Then we perform another loop-erased
    random walk from another arbitrary starting cell, repeating until all cells have been filled.
    """

    def __init__(self, maze):
        super().__init__(maze)
        self.visited = set()

    def random_walk(self, start: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Perform a random walk starting from the given cell.
        """
        path = [start]
        current = start
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while current not in self.visited:
            nx, ny = tuple(map(sum, zip(current, random.choice(directions))))
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height:
                if (nx, ny) in path:
                    # Erase loop
                    loop_start = path.index((nx, ny))
                    path = path[:loop_start + 1]
                else:
                    path.append((nx, ny))
            current = path[-1]

        return path

    def generate(self) -> None:
        """
        Generates a maze using Wilson's algorithm.
        """
        self.maze.reset()
        start_x, start_y = random.randint(0, self.maze.width - 1), random.randint(0, self.maze.height - 1)
        self.visited.add((start_x, start_y))

        while len(self.visited) < self.maze.width * self.maze.height:
            unvisited_cells = [(x, y) for x in range(self.maze.width) for y in range(self.maze.height) if (x, y) not in self.visited]
            start_cell = random.choice(unvisited_cells)
            path = self.random_walk(start_cell)

            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                self.visited.add((x1, y1))
                self.visited.add((x2, y2))
                fx = 2 * x1 + 1
                fy = 2 * y1 + 1
                sx = 2 * x2 + 1
                sy = 2 * y2 + 1
                wall_x, wall_y = (fx + sx) // 2, (fy + sy) // 2
                self.maze.grid[fx, fy] = Structures.SELECTED
                self.maze.grid[sx, sy] = Structures.SELECTED
                self.maze.grid[wall_x, wall_y] = Structures.SELECTED

    def animate(self) -> ArtistAnimation:
        """
        Generate an animation of the maze generation.
        :return: The animation of the maze generation.
        """
        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])

        ims = []

        self.maze.reset()
        start_x, start_y = random.randint(0, self.maze.width - 1), random.randint(0, self.maze.height - 1)
        self.visited = {(start_x, start_y)}

        base_size = 10
        marker_size = base_size * min(1, base_size / max(self.maze.width, self.maze.height))

        while len(self.visited) < self.maze.width * self.maze.height:
            unvisited_cells = [(x, y) for x in range(self.maze.width) for y in range(self.maze.height) if (x, y) not in self.visited]
            start_cell = random.choice(unvisited_cells)
            path = self.random_walk(start_cell)

            for i in range(len(path) - 1):
                x1, y1 = path[i]
                x2, y2 = path[i + 1]
                self.visited.add((x1, y1))
                self.visited.add((x2, y2))
                fx = 2*x1+1
                fy = 2*y1+1
                sx = 2*x2+1
                sy = 2*y2+1
                wall_x, wall_y = (fx + sx) // 2, (fy + sy) // 2
                self.maze.grid[fx, fy] = Structures.SELECTED
                self.maze.grid[sx, sy] = Structures.SELECTED
                self.maze.grid[wall_x, wall_y] = Structures.SELECTED

                # Create the image for the current frame
                im = ax.imshow(
                    self.maze.grid.copy(),
                    cmap='binary',
                    vmin=Structures.EMPTY,
                    vmax=Structures.WALL,
                    animated=True
                )
                red_dot, = ax.plot(
                    2 * y2 + 1, 2 * x2 + 1,
                    marker='o',
                    color='red',
                    markersize=marker_size,
                    animated=True
                )
                ims.append([im, red_dot])

        return ArtistAnimation(fig, ims, interval=100, blit=True)
