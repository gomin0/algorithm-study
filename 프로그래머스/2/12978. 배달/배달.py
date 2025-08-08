import heapq
from collections import defaultdict

def dijkstra(graph, N, start):
    distance = {i: float('inf') for i in range(1, N+1)}
    distance[start] = 0
    
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        dist, node = heapq.heappop(hq)
        if dist > distance[node]:
            continue
        for next_dist, next_node in graph[node]:
            new_dist = dist + next_dist
            if distance[next_node] > new_dist:
                distance[next_node] = new_dist
                heapq.heappush(hq, (new_dist, next_node))
    return distance
    

def solution(N, road, K):
    answer = 0
    
    graph = defaultdict(list)
    for n1, n2, d in road:
        graph[n1].append((d, n2))
        graph[n2].append((d, n1))
    
    distance = dijkstra(graph, N, 1)
    
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1
    
    return answer