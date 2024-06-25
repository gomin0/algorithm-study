def solution(left, right):
    
    answer = 0
    
    for i in range(left, right + 1):
        count = 0
        if i % (i**(1/2)) == 0: # 홀수 개
            answer -= i
        else:
            answer += i
        # for j in range(1, i**(1/2)):
        #     if i % j == 0:
        #         count += 1
        # if i % (i**(1/2)) == 0:
        #     count = count * 2 + 1
        # else:
        #     count = count * 2
        
    return answer