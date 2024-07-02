size = 10
sizeWidth = size
sizeHeight = size
sizeFractal = 16
sizeWidthFractal = sizeFractal
sizeHeightFractal = sizeFractal
animate = True  # Should we generate animations of the maze generation
add_maze_size_to_name = False
mazes_dir = "mazes/"  # The base path where all mazes will be stored
animations_dir = "animations/"  # The base path where all animations of the maze generation will be stored
mazes_filetype = ".png"
animations_filetype = ".mp4"



class Structures:
    WALL = 2
    SELECTED = 1
    EMPTY = 0
