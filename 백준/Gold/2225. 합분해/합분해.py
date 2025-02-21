import sys

n, k = map(int, sys.stdin.readline().split())

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]  # i개로 j만들기
for j in range(n+1):
    dp[1][j] = 1  # 자기자신

for i in range(2, k+1):
    for j in range(n+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000

print(dp[k][n])