def price(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    answer = []
    
    
    zero = 0
    count = 0
    
    for i in lottos:
        if i == 0:
            zero += 1
        for j in win_nums:
            if i == j:
                count += 1
                
    answer.append(price(zero + count))
    answer.append(price(count))
    
    return answer