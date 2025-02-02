import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    
    graph = defaultdict(list)
    for a, b, c in paths:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    summit_set = set(summits)
    
    def dijkstra():
        intensity = [float('inf')] * (n + 1)
        pq = []  # (현재까지의 intensity, 현재 노드)
        
        for gate in gates:
            heapq.heappush(pq, (0, gate))
            intensity[gate] = 0
        
        while pq:
            cost, node = heapq.heappop(pq)
            
            # 이미 더 좋은 경로가 있으면 무시 (중복 계산 방지)
            if cost > intensity[node]:
                continue
                
            if node in summit_set:
                continue  # 최적의 상태로 도달한거라 왔던 길 그대로 돌아가면 됨
            
            for next_node, weight in graph[node]:
                new_intensity = max(cost, weight)
                
                if new_intensity < intensity[next_node]:
                    intensity[next_node] = new_intensity
                    heapq.heappush(pq, (new_intensity, next_node))
        return intensity
    
    result = dijkstra()
    best_summit = (-1, float('inf'))
    for summit in sorted(summits):
        if result[summit] < best_summit[1]:
            best_summit = (summit, result[summit])
    
    return list(best_summit)