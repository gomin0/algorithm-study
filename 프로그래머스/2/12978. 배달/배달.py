# 플로이드 워셜
def floyd_warshall(graph, N):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph
    

def solution(N, road, K):
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

def dijkstra(N, start, graph):
    distance = {i: float('inf') for i in range(1, N+1)}
    distance[start] = 0
    
    hq = []
    heapq.heappush(hq, (0, start))
    
    while hq:
        now_dist, now_node = heapq.heappop(hq)
        if now_dist > distance[now_node]:
            continue
        for next_node, next_dist in graph[now_node]:
            dist = now_dist + next_dist
            if dist < distance[next_node]:
                distance[next_node] = dist
                heapq.heappush(hq, (dist, next_node))
    
    return distance

def solution1(N, road, K):
    answer = 0

    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    distances = dijkstra(N, 1, graph)
    
    for i in distances.values():
        if i <= K:
            answer += 1
    
    return answer