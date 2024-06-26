from Maze import Maze
from generation_algoritms.Aldous_broder import AldousBroderMazeGenerator
from generation_algoritms.DFS import DFSMazeGenerator
from generation_algoritms.Prims import PrimsMazeGenerator
from generation_algoritms.Randomized_kruskal_set import RandomizedKruskalSetMazeGenerator
from generation_algoritms.Wilson import WilsonMazeGenerator
from settings import sizeWidth, sizeHeight, animations_dir, animate, mazes_dir


# TODO Recursive division method
# Mazes can be created with recursive division, an algorithm which works as follows: Begin with the maze's space with
# no walls. Call this a chamber. Divide the chamber with a randomly positioned wall (or multiple walls) where each wall
# contains a randomly positioned passage opening within it. Then recursively repeat the process on the subchambers until
# all chambers are minimum sized. This method results in mazes with long straight walls crossing their space, making
# it easier to see which areas to avoid.
#
# For example, in a rectangular maze, build at random points two walls that are perpendicular to each other. These two
# walls divide the large chamber into four smaller chambers separated by four walls. Choose three of the four walls at
# random, and open a one cell-wide hole at a random point in each of the three. Continue in this manner recursively,
# until every chamber has a width of one cell in either of the two directions.

# TODO Fractal Tessellation algorithm
# On each iteration, this algorithm creates a maze twice the size by copying itself 3 times.
# At the end of each iteration, 3 paths are opened between the 4 smaller mazes.

if __name__ == '__main__':
    maze = Maze(sizeWidth, sizeHeight)

    print("aldous broder start")
    AldousBroderMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Aldous_Broder_maze.png",
        animate=animate,
        animation_filename=animations_dir + 'Aldous_Broder_maze_animation.mp4'
    )
    print("aldous broder done")

    print("DFS start")
    DFSMazeGenerator(
        maze,
        optimize_no_unvisited=True
    ).run(
        maze_filename=mazes_dir + "DFS_maze.png",
        animate=animate,
        animation_filename=animations_dir + 'DFS_maze_animation.mp4'
    )
    print("DFS done")

    print("prims start")
    PrimsMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Prims_maze.png",
        animate=animate,
        animation_filename=animations_dir + 'Prims_maze_animation.mp4'
    )
    print("prims done")

    print("randomized kruskal set start")
    RandomizedKruskalSetMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Randomized_Kruskal_Set_maze.png",
        animate=animate,
        animation_filename=animations_dir + 'Randomized_Kruskal_Set_maze_animation.mp4'
    )
    print("randomized kruskal set done")

    print("wilson start")
    WilsonMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Wilson_maze.png",
        animate=animate,
        animation_filename=animations_dir + 'Wilson_maze_animation.mp4'
    )
    print("wilson done")
