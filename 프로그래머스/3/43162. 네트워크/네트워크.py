def solution(n, computers):
    answer: int = 0
    
    def dfs(start):
        visited.add(start)
        for i in range(n):
            if computers[start][i] == 1 and i not in visited:
                dfs(i)
    
    visited: set[int] = set()
    for i in range(n):
        if i not in visited:
            dfs(i)
            answer += 1
            
    return answer