def solution(n, m, section):
    answer = 0
    
    paint = [True] * n
    
    for i in section:
        paint[i - 1] = False

    j = 0
    while j < n:
        if not paint[j]:
            answer += 1
            j += m
        else:
            j += 1
            
    return answer