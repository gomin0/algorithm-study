from collections import deque, defaultdict


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    distance = [0] * (n + 1)
    visited = set()
    q = deque()
    q.append(1)
    visited.add(1)
    
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if next_node not in visited:
                q.append(next_node)
                visited.add(next_node)
                distance[next_node] = distance[node] + 1
    
    return distance.count(max(distance))