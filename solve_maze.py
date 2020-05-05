import maze
import generate_maze
import sys
import random


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



'''

BFS
create queue
set cell to 0
set in direction for bits
set visited to 0
enqueue current cell

while current not end and not empty
dequeue to current cell
visit current cell with bfs
add 1 to visited
call maze refresh

outside while loop do something for solution path traceback method
set state 
'''

def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()