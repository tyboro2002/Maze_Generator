from settings import solutions_animation_dir, add_maze_size_to_name, solutions_animation_filetype, solutions_dir, \
    solutions_filetype, random_mouse_solver, right_hand_rule_solver, left_hand_rule_solver, a_star_solver_manhattan, \
    a_star_solver_euclidean, dfs_solver, bfs_solver, dijkstra_solver, dead_end_filling_solver
from solver_algorithms.A_star import AStarSolver
from solver_algorithms.BFS import BFSSolver
from solver_algorithms.DFS import DFSSolver
from solver_algorithms.Dead_end_filling import DeadEndFiller
from solver_algorithms.Dijkstra import DijkstraSolver
from solver_algorithms.Left_hand import LeftHandRuleSolver
from solver_algorithms.Random_mouse import RandomMouseSolver
from solver_algorithms.Right_hand import RightHandRuleSolver
import os


def solveMaze(maze, name, animate=False):
    # print(f"working in {solutions_animation_dir + name}")
    os.makedirs(solutions_animation_dir + name, exist_ok=True)
    if random_mouse_solver:
        print(f"{name} maze solve with Random mouse start")
        maze.save_path(
            RandomMouseSolver(
                maze
            ).solve(
                (0, 0),
                (maze.width - 1, maze.height - 1),
                animate=animate,
                animation_filename=solutions_animation_dir + name + "/Random_Mouse" +
                (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_animation_filetype
            )
            , solutions_dir + name + "/Random_Mouse" +
            (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_filetype
        )
        print(f"{name} maze solve with Random mouse done")

    if right_hand_rule_solver:
        print(f"{name} maze solve with right hand rule start")
        maze.save_path(
            RightHandRuleSolver(
                maze
            ).solve(
                (0, 0),
                (maze.width - 1, maze.height - 1),
                animate=animate,
                animation_filename=solutions_animation_dir + name + "/Right_Hand_rule" +
                (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_animation_filetype
            )
            , solutions_dir + name + "/Right_Hand_rule" +
            (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_filetype
        )
        print(f"{name} maze solve with right hand rule done")

    if left_hand_rule_solver:
        print(f"{name} maze solve with left hand rule start")
        maze.save_path(
            LeftHandRuleSolver(
                maze
            ).solve(
                (0, 0),
                (maze.width - 1, maze.height - 1),
                animate=animate,
                animation_filename=solutions_animation_dir + name + "/Left_Hand_rule" +
                (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_animation_filetype
            )
            , solutions_dir + name + "/Left_Hand_rule" +
            (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_filetype
        )
        print(f"{name} maze solve with left hand rule done")

    if dfs_solver:
        print(f"{name} maze solve with DFS start")
        maze.save_path(
            DFSSolver(
                maze
            ).solve(
                (0, 0),
                (maze.width - 1, maze.height - 1),
                animate=animate,
                animation_filename=solutions_animation_dir + name + "/DFS" +
                (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_animation_filetype
            )
            , solutions_dir + name + "/DFS" +
            (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_filetype
        )
        print(f"{name} maze solve with DFS done")

    if bfs_solver:
        print(f"{name} maze solve with BFS start")
        maze.save_path(
            BFSSolver(
                maze
            ).solve(
                (0, 0),
                (maze.width - 1, maze.height - 1),
                animate=animate,
                animation_filename=solutions_animation_dir + name + "/BFS" +
                (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_animation_filetype
            )
            , solutions_dir + name + "/BFS" +
            (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_filetype
        )
        print(f"{name} maze solve with BFS done")

    if dijkstra_solver:
        print(f"{name} maze solve with Dijkstra start")
        maze.save_path(
            DijkstraSolver(
                maze
            ).solve(
                (0, 0),
                (maze.width - 1, maze.height - 1),
                animate=animate,
                animation_filename=solutions_animation_dir + name + "/Dijkstra" +
                (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_animation_filetype
            )
            , solutions_dir + name + "/Dijkstra" +
            (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_filetype
        )
        print(f"{name} maze solve with Dijkstra done")

    if a_star_solver_manhattan:
        print(f"{name} maze solve with A* (manhattan) start")
        maze.save_path(
            AStarSolver(
                maze,
                manhattan=True
            ).solve(
                (0, 0),
                (maze.width - 1, maze.height - 1),
                animate=animate,
                animation_filename=solutions_animation_dir + name + "/A_Star_manhattan" +
                (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_animation_filetype
            )
            , solutions_dir + name + "/A_Star_manhattan" +
            (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_filetype
        )
        print(f"{name} maze solve with A* (manhattan) done")

    if a_star_solver_euclidean:
        print(f"{name} maze solve with A* (Euclidean) start")
        maze.save_path(
            AStarSolver(
                maze,
                manhattan=False
            ).solve(
                (0, 0),
                (maze.width - 1, maze.height - 1),
                animate=animate,
                animation_filename=solutions_animation_dir + name + "/A_Star_Euclidean" +
                (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_animation_filetype
            )
            , solutions_dir + name + "/A_Star_Euclidean" +
            (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_filetype
        )
        print(f"{name} maze solve with A* (Euclidean) done")

    if dead_end_filling_solver:
        print(f"{name} maze solve with dead end filling start")
        maze.save_path(
            DeadEndFiller(
                maze
            ).solve(
                (0, 0),
                (maze.width - 1, maze.height - 1),
                animate=animate,
                animation_filename=solutions_animation_dir + name + "/DeadEndFiller" +
                (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_animation_filetype
            )
            , solutions_dir + name + "/DeadEndFiller" +
            (f"_{maze.width}x{maze.height}" if add_maze_size_to_name else "") + solutions_filetype
        )
        print(f"{name} maze solve with dead end filling done")
