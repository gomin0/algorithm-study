import heapq
from collections import defaultdict

def dijkstra(start, n, graph):
    distance = {i: float('inf') for i in range(1, n+1)}
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        now_distance, now_node = heapq.heappop(queue)
        if now_distance > distance[now_node]:
            continue
        
        for next_distance, next_node in graph[now_node]:
            dist = now_distance + next_distance
            if dist < distance[next_node]:
                distance[next_node] = dist
                heapq.heappush(queue, (dist, next_node))
    return distance

def solution(n, s, a, b, fares):
    answer = float('inf')
    
    graph = defaultdict(list)
    for start, end, d in fares:
        graph[start].append((d, end))
        graph[end].append((d, start))
        
    ab_taxi = dijkstra(s, n, graph)
    a_taxi = dijkstra(a, n, graph)
    b_taxi = dijkstra(b, n, graph)
    
    for i in range(1, n+1):
        total_taxi = ab_taxi[i] + a_taxi[i] + b_taxi[i]
        if answer > total_taxi:
            answer = total_taxi
    
    return answer