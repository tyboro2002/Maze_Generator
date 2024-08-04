from Maze import Maze
from generation_algoritms.Aldous_broder import AldousBroderMazeGenerator
from generation_algoritms.Origin_shift import OriginShiftGenerator
from generation_algoritms.Binary_tree import BinaryTreeMazeGenerator
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
    solve_spiral_backtracker, sigma, solve_sigma, solve_unicursal, unicursal, binary_tree, solve_binary_tree, origin_shift, \
    solve_origin_shift
from solvingMain import solveMaze

# if you get an error that a path is not found make a directory
# TODO make a function to do this


def run_generation(generator, run_gen: bool, run_solve: bool, short_name: str, map_name: str, maze: Maze):
    if run_gen:
        print(f"{short_name} maze generation start")
        generator(
            maze
        ).run(
            maze_filename=mazes_dir + f"{map_name}_maze" +
            (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + mazes_filetype,
            animate=animate,
            animation_filename=animations_dir + f'{map_name}_maze_animation' +
            (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + animations_filetype
        )
        print(f"{short_name} maze generation done")
        if run_solve:
            solveMaze(maze, map_name, animate=animate_solutions)


if __name__ == '__main__':
    maze = Maze(sizeWidth, sizeHeight)
    fractal_maze = Maze(sizeWidthFractal, sizeHeightFractal)

    run_generation(FractalTessellationMazeGenerator, fractal_tessellation, solve_fractal_tessellation, "fractal tessellation", "Fractal_Tessellation", fractal_maze)
    run_generation(AldousBroderMazeGenerator, aldous_broder, solve_aldous_broder, "Aldous Broder", "Aldous_Broder", maze)
    run_generation(DFSMazeGenerator, dfs, solve_dfs, "DFS", "DFS", maze)
    run_generation(PrimsMazeGenerator, prims, solve_prims, "Prims", "Prims", maze)
    run_generation(RandomizedKruskalSetMazeGenerator, randomized_kruskal, solve_randomized_kruskal, "Randomized Kruskal set", "Randomized_Kruskal_Set", maze)
    run_generation(WilsonMazeGenerator, wilson, solve_wilson, "Wilson", "Wilson", maze)
    run_generation(RecursiveDivisionMazeGenerator, recursive_division, solve_recursive_division, "Recursive Division", "Recursive_Division", maze)
    run_generation(SidewinderMazeGenerator, side_winder, solve_side_winder, "Side Winder", "Side_Winder", maze)
    run_generation(EllersMazeGenerator, eller, solve_eller, "Eller", "Eller", maze)
    run_generation(HuntAndKillMazeGenerator, hunt_and_kill, solve_hunt_and_kill, "Hunt And Kill", "Hunt_And_Kill", maze)
    run_generation(SpiralBacktrackerMazeGenerator, spiral_backtracker, solve_spiral_backtracker, "Spiral Backtracker", "Spiral_Backtracker", maze)
    run_generation(SigmaMazeGenerator, sigma, solve_sigma, "Sigma", "Sigma", maze)
    run_generation(UnicursalMazeGenerator, unicursal, solve_unicursal, "Unicursal", "Unicursal", maze)
    run_generation(BinaryTreeMazeGenerator, binary_tree, solve_binary_tree, "Binary Tree", "Binary_Tree", maze)
    run_generation(OriginShiftGenerator, origin_shift, solve_origin_shift, "Origin Shift", "Origin_Shift", maze)
