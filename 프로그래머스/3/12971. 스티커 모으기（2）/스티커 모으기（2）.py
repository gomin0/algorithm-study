def solution(sticker):
    answer = 0
    
    n = len(sticker)
    
    if n == 1:
        return sticker[0]
    elif n == 2:
        return max(sticker)
    
    dp1 = [0 for _ in range(n)]
    dp2 = [0 for _ in range(n)]
    
    # 첫번째꺼 먹기 -> 두번째꺼, 마지막꺼 못먹음
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-2] + sticker[i], dp1[i-1])
    dp1[n-1] = dp1[n-2]
    
    # 찻번째꺼 안먹기
    dp2[1] = sticker[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-2] + sticker[i], dp2[i-1])

    return max(dp1[n-1], dp2[n-1])