import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for n1, n2, d in paths:
        graph[n1].append((d, n2))
        graph[n2].append((d, n1))
    
    summits_set = set(summits)
    intensity = [float('inf')] * (n + 1)
    hq = []
    for gate in gates:
        heapq.heappush(hq, (0, gate))
        intensity[gate] = 0
    
    while hq:
        dist, node = heapq.heappop(hq)
        if node in summits_set or intensity[node] < dist:
            continue
        for next_dist, next_node in graph[node]:
            new_intensity = max(dist, next_dist)
            if intensity[next_node] > new_intensity:
                intensity[next_node] = new_intensity
                heapq.heappush(hq, (new_intensity, next_node))
    
    min_summit = 0
    min_intensity = float('inf')
    for summit in sorted(summits):
        if min_intensity > intensity[summit]:
            min_intensity = intensity[summit]
            min_summit = summit
    
    return [min_summit, min_intensity]