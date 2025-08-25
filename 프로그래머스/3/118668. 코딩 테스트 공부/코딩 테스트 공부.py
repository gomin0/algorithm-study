def solution(alp, cop, problems):
    target_alp = max(p[0] for p in problems)
    target_cop = max(p[1] for p in problems)
    alp = min(alp, target_alp)
    cop = min(cop, target_cop)
    
    dp = [[float('inf')] * (target_cop + 1) for _ in range(target_alp + 1)]
    dp[alp][cop] = 0
    
    for a in range(alp, target_alp + 1):
        for c in range(cop, target_cop + 1):
            if a+1 <= target_alp:
                dp[a+1][c] = min(dp[a+1][c], dp[a][c] + 1)
            if c+1 <= target_cop:
                dp[a][c+1] = min(dp[a][c+1], dp[a][c] + 1)
            for req_a, req_c, rwd_a, rwd_c, cost in problems:
                if a >= req_a and c >= req_c:
                    na = min(target_alp, a + rwd_a)
                    nc = min(target_cop, c + rwd_c)
                    dp[na][nc] = min(dp[na][nc], dp[a][c] + cost)
    
    return dp[target_alp][target_cop]