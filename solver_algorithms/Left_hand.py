from settings import Structures

from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation


class LeftHandRuleSolver:
    """
    keep a wall at the left at all time
    """
    def __init__(self, maze):
        self.maze = maze
        self.maze.grid[self.maze.grid == Structures.EMPTY] = Structures.SELECTED

    def solve(self, start, end, animate=False, animation_filename=""):
        path = self.solve_helper(start, end)
        if not animate:
            return path
        print("generating animation")
        fig, ax = plt.subplots(figsize=(self.maze.width / 2, self.maze.height / 2))
        ax.set_xticks([]), ax.set_yticks([])

        ims = []
        im = ax.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL)

        for i in range(1, len(path)+1):
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
            ims.append([im, path_graph, green_dot])

        print("saving animation")
        ani = ArtistAnimation(fig, ims, interval=100, blit=True)
        ani.save(animation_filename, writer='ffmpeg')
        return path

    def solve_helper(self, start, end):
        """
        Solve the maze using the right-hand rule.
        :param start: Tuple[int, int], the starting point of the maze.
        :param end: Tuple[int, int], the ending point of the maze.
        :return: List[Tuple[int, int]], the path from start to end.
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        direction = 0  # Start by facing right
        x, y = start
        path = [(2*x+1, 2*y+1)]

        while (x, y) != end:
            dir_incr = -2
            appended = False
            while not appended:
                dir_incr += 1
                choosen_dir = (direction + dir_incr) % 4
                if self.maze.grid[2*x+1 + directions[choosen_dir][0], 2*y+1 + directions[choosen_dir][1]] != Structures.WALL:
                    nx = 2 * x + 1 + 2 * directions[choosen_dir][0]
                    ny = 2 * y + 1 + 2 * directions[choosen_dir][1]
                    x = x + directions[choosen_dir][0]
                    y = y + directions[choosen_dir][1]
                    direction = choosen_dir
                    path.append((nx, ny))
                    appended = True
        return path
