size = 1024
sizeWidth = size
sizeHeight = size
animate = True  # Should we generate animations of the maze generation
mazes_dir = "mazes/"  # The base path where all mazes will be stored
animations_dir = "animations/"  # The base path where all animations of the maze generation will be stored


class Structures:
    WALL = 2
    SELECTED = 1
    EMPTY = 0
