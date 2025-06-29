from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    graph: defaultdict[int, list[int]] = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    dist: list[int] = [-1] * (n + 1)
    dist[destination] = 0
    queue: deque[int] = deque([destination])
    
    while queue:
        node: int = queue.popleft()
        for next_node in graph[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node] + 1
                queue.append(next_node)
    answer: list[int] = []
    for source in sources:
        answer.append(dist[source])
    return answer