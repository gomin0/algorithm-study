def solution(m, n, puddles):
    answer = 0
    
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    for x, y in puddles:
        dp[y-1][x-1] = -1
        
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                continue
            if dp[i-1][j] != -1 and i > 0:
                dp[i][j] += dp[i-1][j]
            if dp[i][j-1] != -1 and j > 0:
                dp[i][j] += dp[i][j-1]
            dp[i][j] %= 1000000007
    
    return dp[n-1][m-1]