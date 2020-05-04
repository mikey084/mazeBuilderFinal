import maze
import random


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    stack = []
    current = random.randint(0, m.total_cells -1)
    visited = 1

    while visited < m.total_cells:
        unvisited = m.cell_neighbors(current)
        if len(unvisited) >= 1:
            newCellIdx = random.randint(0, len(unvisited))
            newCell , compassIdx = unvisited[newCellIdx]
            m.connect_cells(current, newCell, compassIdx)
            stack.append(current)
            current = newCell
            visited = visited +1
        else:
            current = stack.pop()
        m.refresh_maze_view()
    m.state = "solve"





def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()