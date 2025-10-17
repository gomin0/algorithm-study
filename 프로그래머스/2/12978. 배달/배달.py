from collections import defaultdict
import heapq


def solution(N, road, K):
    graph = defaultdict(list)
    for a, b, w in road:
        graph[a].append((w, b))
        graph[b].append((w, a))
    
    dist = dijkstra(1, N, graph)

    answer = 1
    for i in range(2, N+1):
        if dist[i] <= K:
            answer += 1

    return answer


def dijkstra(start, n, graph):
    dist = {i: float('inf') for i in range(1, n+1)}
    dist[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        d1, node = heapq.heappop(hq)
        if d1 > dist[node]:
            continue
        for d2, next_node in graph[node]:
            d = d1 + d2
            if dist[next_node] > d:
                dist[next_node] = d
                heapq.heappush(hq, (d, next_node))
    
    return dist