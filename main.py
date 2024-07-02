from Maze import Maze
from generation_algoritms.Aldous_broder import AldousBroderMazeGenerator
from generation_algoritms.DFS import DFSMazeGenerator
from generation_algoritms.Fractal_tessellation import FractalTessellationMazeGenerator
from generation_algoritms.Prims import PrimsMazeGenerator
from generation_algoritms.Randomized_kruskal_set import RandomizedKruskalSetMazeGenerator
from generation_algoritms.Recursive_division import RecursiveDivisionMazeGenerator
from generation_algoritms.Wilson import WilsonMazeGenerator
from settings import sizeWidth, sizeHeight, animations_dir, animate, mazes_dir, mazes_filetype, animations_filetype, \
    add_maze_size_to_name, sizeWidthFractal, sizeHeightFractal

if __name__ == '__main__':
    maze = Maze(sizeWidth, sizeHeight)

    print("fractal tessellation start")
    FractalTessellationMazeGenerator(
        Maze(sizeWidthFractal, sizeHeightFractal)
    ).run(
        maze_filename=mazes_dir + "Fractal_Tessellation_maze" +
        (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + mazes_filetype,
        animate=animate,
        animation_filename=animations_dir + 'Fractal_Tessellation_maze_animation' +
        (f"_{sizeWidthFractal}x{sizeHeightFractal}" if add_maze_size_to_name else "") + animations_filetype
    )
    print("fractal tessellation done")

    print("aldous broder start")
    AldousBroderMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Aldous_Broder_maze" +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
        animate=animate,
        animation_filename=animations_dir + 'Aldous_Broder_maze_animation' +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    )
    print("aldous broder done")

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

    print("prims start")
    PrimsMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Prims_maze" +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
        animate=animate,
        animation_filename=animations_dir + 'Prims_maze_animation' +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    )
    print("prims done")

    print("randomized kruskal set start")
    RandomizedKruskalSetMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Randomized_Kruskal_Set_maze" +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
        animate=animate,
        animation_filename=animations_dir + 'Randomized_Kruskal_Set_maze_animation' +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    )
    print("randomized kruskal set done")

    print("wilson start")
    WilsonMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Wilson_maze" +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + mazes_filetype,
        animate=animate,
        animation_filename=animations_dir + 'Wilson_maze_animation' +
        (f"_{sizeWidth}x{sizeHeight}" if add_maze_size_to_name else "") + animations_filetype
    )
    print("wilson done")

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
