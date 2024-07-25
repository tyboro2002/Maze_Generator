from Maze import Maze
from generation_algoritms.Aldous_broder import AldousBroderMazeGenerator
from generation_algoritms.DFS import DFSMazeGenerator
from generation_algoritms.Ellers import EllersMazeGenerator
from generation_algoritms.Fractal_tessellation import FractalTessellationMazeGenerator
from generation_algoritms.Prims import PrimsMazeGenerator
from generation_algoritms.Randomized_kruskal_set import RandomizedKruskalSetMazeGenerator
from generation_algoritms.Recursive_division import RecursiveDivisionMazeGenerator
from generation_algoritms.Side_winder import SidewinderMazeGenerator
from generation_algoritms.Wilson import WilsonMazeGenerator
from settings import sizeWidth, sizeHeight, animations_dir, animate, mazes_dir, mazes_filetype, animations_filetype, \
    add_maze_size_to_name, sizeWidthFractal, sizeHeightFractal, animate_solutions, fractal_tessellation, \
    solve_fractal_tessellation, aldous_broder, solve_aldous_broder, dfs, solve_dfs, prims, solve_prims, \
    randomized_kruskal, solve_randomized_kruskal, wilson, solve_wilson, recursive_division, solve_recursive_division, \
    side_winder, solve_side_winder, solve_eller, eller
from solvingMain import solveMaze

# if you get an error that a path is not found make a directory
# TODO make a function to do this

# TODO Hunt and Kill:
# Starts from a random cell, performs a random walk (like DFS), and marks cells as visited.
# If it reaches a dead end, it hunts for the next unvisited cell adjacent to a visited cell and continues from there.
# This can create mazes with a mix of long corridors and shorter dead ends.
# steps:
# Start at a random cell and perform a random walk until reaching a dead end.
# Hunt for an unvisited cell adjacent to a visited cell and continue the walk.
# Repeat until all cells are visited.

# TODO Binary Tree:
# Simple and fast.
# For each cell, it randomly removes either the north or west wall (or a specific set of directions).
# This algorithm is less effective for creating complex mazes but is very efficient.

# TODO Growing Tree Algorithm:
# A generalization of both Prim’s and Recursive Backtracker.
# Maintains a list of cells, starting with a single random cell.
# It selects a cell from the list (using different strategies), marks an adjacent unvisited cell, removes the wall
# between them, and adds the new cell to the list.
# Strategies include always choosing the most recently added cell (DFS-like), a random cell (Prim-like), or a
# combination of strategies.

# TODO Sigma Algorithm
# Description: This is a variant of the Prim's algorithm.
# Steps:
# Start with a grid full of walls.
# Randomly select a cell, mark it as part of the maze, and add its neighbors to a set.
# While there are cells in the set, randomly select a cell from the set, remove a wall between it and an adjacent cell
# that's already part of the maze, and add its neighbors to the set.
# Repeat until all cells are part of the maze.

# TODO Spiral Backtracker
# Description: This algorithm generates mazes with a spiral pattern.
# Steps:
# Start at a central cell and carve out a spiral path outward.
# Use a backtracking method to fill in dead ends and create additional paths.

# TODO Unicursal Maze
# Description: This algorithm creates mazes with a single continuous path.
# Steps:
# Create a simple closed curve (e.g., a serpentine path).
# Use a variation of the wall-following algorithm to carve out the path.
# Ensure the maze has no branches or dead ends.

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
