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
from solver_algorithms.Left_hand import LeftHandRuleSolver
from solver_algorithms.Right_hand import RightHandRuleSolver

def solveMaze(maze, name, animate=False):
    print(f"{name} maze solve with right hand rule start")
    maze.save_path(
        RightHandRuleSolver(
            maze
        ).solve(
            (0, 0),
            (maze.width - 1, maze.height - 1),
            animate=animate,
            animation_filename=solutions_animation_dir + name + "_Right_Hand_rule" +
            (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_animation_filetype
        )
        , solutions_dir + name + "_Right_Hand_rule" +
        (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_filetype
    )
    print(f"{name} maze solve with right hand rule done")

    print(f"{name} maze solve with left hand rule start")
    maze.save_path(
        LeftHandRuleSolver(
            maze
        ).solve(
            (0, 0),
            (maze.width - 1, maze.height - 1),
            animate=animate,
            animation_filename=solutions_animation_dir + name + "_Left_Hand_rule" +
            (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_animation_filetype
        )
        , solutions_dir + name + "Left_Hand_rule" +
        (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + solutions_filetype
    )
    print(f"{name} maze solve with left hand rule done")


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

    # print("aldous broder start")
    # AldousBroderMazeGenerator(
    #     maze
    # ).run(
    #     maze_filename=mazes_dir + "Aldous_Broder_maze" +
    #     (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
    #     animate=animate,
    #     animation_filename=animations_dir + 'Aldous_Broder_maze_animation' +
    #     (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    # )
    # print("aldous broder done")
    #
    # print("DFS start")
    # DFSMazeGenerator(
    #     maze,
    #     optimize_no_unvisited=True
    # ).run(
    #     maze_filename=mazes_dir + "DFS_maze" +
    #     (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
    #     animate=animate,
    #     animation_filename=animations_dir + 'DFS_maze_animation' +
    #     (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    # )
    # print("DFS done")
    #
    # print("prims start")
    # PrimsMazeGenerator(
    #     maze
    # ).run(
    #     maze_filename=mazes_dir + "Prims_maze" +
    #     (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
    #     animate=animate,
    #     animation_filename=animations_dir + 'Prims_maze_animation' +
    #     (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    # )
    # print("prims done")
    #
    # print("randomized kruskal set start")
    # RandomizedKruskalSetMazeGenerator(
    #     maze
    # ).run(
    #     maze_filename=mazes_dir + "Randomized_Kruskal_Set_maze" +
    #     (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
    #     animate=animate,
    #     animation_filename=animations_dir + 'Randomized_Kruskal_Set_maze_animation' +
    #     (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    # )
    # print("randomized kruskal set done")
    #
    # print("wilson start")
    # WilsonMazeGenerator(
    #     maze
    # ).run(
    #     maze_filename=mazes_dir + "Wilson_maze" +
    #     (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
    #     animate=animate,
    #     animation_filename=animations_dir + 'Wilson_maze_animation' +
    #     (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    # )
    # print("wilson done")
    #
    # print("Recursive Division start")
    # RecursiveDivisionMazeGenerator(
    #     maze
    # ).run(
    #     maze_filename=mazes_dir + "Recursive_Division_maze" +
    #     (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
    #     animate=animate,
    #     animation_filename=animations_dir + 'Recursive_Division_maze_animation' +
    #     (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    # )
    # print("Recursive Division done")
