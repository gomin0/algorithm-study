from collections import deque, defaultdict

def bfs(n, start, graph):
    distance = [-1] * (n+1)
    distance[start] = 0
    queue = deque([start])
    
    while queue:
        current_node = queue.popleft()
        current_dist = distance[current_node]
        
        for next_node in graph[current_node]:
            if distance[next_node] == -1:
                distance[next_node] = current_dist + 1
                queue.append(next_node)
    return distance

def solution(n, edge):
    
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distance = bfs(n, 1, graph)
    max_distance = max(distance)
    
    return distance.count(max_distance)