from collections import deque

def solution(n, edge):
    graph: list[list[int]] = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    distance: list[int] = [0] * (n+1)
    visited: set[int] = set()
    queue: deque[int] = deque([1])
    visited.add(1)
    
    while queue:
        node: int = queue.popleft()
        for next_node in graph[node]:
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)
                distance[next_node] = distance[node] + 1
    
    return distance.count(max(distance))