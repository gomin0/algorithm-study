def solution(want, number, discount):
    answer: int = 0
    wants: dict[str, int] = dict(zip(want, number))
    goods: dict[str, int] = dict(zip(want, [0] * len(number)))
    length: int = len(discount)
    for i in range(10):
        good: str = discount[i]
        if good in goods:
            goods[good] += 1
    if wants == goods:
        answer += 1
    
    i: int = 1
    j: int = 10
    
    while j < length:
        good1: str = discount[i-1]
        good2: str = discount[j]
        if good1 in goods:
            goods[good1] -= 1
        if good2 in goods:
            goods[good2] += 1
        if wants == goods:
            answer += 1
        i += 1
        j += 1
    
    return answer