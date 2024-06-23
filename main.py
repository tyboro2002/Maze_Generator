from Maze import Maze
from generation_algoritms.DFS import DFSMazeGenerator

if __name__ == '__main__':
    maze = Maze(20, 20)
    generator = DFSMazeGenerator(maze)
    generator.generate()
    maze.display()
    print("generating animation")
    ani = generator.animate()
    print("saving animation")
    ani.save('maze_animation.mp4', writer='ffmpeg')
