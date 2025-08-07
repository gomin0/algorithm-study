import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for n1, n2, d in paths:
        graph[n1].append((n2, d))
        graph[n2].append((n1, d))
    
    # in 빠르게 하기 위함
    summits_set = set(summits)
    intensity = [float('inf')] * (n + 1)
    hq = []
    
    for gate in gates:
        heapq.heappush(hq, (0, gate))
        intensity[gate] = 0
    
    while hq:
        dist, node = heapq.heappop(hq)
        if node in summits_set or dist > intensity[node]:
            continue
        for next_node, next_dist in graph[node]:
            new_intensity = max(dist, next_dist)
            if new_intensity < intensity[next_node]:
                intensity[next_node] = new_intensity
                heapq.heappush(hq, (new_intensity, next_node))
    
    min_intensity = float('inf')
    min_summit = 0
    for summit in sorted(summits):
        if intensity[summit] < min_intensity:
            min_intensity = intensity[summit]
            min_summit = summit
            
    return [min_summit, min_intensity]