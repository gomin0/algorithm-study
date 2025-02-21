import sys

n = int(sys.stdin.readline().strip())
dp = [[0 for _ in range(3)] for _ in range(n)]
dp[0][0], dp[0][1], dp[0][2] = map(int, sys.stdin.readline().split())

for i in range(1, n):
    n1, n2, n3 = map(int, sys.stdin.readline().split())
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + n1
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + n2
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + n3

print(min(dp[n-1]))