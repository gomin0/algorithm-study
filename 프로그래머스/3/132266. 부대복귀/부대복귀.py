from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    answer = []
    
    def dijkstra(n, graph, start):
        distance = [float('inf') for _ in range(n+1)]
        distance[start] = 0
        queue = deque([(start, 0)])
        
        while queue:
            node, d = queue.popleft()
            if d > distance[node]:
                continue
            for next_node in graph[node]:
                if distance[next_node] > d + 1:
                    distance[next_node] = d + 1
                    queue.append((next_node, d+1))
        return distance
    
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = dijkstra(n, graph, destination)
    for source in sources:
        answer.append(distance[source] if distance[source] != float('inf') else -1)
    
    return answer