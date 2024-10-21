def solution(sticker):
    answer = 0
    
    n = len(sticker)
    
    if n == 1:
        return sticker[0]
    
    dp1 = [0] * n  # 처음 거 먹는 경우
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    
    for i in range(2, n-1):  # 마지막 못먹음
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
        
    dp2 = [0] *n  # 마지막 거 먹는 경우
    dp2[1] = sticker[1]
    
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    
    return max(dp1[n-2], dp2[n-1])