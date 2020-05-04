import maze
import generate_maze


def solve_dfs(m):
    stack = []
    current = 0
    visited = 1

    while current != m.total_cells -1:
        print(current)
        unvisited = m.cell_neighbors(current)
