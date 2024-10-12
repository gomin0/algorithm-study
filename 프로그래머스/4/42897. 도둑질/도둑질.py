def solution(money):
    answer = 0
    n = len(money)
    
    # 첫집 털기
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = money[0]
    
    for i in range(2, n-1):  # 마지막 집 제외
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    
    # 마지막집 털기
    dp2 = [0] * n
    dp2[0] = 0
    dp2[1] = money[1]
    
    for j in range(2, n):
        dp2[j] = max(dp2[j - 1], dp2[j - 2] + money[j])
        
    answer = max(dp1[n - 2], dp2[n - 1])
    
    
    return answer