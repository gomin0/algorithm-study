def solution(n):
    answer: int = 1
    
    sum_num: int = 0
    for i in range(1, n-1):
        sum_num += i
        for j in range(i + 1, n):
            sum_num += j
            if sum_num == n:
                answer += 1
                sum_num = 0
                break
            elif sum_num > n:
                sum_num = 0
                break
    
    return answer