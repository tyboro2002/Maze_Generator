from Maze import Maze
from generation_algoritms.DFS import DFSMazeGenerator

size = 50
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
