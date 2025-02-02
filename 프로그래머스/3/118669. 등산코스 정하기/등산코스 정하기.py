import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    answer = []
    
    graph = defaultdict(list)
    
    for a, b, c in paths:
        graph[a].append((b, c))
        graph[b].append((a, c))

    summits_set = set(summits)
    
    pq = []
    intensity = [float('inf') for _ in range(n+1)]
    
    for gate in gates:
        heapq.heappush(pq, (0, gate))
        intensity[gate] = 0

    while pq:
        cost, node = heapq.heappop(pq)
        
        if cost > intensity[node]:
            continue
        if node in summits_set:
            continue
        
        for next_node, next_cost in graph[node]:
            new_intensity = max(cost, next_cost)
            if new_intensity < intensity[next_node]:
                intensity[next_node] = new_intensity
                heapq.heappush(pq, (new_intensity, next_node))
    
    best_summit = (-1, float('inf'))
    for summit in sorted(summits):
        if intensity[summit] < best_summit[1]:
            best_summit = (summit, intensity[summit])
    
    return list(best_summit)