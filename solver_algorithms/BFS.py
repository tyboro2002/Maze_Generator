from collections import deque

from Maze import Solver
from settings import Structures
import matplotlib.pyplot as plt


class BFSSolver(Solver):
    """
    Start at the root.
    Shift the first (i.e. least recently added) element out of the queue.
    Check for a match. If found, return the target node.
    Add each of the current node's children to the stack.
    Repeat until a match is found, or the stack is empty.
    """
    def __init__(self, maze):
        super().__init__(maze)
        self.maze.grid[self.maze.grid == Structures.SELECTED] = Structures.EMPTY

    def solve_step(self, start, end, animate):
        self._bfs(start, end, animate=animate)

    def _bfs(self, start, end, animate=False):
        """
        The BFS function.
        :param start: Tuple[int, int], the starting position in the maze.
        :param end: Tuple[int, int], the ending position in the maze.
        :param animate: bool, whether to animate the solving process.
        """
        queue = deque([start])
        parent = {start: None}
        self.visited[start[0], start[1]] = True
        self.maze.grid[2 * start[0] + 1, 2 * start[1] + 1] = Structures.SELECTED

        while queue:
            x, y = queue.popleft()
            cell_x, cell_y = 2 * x + 1, 2 * y + 1

            if (x, y) == end:
                self._construct_path(parent, end)
                return True

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height and not self.visited[nx, ny] and self.maze.grid[2*nx+1-dx, 2*ny+1-dy] != Structures.WALL:
                    queue.append((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    self.visited[nx, ny] = True
                    self.maze.grid[2 * nx + 1, 2 * ny + 1] = Structures.SELECTED
                    self.maze.grid[cell_x + dx, cell_y + dy] = Structures.SELECTED

                    if animate:
                        im = plt.imshow(self.maze.grid.copy(), cmap='binary', vmin=Structures.EMPTY, vmax=Structures.WALL, animated=True)
                        self.ims.append([im])

        return False

    def _construct_path(self, parent, end):
        """
        Construct the path from start to end using the parent dictionary.
        :param parent: Dict[Tuple[int, int], Tuple[int, int]], the parent dictionary.
        :param end: Tuple[int, int], the ending position in the maze.
        """
        current = end
        while current is not None:
            self.path.append((2 * current[0] + 1, 2 * current[1] + 1))
            current = parent[current]
        self.path.reverse()
