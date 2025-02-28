# Problem 10: Maze Solver (Hard)
# Write a program to find a path through a maze represented as a 2D list.
# In the maze, walls are marked as 1 and open paths as 0.
# Given a starting coordinate and an ending coordinate, implement an algorithm (e.g., BFS or DFS)
# to find a valid path from start to finish if one exists.
# Example:
#   Input: 2D list maze, start = (0, 0), end = (n-1, m-1)
#   Output: A list of coordinates forming the path from start to finish

from collections import deque

def solve_maze(maze, start, end):
    # TODO: Use BFS (or DFS) to find the path from start to end
    # Return a list of coordinates representing the path, or an empty list if no path exists
    pass

# Example maze: 0s are open paths, 1s are walls
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

# Test
path = solve_maze(maze, (0, 0), (4, 4))
print(path)  # Expected output: A valid path from (0,0) to (4,4) if one exists
