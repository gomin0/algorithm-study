# n = 4부터 특이 케이스 2개씩 존재
def solution(n):
    answer = 0
    MOD = 1000000007
    
    if n % 2 != 0:
        return 0
    dp = [0] * (n+1)
    dp[2] = 3
    
    for i in range(4, n + 1, 2):
        dp[i] = dp[i-2] * 3 + 2  # 전거 * 두칸 채우기 + 특이케이스 2
        for j in range(i-4, -1, -2):
            dp[i] += dp[j] * 2  # 그전거들 특이케이스 앞뒤
        dp[i] = dp[i] % MOD
    
    return dp[n]