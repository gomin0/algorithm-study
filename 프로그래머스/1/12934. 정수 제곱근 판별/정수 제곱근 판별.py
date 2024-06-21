import math

def solution(n):
    
    x = int(math.sqrt(n))
    
    if x ** 2 == n:
        return (x+1) ** 2
    
    else:
        return -1