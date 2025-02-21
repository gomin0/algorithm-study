import sys

n, k = map(int, sys.stdin.readline().split())
money = []
for _ in range(n):
    num = int(sys.stdin.readline())
    money.append(num)

dp = [0] * (k+1)
dp[0] = 1

for m in money:
    for i in range(m, k+1):
        dp[i] += dp[i-m]

print(dp[k])