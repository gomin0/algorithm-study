def solution(picks, minerals):
    answer = 0
    
    length = len(minerals)
    count = length // 5
    rest = length % 5
    sequence = 0
    
    weight = []
    
    for i in range(0, count * 5, 5):
        w = 0
        temp = minerals[i:i+5]
        for i in temp:
            if i == "diamond":
                w += 25
            elif i == "iron":
                w += 5
            else:  # i == "stone":
                w += 1
        weight.append((w, sequence))
        sequence += 1
        
    if rest > 0:
        temp = minerals[-rest:]
        w = 0
        for i in temp:
            if i == "diamond":
                w += 25
            elif i == "iron":
                w += 5
            else:  # i == "stone":
                w += 1
        weight.append((w, sequence))
    weight.sort(reverse = True)
    
    result = []
    for w in weight:
        if picks[0] > 0:
            result.append((w[1], "d"))
            picks[0] -= 1
        elif picks[1] > 0:
            result.append((w[1], "i"))
            picks[1] -= 1
        elif picks[2] > 0:
            result.append((w[1], "s"))
            picks[2] -= 1
        else:
            break
    
    result.sort()
    
    pick_index = 0
    mineral_index = 0
    can = 5  # 내구도
    fatigue = 0  # 피로도
    while pick_index < len(result) and mineral_index < len(minerals):
        if result[pick_index][1] == "d":
            fatigue += 1
        elif result[pick_index][1] == "i":
            if minerals[mineral_index] == "diamond":
                fatigue += 5
            else:
                fatigue += 1
        else:
            if minerals[mineral_index] == "diamond":
                fatigue += 25
            elif minerals[mineral_index] == "iron":
                fatigue += 5
            else:
                fatigue += 1
        can -= 1
        mineral_index += 1
        if can == 0:
            can = 5
            pick_index += 1
        
    return fatigue