from Maze import Solver
from settings import Structures


class LeftHandRuleSolver(Solver):
    """
    keep a wall at the left at all time
    """
    def __init__(self, maze):
        super().__init__(maze, reverse_path=False)
        self.maze.grid[self.maze.grid == Structures.EMPTY] = Structures.SELECTED

    def solve_step(self, start, end, animate):
        self.path = self.solve_helper(start, end)

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
