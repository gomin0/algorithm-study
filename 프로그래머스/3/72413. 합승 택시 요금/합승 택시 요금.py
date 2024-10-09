import heapq

def dijkstra(start, n, graph):
    distance = {i: float('inf') for i in range(1, n+1)}
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (start, 0))
    
    while queue:
        now_node, now_distance = heapq.heappop(queue)
        if now_distance > distance[now_node]:
            continue
        for next_node, next_distance in graph[now_node]:
            dist = now_distance + next_distance
            if dist < distance[next_node]:
                distance[next_node] = dist
                heapq.heappush(queue, (next_node, dist))
    return distance

def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = [[] for i in range(n+1)]
    
    for start, end, d in fares:
        graph[start].append((end, d))
        graph[end].append((start, d))
    
    ab_distance = dijkstra(s, n, graph)
    a_distance = dijkstra(a, n, graph)
    b_distance = dijkstra(b, n, graph)
    
    for i in range(1, n+1):
        total_distance = ab_distance[i] + a_distance[i] + b_distance[i]
        if total_distance < answer:
            answer = total_distance
    
    return answer