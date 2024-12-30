import heapq
from collections import defaultdict

def dijkstra(graph, start, n):
    distance = {i: float('inf') for i in range(1, n+1)}
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for next_dist, next_node in graph[node]:
            if distance[next_node] > next_dist + dist:
                distance[next_node] = next_dist + dist
                heapq.heappush(queue, (next_dist + dist, next_node))
    return distance

def solution(n, s, a, b, fares):
    answer = float('inf')
    
    graph = defaultdict(list)
    for start, end, dist in fares:
        graph[start].append((dist, end))
        graph[end].append((dist, start))
    
    distance1 = dijkstra(graph, s, n)
    distance2 = dijkstra(graph, a, n)
    distance3 = dijkstra(graph, b, n)
    
    for i in range(1, n+1):
        answer = min(answer, distance1[i] + distance2[i] + distance3[i])
    
    return answer