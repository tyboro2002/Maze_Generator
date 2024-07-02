size = 10
sizeWidth = size
sizeHeight = size
sizeFractal = 16
sizeWidthFractal = sizeFractal
sizeHeightFractal = sizeFractal
animate = False  # Should we generate animations of the maze generation
animate_solutions = True  # Should we generate animations of the maze solving
add_maze_size_to_name = False
mazes_dir = "mazes/"  # The base path where all mazes will be stored
animations_dir = "animations/"  # The base path where all animations of the maze generation will be stored
solutions_dir = "solutions/"  # The base path where all solutions of the maze generation will be stored
# The base path where all solutions animation of the maze generation will be stored
solutions_animation_dir = "solutions_animations/"
mazes_filetype = ".png"
animations_filetype = ".mp4"
solutions_filetype = ".png"
solutions_animation_filetype = ".mp4"



class Structures:
    WALL = 2
    SELECTED = 1
    EMPTY = 0
