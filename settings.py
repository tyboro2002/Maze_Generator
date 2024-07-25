size = 10
sizeWidth = size
sizeHeight = size
sizeFractal = 16  # this must be a power of 2
sizeWidthFractal = sizeFractal
sizeHeightFractal = sizeFractal
animate = True  # Should we generate animations of the maze generation
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


# what mazes need to be generated
run_generator = False
fractal_tessellation = run_generator
aldous_broder = run_generator
dfs = run_generator
prims = run_generator
randomized_kruskal = run_generator
wilson = run_generator
recursive_division = run_generator
side_winder = run_generator
eller = True

# what mazes need to be solved (if not generated they will also not be solved)
run_solve = True
solve_fractal_tessellation = run_solve
solve_aldous_broder = run_solve
solve_dfs = run_solve
solve_prims = run_solve
solve_randomized_kruskal = run_solve
solve_wilson = run_solve
solve_recursive_division = run_solve
solve_side_winder = run_solve
solve_eller = True

# what solvers need to be used
run_solver = True
random_mouse_solver = True
right_hand_rule_solver = run_solver
left_hand_rule_solver = run_solver
dfs_solver = run_solver
bfs_solver = run_solver
dijkstra_solver = run_solver
a_star_solver_manhattan = run_solver
a_star_solver_euclidean = run_solver
dead_end_filling_solver = run_solver


class Structures:
    WALL = 4
    SELECTED = 2
    EMPTY = 0
