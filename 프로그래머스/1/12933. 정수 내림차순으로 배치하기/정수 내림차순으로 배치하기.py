def solution(n):
    s = list(str(n))
    s.sort(reverse=True)
    
    answer = int(''.join(s))
    return answer