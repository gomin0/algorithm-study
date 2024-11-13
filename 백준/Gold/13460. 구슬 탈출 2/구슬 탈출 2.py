from collections import deque


direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def move(graph, dx, dy, x, y):
    move_count = 0
    while graph[x+dx][y+dy] != "#" and graph[x][y] != 'O':
        x += dx
        y += dy
        move_count += 1

    return x, y, move_count


def bfs(graph, red, blue):
    queue = deque([(red[0], red[1], blue[0], blue[1], 0)])
    visited = set([(red[0], red[1], blue[0], blue[1])])

    while queue:
        rx, ry, bx, by, count = queue.popleft()

        if count >= 10:
            return -1

        for i in range(4):
            nrx, nry, r_move = move(graph, direction[i][0], direction[i][1], rx, ry)
            nbx, nby, b_move = move(graph, direction[i][0], direction[i][1], bx, by)

            if graph[nbx][nby] == 'O':
                continue
            if graph[nrx][nry] == 'O':
                return count + 1

            if (nrx, nry) == (nbx, nby):
                if r_move > b_move:
                    nrx -= direction[i][0]
                    nry -= direction[i][1]
                else:
                    nbx -= direction[i][0]
                    nby -= direction[i][1]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, count + 1))

    return -1


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(input()))


for i in range(n):
    for j in range(m):
        point = graph[i][j]
        if point == 'B':
            blue = (i, j)
            graph[i][j] = '.'
        elif point == 'R':
            red = (i, j)
            graph[i][j] = '.'

print(bfs(graph, red, blue))