import maze
import generate_maze
import sys
import random
import time

# Method to solve the maze using DFS
def solve_dfs(m):
    stack = []
    current = 0
    visited = 1

    while current != m.total_cells -1:
        print(current)
        unvisited = m.cell_neighbors(current)
        if len(unvisited) >= 1:
            newCellIdx = random.randint(0, len(unvisited)-1)
            newCell, compassIdx = unvisited[newCellIdx]
            m.visit_cell(current, newCell, compassIdx)
            stack.append(current)
            current = newCell
            visited += 1
        else:
            m.backtrack(current)
            current = stack.pop()
            print("run")
        m.refresh_maze_view()
    m.state = 'idle'

# Method to solve the maze using BFS
def solve_bfs(m):
    queue = []
    current = 0
    inDirection = 0b0000
    numVisited = 0
    queue.insert(0,(current, inDirection))

    while not current == len(m.maze_array) -1 and len(queue) > 0:
        current, inDirection = queue.pop()
        m.bfs_visit_cell(current, inDirection)
        numVisited += 1
        m.refresh_maze_view()
        neighbors = m.cell_neighbors(current)

        for x in neighbors:
            queue.insert(0, x)

    m.reconstruct_solution(current)
    m.state = 'idle'


def main(solver='bfs'):
    # This is to get current time for runtime below
    start_time = time.time()
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
        # Calculate runtime
        print(str((time.time() - start_time)) + " seconds")
    elif solver == 'bfs':
        solve_bfs(current_maze)
        # Calculate runtime
        print(str((time.time() - start_time)) + " seconds")
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()