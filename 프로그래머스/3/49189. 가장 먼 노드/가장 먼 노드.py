from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    
    def bfs(n, start, graph):
        distance = [-1 for _ in range(n)]
        distance[start] = 0
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            dist = distance[node]
            for next_node in graph[node]:
                if distance[next_node] == -1:
                    distance[next_node] = dist + 1
                    queue.append(next_node)
        return distance
    
    graph = defaultdict(list)
    for a, b in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    distance = bfs(n, 0, graph)
    
    return distance.count(max(distance))