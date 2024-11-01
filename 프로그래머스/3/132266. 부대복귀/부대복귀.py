import heapq
from collections import defaultdict

def dijkstra(start, graph, n):
    distance = {i:float('inf') for i in range(1, n+1)}
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        now_distance, now_node = heapq.heappop(queue)
        if now_distance > distance[now_node]:
            continue
        for next_node in graph[now_node]:
            dist = now_distance + 1
            if dist < distance[next_node]:
                distance[next_node] = dist
                heapq.heappush(queue, (dist, next_node))
    return distance

def solution(n, roads, sources, destination):
    answer = []
    
    graph = defaultdict(list)
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    distance = dijkstra(destination, graph, n)
    
    for source in sources:
        dist = distance[source]
        if dist == float('inf'):
            answer.append(-1)
        else:
            answer.append(dist)
    
    return answer