def solution(a, b, n):
    answer = 0
    
    while n >= a:
        rest = n % a
        answer += (n // a) * b
        n = (n // a) * b + rest
    
    return answer