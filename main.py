from Maze import Maze
from generation_algoritms.DFS import DFSMazeGenerator
from generation_algoritms.Prims import PrimsMazeGenerator

size = 100
sizeWidth = size
sizeHeight = size

if __name__ == '__main__':
    maze = Maze(sizeWidth, sizeHeight)
    DFSMazeGenerator(
        maze,
        optimize_no_unvisited=True
    ).run(
        maze_filename="mazes/DFS_maze.png",
        animate=False,
        animation_filename='animations/DFS_maze_animation.mp4'
    )

    PrimsMazeGenerator(
        maze
    ).run(
        maze_filename="mazes/Prims_maze.png",
        animate=True,
        animation_filename='animations/Prims_maze_animation.mp4'
    )
