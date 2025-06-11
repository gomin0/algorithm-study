def solution(m, n, puddles):
    dp: list[list[int]] = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if [j+1, i+1] in puddles:
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
            dp[i][j] %= 1000000007
    
    return dp[n-1][m-1]