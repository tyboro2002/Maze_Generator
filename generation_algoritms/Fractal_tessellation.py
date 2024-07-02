import random
from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation

from Maze import MazeGenerator
from settings import Structures


class FractalTessellationMazeGenerator(MazeGenerator):
    """
    A maze generator algorithm that generates mazes by the Fractal Tessellation algorithm.

    On each iteration, this algorithm creates a maze twice the size by copying itself 3 times.
    At the end of each iteration, 3 paths are opened between the 4 smaller mazes.
    """
    def __init__(self, maze):
        super().__init__(maze)
        self.current_width = 1
        self.current_height = 1

    def expand_maze(self):
        region = self.maze.grid[0:2*self.current_height+1, 0:2*self.current_width+1].copy()
        self.maze.grid[
            2*self.current_height:4*self.current_height+1, 2*self.current_width:4*self.current_width+1
        ] = region
        self.maze.grid[
            2 * self.current_height:4 * self.current_height + 1, 0:2 * self.current_width + 1
        ] = region
        self.maze.grid[
            0:2*self.current_height+1, 2*self.current_width:4*self.current_width+1
        ] = region
        upp_wall = random.randint(1, self.current_height)
        bottom_wall = random.randint(self.current_height, 2*self.current_height-1)
        right_wall = random.randint(self.current_width, 2*self.current_width-1)
        left_wall = random.randint(1, self.current_width)
        pos_arrangements = ['lbu', 'rbu', 'lru', 'rlb']
        arrangement = random.choice(pos_arrangements)
        if 'r' in arrangement:
            self.maze.grid[(2 * self.current_height, 2 * right_wall+1)] = Structures.SELECTED
        if 'b' in arrangement:
            self.maze.grid[(2 * bottom_wall + 1, 2 * self.current_width)] = Structures.SELECTED
        if 'u' in arrangement:
            self.maze.grid[(2 * upp_wall - 1, 2 * self.current_width)] = Structures.SELECTED
        if 'l' in arrangement:
            self.maze.grid[(2 * self.current_height, 2 * left_wall-1)] = Structures.SELECTED
        self.current_width *= 2
        self.current_height *= 2
        # print(f"expanded width: {self.current_width//2}, height: {self.current_height//2}")
        # print(f"to width: {self.current_width}, height: {self.current_height}")
        # print()

    def generate(self):
        self.maze.reset()
        # Initialize the maze with a single cell as a path
        self.maze.grid[1, 1] = Structures.SELECTED
        while self.current_width < self.maze.width or self.current_height < self.maze.height:
            self.expand_maze()

    def animate(self):
        fig, ax = plt.subplots(figsize=(max(self.maze.width / 5, 10), max(self.maze.height / 5, 10)))
        ax.set_xticks([]), ax.set_yticks([])

        ims = []

        self.maze.reset()
        self.maze.grid[1, 1] = Structures.SELECTED
        # append the initial state
        im = ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL,
                       animated=True)
        ims.append([im])

        # expand until size is found
        while self.current_width < self.maze.width or self.current_height < self.maze.height:
            self.expand_maze()
            im = ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL,
                           animated=True)
            ims.append([im])

        return ArtistAnimation(fig, ims, interval=100, blit=True)
