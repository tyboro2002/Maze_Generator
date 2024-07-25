import random

from matplotlib import pyplot as plt, animation
from matplotlib.animation import Animation

from Maze import Maze, MazeGenerator
from settings import Structures


class SidewinderMazeGenerator(MazeGenerator):
    """
    A maze generator algorithm that generates mazes by the Sidewinder algorithm.
    The Sidewinder algorithm works as follows:
        Start with the top row and work left to right.
        For each cell, decide whether to carve a passage to the east.
        If carving east is chosen, connect it and continue.
        If not, close out the current run with a passage north to a random cell within the run.
        Move to the next row and repeat until the maze is complete.

    This process ensures that the maze is fully connected and each cell is reachable from any other cell.
    """

    def __init__(self, maze: Maze) -> None:
        super().__init__(maze)

    def generate(self) -> None:
        """
        Generates a maze with the Sidewinder algorithm.
        """
        self.maze.reset()

        for y in range(self.maze.height):
            run = []
            for x in range(self.maze.width):
                run.append((x, y))

                at_eastern_boundary = (x == self.maze.width - 1)
                at_northern_boundary = (y == 0)
                should_close_out = at_eastern_boundary or (not at_northern_boundary and random.choice([True, False]))

                if should_close_out:
                    member_x, member_y = random.choice(run)
                    if member_y > 0:
                        self.maze.grid[2 * member_x + 1, 2 * member_y] = Structures.EMPTY  # carve north
                    run = []
                else:
                    self.maze.grid[2 * x + 2, 2 * y + 1] = Structures.EMPTY  # carve east

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

        for y in range(self.maze.height):
            run = []
            for x in range(self.maze.width):
                run.append((x, y))

                at_eastern_boundary = (x == self.maze.width - 1)
                at_northern_boundary = (y == 0)
                should_close_out = at_eastern_boundary or (not at_northern_boundary and random.choice([True, False]))

                if should_close_out:
                    member_x, member_y = random.choice(run)
                    if member_y > 0:
                        self.maze.grid[2 * member_x + 1, 2 * member_y] = Structures.EMPTY  # carve north
                        im = ax.imshow(
                            self.maze.grid.copy(),
                            cmap='binary',
                            vmin=Structures.EMPTY,
                            vmax=Structures.WALL,
                            animated=True
                        )
                        ims.append([im])
                    run = []
                else:
                    pass
                    self.maze.grid[2 * x + 2, 2 * y + 1] = Structures.EMPTY  # carve east
                    im = ax.imshow(
                        self.maze.grid.copy(),
                        cmap='binary',
                        vmin=Structures.EMPTY,
                        vmax=Structures.WALL,
                        animated=True
                    )
                    ims.append([im])

        return animation.ArtistAnimation(fig, ims, interval=100, blit=True)
