class Solution(object):
    """
    Not recommeded for the following reasons:
    - it can be solved by BFS, but it's not a traditional BFS question
    - the code cannot be simplified further and the solution still looks messy
    """
    def shortestDistance(self, maze, start, destination):
        def hitWall(row, col):
            if row < 0 or row > len(maze) - 1 or col < 0 or col > len(maze[0]) - 1 \
                    or maze[row][col] == 1:
                return True
            return False

        row, col = len(maze), len(maze[0])

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        distance = [[float('inf') for _ in range(col)] for _ in range(row)]

        distance[start[0]][start[1]] = 0
        queue = [start]

        while len(queue):
            p = queue.pop(0)

            for dir in dirs:
                c_row, c_col = p[0], p[1]
                num_step = 0

                while not hitWall(c_row + dir[0], c_col + dir[1]):
                    c_row += dir[0]
                    c_col += dir[1]
                    num_step += 1

                if distance[p[0]][p[1]] + num_step < distance[c_row][c_col]:
                    distance[c_row][c_col] = distance[p[0]][p[1]] + num_step
                    queue.append([c_row, c_col])

        if distance[destination[0]][destination[1]] < float('inf'):
            return distance[destination[0]][destination[1]]
        else:
            return -1
