from collections import deque, defaultdict

def bfs(n, graph, start):
    count = 1
    q = deque([start])
    visited = {i:False for i in range(1, n+1)}
    visited[start] = True

    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                count += 1
                q.append(next_node)
    
    return abs(count - (n-count))
            
            
def solution(n, wires):
    answer = float('inf')
    
    graph = defaultdict(list)
    
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
                
    for a, b in wires:
        # 끊기
        graph[a].remove(b)
        graph[b].remove(a)
    
        answer = min(bfs(n, graph, a), answer)
        
        # 복구
        graph[a].append(b)
        graph[b].append(a)
        
    return answer