from Maze import Solver
from settings import Structures

import matplotlib.pyplot as plt


class DFSSolver(Solver):
    """
    Start at the root.
    Pop the last (i.e. most recently added) element off the stack.
    Check for a match. If found, return the target node.
    Add each of the current node's children to the stack.
    Repeat until a match is found, or the stack is empty.

    The algorithm will be given a starting X and Y value. If the X and Y values are not on a wall, the method will cal
    itself with all adjacent X and Y values, making sure that it did not already use those X and Y values before. If the
    X and Y values are those of the end location, it will save all the previous instances of
    the method as the correct path.
    """
    def __init__(self, maze):
        super().__init__(maze)
        self.maze.grid[self.maze.grid == Structures.SELECTED] = Structures.EMPTY

    def solve_step(self, start, end, animate):
        self._dfs_stack(start, end, animate=True)

    def _dfs_stack(self, start, end, animate=False):
        """
        The stack-based DFS function.
        :param start: Tuple[int, int], the starting position in the maze.
        :param end: Tuple[int, int], the ending position in the maze.
        :param animate: bool, whether to animate the solving process.
        """
        stack = [(start, [(2*start[0]+1, 2*start[1]+1)])]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        while stack:
            (x, y), current_path = stack.pop()
            cell_x, cell_y = 2 * x + 1, 2 * y + 1

            if (x, y) == end:
                self.path = current_path
                return True

            self.visited[x, y] = True
            self.maze.grid[cell_x, cell_y] = Structures.SELECTED

            if animate:
                im = plt.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL,
                                animated=True)
                self.ims.append([im])

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and not self.visited[nx, ny] and self.maze.grid[2*nx+1-dx, 2*ny+1-dy] != Structures.WALL:
                    self.maze.grid[2 * x + 1 + dx, 2 * y + 1 + dy] = Structures.SELECTED
                    stack.append(((nx, ny), current_path + [(2*nx+1, 2*ny+1)]))

        return False

    def _dfs(self, current, end, animate=False):
        """
        The recursive DFS function.
        :param current: Tuple[int, int], the current position in the maze.
        :param end: Tuple[int, int], the ending point of the maze.
        :return: bool, True if the end is found, otherwise False.
        """
        x, y = current
        if current == end:
            self.path.append((2*x+1, 2*y+1))
            return True

        self.visited[x, y] = True
        self.maze.grid[2*x+1, 2*y+1] = Structures.SELECTED
        self.path.append((2*x+1, 2*y+1))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        if animate:
            im = plt.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL,
                            animated=True)
            # red_dot, = plt.plot(2 * y + 1, 2 * x + 1, marker='o', color='red', markersize=5, animated=True)
            self.ims.append([im])

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and not self.visited[nx, ny] and self.maze.grid[2*nx+1-dx, 2*ny+1-dy] != Structures.WALL:
                self.maze.grid[2 * x + 1+dx, 2 * y + 1+dy] = Structures.SELECTED
                if self._dfs((nx, ny), end, animate=animate):
                    return True

        self.path.pop()
        return False
