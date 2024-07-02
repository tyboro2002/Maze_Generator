import random
from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation
from Maze import MazeGenerator
from settings import Structures


class RecursiveDivisionMazeGenerator(MazeGenerator):
    """
    A class to generate mazes using the Recursive Division Algorithm.

    Mazes can be created with recursive division, an algorithm which works as follows: Begin with the maze's space with
    no walls. Call this a chamber. Divide the chamber with a randomly positioned wall (or multiple walls) where each wall
    contains a randomly positioned passage opening within it. Then recursively repeat the process on the subchambers until
    all chambers are minimum sized. This method results in mazes with long straight walls crossing their space, making
    it easier to see which areas to avoid.

    For example, in a rectangular maze, build at random points two walls that are perpendicular to each other. These two
    walls divide the large chamber into four smaller chambers separated by four walls. Choose three of the four walls at
    random, and open a one cell-wide hole at a random point in each of the three. Continue in this manner recursively,
    until every chamber has a width of one cell in either of the two directions.
    """

    def __init__(self, maze):
        super().__init__(maze)

    def divide(self, x: int, y: int, width: int, height: int, orientation: str) -> None:
        """
        Recursively divide the space into smaller chambers.
        """
        if width <= 1 or height <= 1:
            return

        if orientation == 'H':
            wallx = x
            wally = y + (height // 2)  # TODO place wall random instead in mid
            passagex = wallx + random.randint(0, width - 1)
            passagey = wally
            dx = 1
            dy = 0
            length = width
            next_orientation = 'V'
        else:
            wallx = x + (width // 2)  # TODO place wall random instead in mid
            wally = y
            passagex = wallx
            passagey = wally + random.randint(0, height - 1)
            dx = 0
            dy = 1
            length = height
            next_orientation = 'H'

        for i in range(length):
            nextx = wallx + i * dx
            nexty = wally + i * dy

            if orientation == 'V':
                self.maze.grid[2 * nextx, 2 * nexty + 1] = Structures.WALL  # Set wall in the gray space
            else:
                self.maze.grid[2 * nextx + 1, 2 * nexty] = Structures.WALL  # Set wall in the gray space

            if (nextx, nexty) != (passagex, passagey):
                self.maze.grid[2 * nextx, 2 * nexty] = Structures.WALL  # Set wall in the gray space

        self.maze.grid[2 * passagex, 2 * passagey] = Structures.WALL

        if orientation == 'H':
            self.maze.grid[2 * passagex + 1, 2 * passagey] = Structures.SELECTED
        else:
            self.maze.grid[2 * passagex, 2 * passagey + 1] = Structures.SELECTED

        half_height = height // 2
        half_width = width // 2

        if orientation == 'H':
            self.divide(x, y + half_height, width, height - half_height, next_orientation)
            self.divide(x, y, width, half_height, next_orientation)
        else:
            self.divide(x + half_width, y, width - half_width, height, next_orientation)
            self.divide(x, y, half_width, height, next_orientation)

    def generate(self) -> None:
        """
        Generates a maze using the Recursive Division algorithm.
        """
        self.maze.grid.fill(Structures.SELECTED)  # Set all cells to paths
        self.maze.grid[0, :] = Structures.WALL  # Top boundary
        self.maze.grid[:, 0] = Structures.WALL  # Left boundary
        self.maze.grid[-1, :] = Structures.WALL  # Bottom boundary
        self.maze.grid[:, -1] = Structures.WALL  # Right boundary

        self.divide(0, 0, self.maze.width, self.maze.height, 'H')

    def animate(self) -> ArtistAnimation:
        """
        Generate an animation of the maze generation.
        :return: The animation of the maze generation.
        """
        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])

        ims = []

        self.maze.grid.fill(Structures.SELECTED)  # Set all cells to paths
        self.maze.grid[0, :] = Structures.WALL  # Top boundary
        self.maze.grid[:, 0] = Structures.WALL  # Left boundary
        self.maze.grid[-1, :] = Structures.WALL  # Bottom boundary
        self.maze.grid[:, -1] = Structures.WALL  # Right boundary
        steps = [(0, 0, self.maze.width, self.maze.height, 'H')]

        base_size = 10
        marker_size = base_size * min(1, base_size / max(self.maze.width, self.maze.height))

        while steps:
            x, y, width, height, orientation = steps.pop()
            if width <= 1 or height <= 1:
                continue

            if orientation == 'H':
                wallx = x
                wally = y + (height // 2)
                passagex = wallx + random.randint(0, width - 1)
                passagey = wally
                dx = 1
                dy = 0
                length = width
                next_orientation = 'V'
            else:
                wallx = x + (width // 2)
                wally = y
                passagex = wallx
                passagey = wally + random.randint(0, height - 1)
                dx = 0
                dy = 1
                length = height
                next_orientation = 'H'

            for i in range(length):
                nextx = wallx + i * dx
                nexty = wally + i * dy

                if orientation == 'V':
                    self.maze.grid[2 * nextx, 2 * nexty + 1] = Structures.WALL  # Set wall in the gray space
                else:
                    self.maze.grid[2 * nextx + 1, 2 * nexty] = Structures.WALL  # Set wall in the gray space

                if (nextx, nexty) != (passagex, passagey):
                    self.maze.grid[2 * nextx, 2 * nexty] = Structures.WALL  # Set wall in the gray space

            self.maze.grid[2 * passagex, 2 * passagey] = Structures.WALL

            if orientation == 'H':
                self.maze.grid[2 * passagex + 1, 2 * passagey] = Structures.SELECTED
            else:
                self.maze.grid[2 * passagex, 2 * passagey + 1] = Structures.SELECTED

            im = ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL, animated=True)
            red_dot, = ax.plot(
                2 * passagey + 1, 2 * passagex + 1,
                marker='o',
                color='red',
                markersize=marker_size,
                animated=True
            )
            ims.append([im, red_dot])

            half_height = height//2
            half_width = width//2

            if orientation == 'H':
                steps.append((x, y + half_height, width, height-half_height, next_orientation))
                steps.append((x, y, width, half_height, next_orientation))
            else:
                steps.append((x + half_width, y, width-half_width, height, next_orientation))
                steps.append((x, y, half_width, height, next_orientation))

        return ArtistAnimation(fig, ims, interval=100, blit=True)
