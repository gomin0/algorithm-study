import sys

n = int(sys.stdin.readline().strip())
dp = [0] * n
dp[0] = 3

if n > 1:
    dp[1] = 7

for i in range(2, n):
    dp[i] = (dp[i-2] * 3 + (dp[i-1] - dp[i-2]) * 2) % 9901

print(dp[n-1])