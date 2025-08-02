def solution(n):
    answer = 0
    
    def dfs(open, close):
        nonlocal answer
        if open == n and close == n:
            answer += 1
        if open < n:
            dfs(open+1, close)
        if close < open:
            dfs(open, close+1)
    
    dfs(0, 0)
    return answer