from Maze import Maze
from generation_algoritms.Aldous_broder import AldousBroderMazeGenerator
from generation_algoritms.DFS import DFSMazeGenerator
from generation_algoritms.Fractal_tessellation import FractalTessellationMazeGenerator
from generation_algoritms.Prims import PrimsMazeGenerator
from generation_algoritms.Randomized_kruskal_set import RandomizedKruskalSetMazeGenerator
from generation_algoritms.Recursive_division import RecursiveDivisionMazeGenerator
from generation_algoritms.Wilson import WilsonMazeGenerator
from settings import sizeWidth, sizeHeight, animations_dir, animate, mazes_dir, mazes_filetype, animations_filetype, \
    add_maze_size_to_name, sizeWidthFractal, sizeHeightFractal, solutions_dir, solutions_filetype, \
    solutions_animation_dir, solutions_animation_filetype, animate_solutions
from solver_algorithms.BFS import BFSSolver
from solver_algorithms.DFS import DFSSolver
from solver_algorithms.Dijkstra import DijkstraSolver
from solver_algorithms.Left_hand import LeftHandRuleSolver
from solver_algorithms.Random_mouse import RandomMouseSolver
from solver_algorithms.Right_hand import RightHandRuleSolver

# if you get an error that a path is not found make a directory
# TODO make a function to do this

# TODO dead end filling
# find all of the dead-ends in the maze, and then
# "fill in" the path from each dead-end until the first junction is met.


# TODO A*
# A* keeps track of two different factors. First, how expensive it was to get to a given node from the origin.
# Second, the minimum predicted cost of getting from that node to the goal. A* predicts the cost of traveling through a
# given node based on a heuristic function we provide it, which is based on the structure of our graph.
#
# In this case, we set the heuristic function to calculate the diagonal distance between the current node and the
# target node, so that our search will be encouraged to go as directly toward the goal as possible.

# TODO dijkstra (looks like BFS here)
# min-heap priority queue
# In spanning trees like ours, Dijkstra's proceeds like BFS, with changes to step 2:
#
# Remove the minimum entry from the priority queue.
# and step 4:
#
# Insert each of the current node's children into the priority queue.


def solveMaze(maze, name, animate=False):
    # print(f"{name} maze solve with Random mouse start")
    # maze.save_path(
    #     RandomMouseSolver(
    #         maze
    #     ).solve(
    #         (0, 0),
    #         (maze.width - 1, maze.height - 1),
    #         animate=animate,
    #         animation_filename=solutions_animation_dir + name + "/Random_Mouse" +
    #         (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_animation_filetype
    #     )
    #     , solutions_dir + name + "/Random_Mouse" +
    #     (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_filetype
    # )
    # print(f"{name} maze solve with Random mouse done")

    # print(f"{name} maze solve with right hand rule start")
    # maze.save_path(
    #     RightHandRuleSolver(
    #         maze
    #     ).solve(
    #         (0, 0),
    #         (maze.width - 1, maze.height - 1),
    #         animate=animate,
    #         animation_filename=solutions_animation_dir + name + "/Right_Hand_rule" +
    #         (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_animation_filetype
    #     )
    #     , solutions_dir + name + "/Right_Hand_rule" +
    #     (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_filetype
    # )
    # print(f"{name} maze solve with right hand rule done")
    #
    # print(f"{name} maze solve with left hand rule start")
    # maze.save_path(
    #     LeftHandRuleSolver(
    #         maze
    #     ).solve(
    #         (0, 0),
    #         (maze.width - 1, maze.height - 1),
    #         animate=animate,
    #         animation_filename=solutions_animation_dir + name + "/Left_Hand_rule" +
    #         (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_animation_filetype
    #     )
    #     , solutions_dir + name + "/Left_Hand_rule" +
    #     (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_filetype
    # )
    # print(f"{name} maze solve with left hand rule done")

    # print(f"{name} maze solve with DFS start")
    # maze.save_path(
    #     DFSSolver(
    #         maze
    #     ).solve(
    #         (0, 0),
    #         (maze.width - 1, maze.height - 1),
    #         animate=animate,
    #         animation_filename=solutions_animation_dir + name + "/DFS" +
    #         (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_animation_filetype
    #     )
    #     , solutions_dir + name + "/DFS" +
    #     (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_filetype
    # )
    # print(f"{name} maze solve with DFS done")

    # print(f"{name} maze solve with BFS start")
    # maze.save_path(
    #     BFSSolver(
    #         maze
    #     ).solve(
    #         (0, 0),
    #         (maze.width - 1, maze.height - 1),
    #         animate=animate,
    #         animation_filename=solutions_animation_dir + name + "/BFS" +
    #         (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_animation_filetype
    #     )
    #     , solutions_dir + name + "/BFS" +
    #     (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_filetype
    # )
    # print(f"{name} maze solve with BFS done")

    print(f"{name} maze solve with Dijkstra start")
    maze.save_path(
        DijkstraSolver(
            maze
        ).solve(
            (0, 0),
            (maze.width - 1, maze.height - 1),
            animate=animate,
            animation_filename=solutions_animation_dir + name + "/Dijkstra" +
            (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_animation_filetype
        )
        , solutions_dir + name + "/Dijkstra" +
        (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_filetype
    )
    print(f"{name} maze solve with Dijkstra done")


if __name__ == '__main__':
    maze = Maze(sizeWidth, sizeHeight)
    fractal_maze = Maze(sizeWidthFractal, sizeHeightFractal)

    print("fractal tessellation maze generation start")
    FractalTessellationMazeGenerator(
        fractal_maze
    ).run(
        maze_filename=mazes_dir + "Fractal_Tessellation_maze" +
        (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + mazes_filetype,
        animate=animate,
        animation_filename=animations_dir + 'Fractal_Tessellation_maze_animation' +
        (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + animations_filetype
    )
    print("fractal tessellation maze generation done")
    solveMaze(fractal_maze, "Fractal_Tessellation", animate=animate_solutions)

    print("Aldous Broder start")
    AldousBroderMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Aldous_Broder_maze" +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
        animate=animate,
        animation_filename=animations_dir + 'Aldous_Broder_maze_animation' +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    )
    print("Aldous Broder done")
    solveMaze(maze, "Aldous_Broder", animate=animate_solutions)

    print("DFS start")
    DFSMazeGenerator(
        maze,
        optimize_no_unvisited=True
    ).run(
        maze_filename=mazes_dir + "DFS_maze" +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
        animate=animate,
        animation_filename=animations_dir + 'DFS_maze_animation' +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    )
    print("DFS done")
    solveMaze(maze, "DFS", animate=animate_solutions)

    print("Prims start")
    PrimsMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Prims_maze" +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
        animate=animate,
        animation_filename=animations_dir + 'Prims_maze_animation' +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    )
    print("Prims done")
    solveMaze(maze, "Prims", animate=animate_solutions)

    print("Randomized Kruskal set start")
    RandomizedKruskalSetMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Randomized_Kruskal_Set_maze" +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
        animate=animate,
        animation_filename=animations_dir + 'Randomized_Kruskal_Set_maze_animation' +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    )
    print("Randomized Kruskal set done")
    solveMaze(maze, "Randomized_Kruskal", animate=animate_solutions)

    print("Wilson start")
    WilsonMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Wilson_maze" +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
        animate=animate,
        animation_filename=animations_dir + 'Wilson_maze_animation' +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    )
    print("Wilson done")
    solveMaze(maze, "Wilson", animate=animate_solutions)

    print("Recursive Division start")
    RecursiveDivisionMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Recursive_Division_maze" +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
        animate=animate,
        animation_filename=animations_dir + 'Recursive_Division_maze_animation' +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    )
    print("Recursive Division done")
    solveMaze(maze, "Recursive_Division", animate=animate_solutions)
