import heapq
from collections import defaultdict

def dijkstra(start, N, graph):
    distance = {i: float('inf') for i in range(1, N+1)}
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
    
def solution(N, road, K):
    answer = 0

    graph = defaultdict(list)
    
    for start, end, time in road:
        graph[start].append((time, end))
        graph[end].append((time, start))

    distance = dijkstra(1, N, graph)
    
    for d in distance.values():
        if d <= K:
            answer += 1
    
    return answer