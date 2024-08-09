def solution(order):
    answer = 0
    box = []
    second_box = []
    
    for i in range(len(order), 0, -1):
        box.append(i)
    
    idx = 0
    while box or second_box:
        now = order[idx]
        if box and box[-1] == now:
            box.pop()
            idx += 1
            answer += 1
        elif second_box and second_box[-1] == now:
            second_box.pop()
            idx += 1
            answer += 1
        elif box:
            second_box.append(box.pop())
        else:
            break
    
    return answer