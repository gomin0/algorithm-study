def solution(n):
    jump: int = 0
    
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            jump += 1
    return jump