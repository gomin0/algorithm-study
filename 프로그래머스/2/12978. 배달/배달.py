# 플로이드 워셜
def floyd_warshall(graph, N):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph
    

def solution1(N, road, K):
    answer = 0

    graph = [[float('inf')] * (N+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        graph[i][i] = 0
        
    for start, end, time in road:
        graph[start][end] = min(graph[start][end], time)
        graph[end][start] = min(graph[end][start], time)
    
    graph = floyd_warshall(graph, N)
    
    for j in range(1, N + 1):
        if graph[1][j] <= K:
            answer += 1

    return answer


# 다익스트라
import heapq
from collections import defaultdict

def dijkstra(start, N, graph):
    
    distance = {i: float('inf') for i in range(1, N + 1)}
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        now_distance, now_node = heapq.heappop(queue)
        if now_distance > distance[now_node]:
            continue
        
        for next_node, next_distance in graph[now_node]:
            dist = now_distance + next_distance
            if dist < distance[next_node]:
                distance[next_node] = dist
                heapq.heappush(queue, (dist, next_node))
    
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