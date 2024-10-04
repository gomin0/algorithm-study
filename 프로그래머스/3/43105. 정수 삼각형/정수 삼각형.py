def solution(triangle):
    answer = 0
    
    n = len(triangle)
    dp = [[0] * (d+1) for d in range(n)]

    dp[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(i+1):
            tri = triangle[i][j]
            if j == 0:
                dp[i][j] = tri + dp[i-1][j]
            elif j == i:
                dp[i][j] = tri + dp[i-1][j-1]
            else:
                dp[i][j] = tri + max(dp[i-1][j-1], dp[i-1][j])
        
    return max(dp[n-1])

# dp[4][0] = triangle[4][0] + dp[3][0]
# dp[4][1] = triangle[4][1] + max(dp[3][0], dp[3][1])
# ...
# dp[4][4] = triangle[4][4] + dp[3][3]

# [7]
# [3, 8]
# [8, 1, 0]
# [2, 7, 4, 4]
# [4, 5, 2, 6, 5]