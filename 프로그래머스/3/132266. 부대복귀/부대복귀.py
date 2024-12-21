from collections import deque, defaultdict

def solution(n, roads, sources, destination):

    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [-1 for _ in range(n+1)]
    distance[destination] = 0
    
    queue = deque([destination])
    while queue:
        node = queue.popleft()
        dist = distance[node]
        
        for next_node in graph[node]:
            if distance[next_node] == -1:
                distance[next_node] = dist + 1
                queue.append(next_node)
    
    return [distance[source] for source in sources]