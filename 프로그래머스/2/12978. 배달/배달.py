# 다익스트라
import heapq
from collections import defaultdict

def dijkstra(start, N, graph):
    
    distance = {i: float('inf') for i in range(1, N + 1)}
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (start, 0))
    
    while queue:
        now_node, now_distance = heapq.heappop(queue)
        if now_distance > distance[now_node]:
            continue
        
        for next_node, next_distance in graph[now_node]:
            dist = now_distance + next_distance
            if dist < distance[next_node]:
                distance[next_node] = dist
                heapq.heappush(queue, (next_node, dist))
    
    return distance

def solution(N, road, K):
    answer = 0

    graph = defaultdict(list)
    for start, end, time in road:
        graph[start].append((end, time))
        graph[end].append((start, time))
        
    distance = dijkstra(1, N, graph)
    
    for i in distance.values():
        if i <= K:
            answer += 1

    return answer