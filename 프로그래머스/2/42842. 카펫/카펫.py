def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            a = i
            b = yellow / i
            if (a *2 + b * 2 + 4) == brown:
                return [b+2, a+2]