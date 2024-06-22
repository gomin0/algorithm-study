def solution(x, n):
    answer = []
    a = 1;
    for i in range(n):
        answer.append(x * a)
        a += 1
    
    return answer