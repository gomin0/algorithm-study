def solution(sticker) -> int:
    length: int = len(sticker)
    
    if length == 1:
        return sticker[0]
    
    dp1: list[int] = [0] * length
    dp2: list[int] = [0] * length
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    dp2[1] = sticker[1]
    
    for i in range(2, length - 1):
        dp1[i] = max(dp1[i-2] + sticker[i], dp1[i-1])
    
    for i in range(2, length):
        dp2[i] = max(dp2[i-2] + sticker[i], dp2[i-1])
    
    answer: int = max(dp1[-2], dp2[-1])
    return answer