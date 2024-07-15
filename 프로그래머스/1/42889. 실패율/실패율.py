def solution(N, stages):
    answer = []
    rate = {i: 0 for i in range(1, N + 1)}
    
    for i in range(1, N + 1):
        count = 0
        fail = 0
        for j in stages:
            if j >= i:
                count += 1
            if j == i:
                fail += 1
        if count == 0:  # count가 0이면 실패율을 0으로 설정
            rate[i] = 0
        else:
            rate[i] = fail / count
    
    return sorted(rate, key=lambda x : rate[x], reverse=True)