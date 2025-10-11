from collections import defaultdict
import heapq


def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = [float('inf')] * (n + 1)
    distance[1] = 0
    distance[0] = 0
    hq = []
    heapq.heappush(hq, (0, 1))
    
    while hq:
        dist, node = heapq.heappop(hq)
        if distance[node] < dist:
            continue
        for next_node in graph[node]:
            next_dist = dist + 1
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heapq.heappush(hq, (next_dist, next_node))
    
    return distance.count(max(distance))