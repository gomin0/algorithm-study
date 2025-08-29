def solution(strs, t):
    answer = 0
    n = len(t)
    pieces = set(strs)
    lens = {len(s) for s in pieces}
    
    INF = float('inf')
    dp = [INF] * (n+1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        for l in lens:
            if l <= i and t[i - l:i] in pieces:
                if dp[i-l] != INF:
                    dp[i] = min(dp[i], dp[i-l]+1)

    return -1 if dp[n] == INF else dp[n]