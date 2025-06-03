import math

def solution(n,a,b):
    times: int = 0
    max_times: int = int(math.log2(n))
    
    for i in range(max_times):
        if a == b:
            break
        a = (a+1) // 2
        b = (b+1) // 2
        times += 1
    
    return times