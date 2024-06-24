from Maze import Maze
from generation_algoritms.DFS import DFSMazeGenerator
from generation_algoritms.Prims import PrimsMazeGenerator
from settings import sizeWidth, sizeHeight, animations_dir, animate, mazes_dir

if __name__ == '__main__':
    maze = Maze(sizeWidth, sizeHeight)
    DFSMazeGenerator(
        maze,
        optimize_no_unvisited=True
    ).run(
        maze_filename=mazes_dir + "DFS_maze.png",
        animate=animate,
        animation_filename=animations_dir + 'DFS_maze_animation.mp4'
    )

    PrimsMazeGenerator(
        maze
    ).run(
        maze_filename=mazes_dir + "Prims_maze.png",
        animate=animate,
        animation_filename=animations_dir + 'Prims_maze_animation.mp4'
    )
