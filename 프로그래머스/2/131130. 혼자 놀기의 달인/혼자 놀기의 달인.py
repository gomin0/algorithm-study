def pick(cards, n, pickup):  # cards에서 n번째 상자를 골랐을 때 벌어지는 일
    count = 0
    while pickup[n]:
        pickup[n] = False
        n = cards[n] - 1  # 0 base니까
        count += 1
    return count, pickup
    

def solution(cards):
    length = len(cards)
    record = []
    
    for i in range(length):
        pickup = [True for _ in range(length)]
        pick1 = i
        pick1_count, pickup = pick(cards, pick1, pickup)
        if pick1_count == length:
            return 0
        for j in range(length):
            if pickup[j]:
                pick2 = j
                pick2_count, pickup = pick(cards, pick2, pickup)
                record.append(pick1_count * pick2_count)
    
    return max(record)