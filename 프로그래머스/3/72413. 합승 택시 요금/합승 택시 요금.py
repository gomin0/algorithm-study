from collections import defaultdict
import heapq


def dijkstra(graph, start, n):
    distance: dict[int, int] = {i: float('inf') for i in range(1, n+1)}
    distance[start] = 0
    
    queue: list[tuple[int, int]] = []
    heapq.heappush(queue, (distance[start], start))
    
    while queue:
        dist, node = heapq.heappop(queue)
        if distance[node] < dist:
            continue
        for next_dist, next_node in graph[node]:
            next_dist += dist
            if distance[next_node] > next_dist:
                distance[next_node] = next_dist
                heapq.heappush(queue, (next_dist, next_node))
    return distance


# 지점 개수, 출발, a, b, [c, d, f원]
def solution(n, s, a, b, fares):
    answer = float('inf')
    
    graph = defaultdict(list)
    for start, end, dist in fares:
        graph[start].append((dist, end))
        graph[end].append((dist, start))
    
    distance_from_s = dijkstra(graph, s, n)
    distance_from_a = dijkstra(graph, a, n)
    distance_from_b = dijkstra(graph, b, n)
    
    for i in range(1, n+1):
        answer = min(
            answer,
            distance_from_s[i] + distance_from_a[i] + distance_from_b[i]
        )
    
    return answer