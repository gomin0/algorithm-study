def solution(k, dungeons):
    
    def dfs(k, dungeons, visited, count):
        max_count = count
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                max_count = max(max_count, dfs(k - dungeons[i][1], dungeons, visited, count + 1))
                visited[i] = False
        return max_count
    
    visited = [False] * len(dungeons)
    
    
    return dfs(k, dungeons, visited, 0)