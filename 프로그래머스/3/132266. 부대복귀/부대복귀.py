from collections import defaultdict, deque


def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    dist = [-1] * (n + 1)
    dist[destination] = 0
    q = deque([destination])
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if dist[next_node] == -1:
                dist[next_node] = dist[node] + 1
                q.append(next_node)
    
    answer = []
    for source in sources:
        answer.append(dist[source])
    return answer