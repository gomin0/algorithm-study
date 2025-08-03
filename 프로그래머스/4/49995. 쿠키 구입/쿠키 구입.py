def solution(cookie):
    answer: int = 0
    n: int = len(cookie)
    
    for m in range(n-1):
        left: int = m
        right: int = m + 1
        left_sum: int = cookie[left]
        right_sum: int = cookie[right]
        
        while True:
            if left_sum == right_sum:
                answer = max(answer, left_sum)
            if left_sum <= right_sum:
                left -= 1
                if left < 0:
                    break
                left_sum += cookie[left]
            else:
                right += 1
                if right >= n:
                    break
                right_sum += cookie[right]
    
    return answer