def solution(numbers):
    answer = 0;
    
    for i in range(1, 10):
        answer += i
    
    for i in numbers:
        answer -= i
    
    return answer