# 그냥 2랑 1로 n을 만드는 가지수
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007  #이렇게 해야 값이 안커져서 시간초과 방지

    return dp[n]