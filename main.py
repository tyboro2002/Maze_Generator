from Maze import Maze
from generation_algoritms.Aldous_broder import AldousBroderMazeGenerator
from generation_algoritms.DFS import DFSMazeGenerator
from generation_algoritms.Ellers import EllersMazeGenerator
from generation_algoritms.Fractal_tessellation import FractalTessellationMazeGenerator
from generation_algoritms.Hunt_and_kill import HuntAndKillMazeGenerator
from generation_algoritms.Prims import PrimsMazeGenerator
from generation_algoritms.Randomized_kruskal_set import RandomizedKruskalSetMazeGenerator
from generation_algoritms.Recursive_division import RecursiveDivisionMazeGenerator
from generation_algoritms.Side_winder import SidewinderMazeGenerator
from generation_algoritms.Sigma import SigmaMazeGenerator
from generation_algoritms.Spiral_backtracker import SpiralBacktrackerMazeGenerator
from generation_algoritms.Unicursal import UnicursalMazeGenerator
from generation_algoritms.Wilson import WilsonMazeGenerator
from settings import sizeWidth, sizeHeight, animations_dir, animate, mazes_dir, mazes_filetype, animations_filetype, \
    add_maze_size_to_name, sizeWidthFractal, sizeHeightFractal, animate_solutions, fractal_tessellation, \
    solve_fractal_tessellation, aldous_broder, solve_aldous_broder, dfs, solve_dfs, prims, solve_prims, \
    randomized_kruskal, solve_randomized_kruskal, wilson, solve_wilson, recursive_division, solve_recursive_division, \
    side_winder, solve_side_winder, solve_eller, eller, hunt_and_kill, solve_hunt_and_kill, spiral_backtracker, \
    solve_spiral_backtracker, sigma, solve_sigma, solve_unicursal, unicursal
from solvingMain import solveMaze

# if you get an error that a path is not found make a directory
# TODO make a function to do this


# TODO Binary Tree:
# Simple and fast.
# For each cell, it randomly removes either the north or west wall (or a specific set of directions).
# This algorithm is less effective for creating complex mazes but is very efficient.

# TODO Amoeba Maze
# Description: This algorithm uses cellular automata to generate organic-looking mazes.
# Steps:
# Initialize the grid with a random distribution of walls and passages.
# Apply cellular automaton rules to evolve the grid, ensuring connectivity and complexity.


if __name__ == '__main__':
    maze = Maze(sizeWidth, sizeHeight)
    fractal_maze = Maze(sizeWidthFractal, sizeHeightFractal)

    if fractal_tessellation:
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
        if solve_fractal_tessellation:
            solveMaze(fractal_maze, "Fractal_Tessellation", animate=animate_solutions)

    if aldous_broder:
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
        if solve_aldous_broder:
            solveMaze(maze, "Aldous_Broder", animate=animate_solutions)

    if dfs:
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
        if solve_dfs:
            solveMaze(maze, "DFS", animate=animate_solutions)

    if prims:
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
        if solve_prims:
            solveMaze(maze, "Prims", animate=animate_solutions)

    if randomized_kruskal:
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
        if solve_randomized_kruskal:
            solveMaze(maze, "Randomized_Kruskal", animate=animate_solutions)

    if wilson:
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
        if solve_wilson:
            solveMaze(maze, "Wilson", animate=animate_solutions)

    if recursive_division:
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
        if solve_recursive_division:
            solveMaze(maze, "Recursive_Division", animate=animate_solutions)

    if side_winder:
        print("Side Winder start")
        SidewinderMazeGenerator(
            maze
        ).run(
            maze_filename=mazes_dir + "Side_Winder_maze" +
            (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
            animate=animate,
            animation_filename=animations_dir + 'Side_Winder_maze_animation' +
            (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
        )
        print("Side Winder done")
        if solve_side_winder:
            solveMaze(maze, "Side_Winder", animate=animate_solutions)

    if eller:
        print("Eller start")
        EllersMazeGenerator(
            maze
        ).run(
            maze_filename=mazes_dir + "Eller_maze" +
            (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
            animate=animate,
            animation_filename=animations_dir + 'Eller_maze_animation' +
            (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
        )
        print("Eller done")
        if solve_eller:
            solveMaze(maze, "Eller", animate=animate_solutions)

    if hunt_and_kill:
        print("Hunt And Kill start")
        HuntAndKillMazeGenerator(
            maze
        ).run(
            maze_filename=mazes_dir + "Hunt_And_Kill_maze" +
            (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
            animate=animate,
            animation_filename=animations_dir + 'Hunt_And_Kill_maze_animation' +
            (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
        )
        print("Hunt And Kill done")
        if solve_hunt_and_kill:
            solveMaze(maze, "Hunt_And_Kill", animate=animate_solutions)

    if spiral_backtracker:
        print("Spiral Backtracker start")
        SpiralBacktrackerMazeGenerator(
            maze
        ).run(
            maze_filename=mazes_dir + "Spiral_Backtracker_maze" +
            (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
            animate=animate,
            animation_filename=animations_dir + 'Spiral_Backtracker_maze_animation' +
            (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
        )
        print("Spiral Backtracker done")
        if solve_spiral_backtracker:
            solveMaze(maze, "Spiral_Backtracker", animate=animate_solutions)

    if sigma:
        print("Sigma start")
        SigmaMazeGenerator(
            maze
        ).run(
            maze_filename=mazes_dir + "Sigma_maze" +
            (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
            animate=animate,
            animation_filename=animations_dir + 'Sigma_maze_animation' +
            (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
        )
        print("Sigma done")
        if solve_sigma:
            solveMaze(maze, "Sigma", animate=animate_solutions)

    if unicursal:
        print("Unicursal start")
        UnicursalMazeGenerator(
            maze
        ).run(
            maze_filename=mazes_dir + "Unicursal_maze" +
            (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
            animate=animate,
            animation_filename=animations_dir + 'Unicursal_maze_animation' +
            (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
        )
        print("Unicursal done")
        if solve_unicursal:
            solveMaze(maze, "Sigma", animate=animate_solutions)
