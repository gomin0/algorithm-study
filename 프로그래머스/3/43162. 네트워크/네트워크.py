def solution(n, computers):    
    def dfs(start):
        stack: list[int] = [start]
        visited.add(start)
        while stack:
            node: int = stack.pop()
            for i in range(n):
                if computers[node][i] == 1 and i not in visited:
                    stack.append(i)
                    visited.add(i)
    
    answer: int = 0
    visited: set[int] = set()
    for i in range(n):
        if i not in visited:
            dfs(i)
            answer += 1
            
    return answer