from collections import deque, defaultdict

def bfs(graph, start, n):
    distance = [-1] * (n+1)
    distance[start] = 0
    queue = deque([start])
    
    while queue:
        current_node = queue.popleft()
        current_distance = distance[current_node]
        
        for next_node in graph[current_node]:
            if distance[next_node] == -1:
                distance[next_node] = current_distance + 1
                queue.append(next_node)
    return distance

def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    distance = bfs(graph, 1, n)
    max_distance = max(distance)
    
    return distance.count(max_distance)