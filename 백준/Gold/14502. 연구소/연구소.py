import sys
from itertools import combinations
from collections import deque
import copy


def three_point(points):
    new_wall = list(combinations(points, 3))
    return new_wall


def bfs(graph, points, virus):
    for i, j in points:
        graph[i][j] = 1

    queue = deque()
    for v in virus:
        queue.append(v)

    while queue:
        x, y = queue.popleft()

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))

    count = 0
    for k in range(n):
        count += graph[k].count(0)

    return count


n, m = map(int, sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

points = []
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            points.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

answer = 0
new_wall = three_point(points)
for p in new_wall:
    new_graph = copy.deepcopy(graph)
    answer = max(answer, bfs(new_graph, p, virus))

print(answer)