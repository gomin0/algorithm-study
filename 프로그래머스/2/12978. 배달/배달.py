from collections import defaultdict
import heapq


def dijkstra(N, graph, start):
    distance = {i: float('inf') for i in range(1, N+1)}
    distance[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    
    while hq:
        now_dist, now_node = heapq.heappop(hq)
        if now_dist > distance[now_node]:
            continue
        for next_dist, next_node in graph[now_node]:
            new_dist = now_dist + next_dist
            if distance[next_node] > new_dist:
                distance[next_node] = new_dist
                heapq.heappush(hq, (new_dist, next_node))
    
    return distance


def solution(N, road, K):
    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append((c, b))
        graph[b].append((c, a))

    distance = dijkstra(N, graph, 1)
    answer = 0
    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1

    return answer