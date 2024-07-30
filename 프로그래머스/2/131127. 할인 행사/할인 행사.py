def solution(want, number, discount):
    answer = 0
    bascket = []
    wanted = []
    
    for idx, i in enumerate(want):
        for _ in range(number[idx]):
            wanted.append(i)

    wanted.sort()
        
    
    for i in range(len(discount)):
        if i+10 <= len(discount):
            bascket = discount[i:i+10]
            bascket.sort()
            if bascket == wanted:
                answer += 1
        else:
            break
    
    return answer