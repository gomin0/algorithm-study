#dfs
def solution(n, computers):
    def dfs(node):
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i)
                
    visited = [False for _ in range(n)]
    
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    return count

# bfs
# from collections import deque

# def solution(n, computers):
#     def bfs(start):
#         queue = deque([start])
#         visited[start] = True
        
#         while queue:
#             node = queue.popleft()
            
#             for i in range(n):
#                 if computers[node][i] == 1 and not visited[i]:
#                     queue.append(i)
#                     visited[i] = True
                    
#     visited = [False for _ in range(n)]
    
#     count = 0
#     for i in range(n):
#         if not visited[i]:
#             bfs(i)
#             count += 1
            
#     return count