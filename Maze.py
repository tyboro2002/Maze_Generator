import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

from settings import Structures


class Maze:
    """
    The Maze class is a class to hold the maze we generated.
    """

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        # Create a grid with walls (2) and cells (0)
        self.grid = np.zeros((2 * height + 1, 2 * width + 1), dtype=np.int8)
        self.grid[1::2, 1::2] = Structures.EMPTY  # Paths
        self.grid[0::2, :] = Structures.WALL  # Horizontal walls
        self.grid[:, 0::2] = Structures.WALL  # Vertical walls

    def reset(self) -> None:
        """
        Reset the maze to its initial state.
        """
        self.grid.fill(Structures.WALL)
        self.grid[1::2, 1::2] = Structures.EMPTY

    def display(self) -> None:
        """
        Display the maze on the screen.
        """
        plt.imshow(self.grid, cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL)
        plt.xticks([]), plt.yticks([])
        plt.show()

    def display_path(self, path):
        """
        Display the maze with the path overlayed.
        :param path: List[Tuple[int, int]], the path to display on the maze.
        """
        fig, ax = plt.subplots(figsize=(max(self.width / 5, 10), max(self.height / 5, 10)))
        ax.set_xticks([]), ax.set_yticks([])

        # Plot the maze
        ax.imshow(self.grid, cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL)

        base_size = 10
        marker_size = base_size * min(1, base_size / max(self.width, self.height))

        linewidth = base_size * min(1, base_size / max(self.width, self.height)) * 0.5

        # Plot the path
        path_y, path_x = zip(*path)
        ax.plot(path_x, path_y, marker='o', color='red', markersize=marker_size, linewidth=linewidth)

        plt.show()

    def save_path(self, path, filename: str):
        """
        Display the maze with the path overlayed.
        :param path: List[Tuple[int, int]], the path to display on the maze.
        :param filename: str, the path to save the image
        """
        fig, ax = plt.subplots(figsize=(max(self.width / 5, 10), max(self.height / 5, 10)))
        ax.set_xticks([]), ax.set_yticks([])

        # Plot the maze
        ax.imshow(self.grid, cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL)

        base_size = 15
        marker_size = base_size * min(1, base_size / max(self.width, self.height))

        linewidth = base_size * min(1, base_size / max(self.width, self.height)) * 0.5

        # Plot the path
        path_y, path_x = zip(*path)
        ax.plot(path_x, path_y, marker='o', color='red', markersize=marker_size, linewidth=linewidth)

        plt.savefig(filename, bbox_inches='tight')
        plt.close()

    def save(self, filename: str) -> None:
        """
        Save the maze to a file with the given filename.
        :param filename: The name of the file to save.
        """
        # Adjust figure size based on maze dimensions
        fig, ax = plt.subplots(figsize=(max(self.width / 5, 10), max(self.height / 5, 10)))
        ax.set_xticks([]), ax.set_yticks([])
        ax.imshow(self.grid, cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL)
        plt.savefig(filename, bbox_inches='tight')
        plt.close()


class MazeGenerator:
    """
    A super class to bundle the maze generator classes.
    """

    def __init__(self, maze: Maze) -> None:
        self.maze = maze

    def generate(self):
        raise NotImplementedError("You should implement this method in subclasses.")

    def animate(self):
        raise NotImplementedError("You should implement this method in subclasses.")

    def run(
            self,
            maze_filename: str,
            animate: bool = True,
            animation_filename: str = "maze_animation.mp4"
    ) -> None:
        """
        Do a full maze generation run (possibly save the animation of the generation).
        """
        if not animate:
            self.generate()
            self.maze.save(maze_filename)
        else:
            print("generating animation")
            ani = self.animate()
            print("saving animation")
            ani.save(animation_filename, writer='ffmpeg')
            self.maze.save(maze_filename)


class Solver:
    """
    A super class to bundle the maze solver classes.
    """

    def __init__(self, maze: Maze, reverse_path=True) -> None:
        self.maze = maze
        self.ims = []
        self.path = []
        self.visited = np.zeros_like(maze.grid, dtype=bool)
        self.reverse_path = reverse_path

    # def solve(self, start, end, animate=False, animation_filename=""):
    #     raise NotImplementedError("You should implement this method in subclasses.")

    def solve(self, start, end, animate=False, animation_filename=""):
        """
        Solve the maze using Dijkstra's algorithm.
        :param start: Tuple[int, int], the starting point of the maze.
        :param end: Tuple[int, int], the ending point of the maze.
        :return: List[Tuple[int, int]], the path from start to end.
        """
        self.solve_setup()
        if not animate:
            self.solve_step(start, end, animate)
            self.maze.grid[2 * end[0] + 1, 2 * end[1] + 1] = Structures.SELECTED
            return self.path

        print("generating animation")

        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])

        self.solve_step(start, end, animate)

        self.maze.grid[2 * end[0] + 1, 2 * end[1] + 1] = Structures.SELECTED
        im = self.add_image(ax)

        if self.reverse_path:
            path = self.path[::-1]
        else:
            path = self.path

        for i in range(1, len(path) + 1):
            # Plot the path
            cur_path = path[:i]
            path_y, path_x = zip(*cur_path)
            path_graph, = ax.plot(path_x, path_y, marker='o', color='red', markersize=5, linewidth=2)

            green_dot, = ax.plot(
                cur_path[-1][1], cur_path[-1][0],
                marker='o',
                color='green',
                markersize=5,
                animated=True
            )
            self.ims.append([im, path_graph, green_dot])

        print("saving animation")
        ani = ArtistAnimation(fig, self.ims, interval=100, blit=True)
        ani.save(animation_filename, writer='ffmpeg')
        plt.close()
        return self.path

    def add_image(self, ax):
        im = plt.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL,
                        animated=True)
        self.ims.append([im])

        return ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL)

    def solve_step(self, start, end, animate):
        raise NotImplementedError("You should implement this method in subclasses.")

    # def solve_setup(self):
    #     raise NotImplementedError("You should implement this method in subclasses.")

    def solve_setup(self):
        self.visited.fill(False)
