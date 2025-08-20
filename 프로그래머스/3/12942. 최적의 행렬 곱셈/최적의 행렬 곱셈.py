def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[0] * n for _ in range(n)]
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = (dp[i][k] + dp[k+1][j] + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1])
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n-1]