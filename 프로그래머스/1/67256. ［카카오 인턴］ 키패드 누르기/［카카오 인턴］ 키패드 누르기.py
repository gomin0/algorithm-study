def dist(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(y2-y1) + abs(x2-x1)

def solution(numbers, hand):
    answer = ''
    
    key = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        "*": [3, 0], 0: [3, 1], "#": [3, 2]
    }
    
    l_key = key["*"]
    r_key = key["#"]
    
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            l_key = key[i]
        elif i in [3, 6, 9]:
            answer += 'R'
            r_key = key[i]
        else:
            if dist(l_key, key[i]) < dist(r_key, key[i]):
                answer += 'L'
                l_key = key[i]
            elif dist(l_key, key[i]) > dist(r_key, key[i]):
                answer += 'R'
                r_key = key[i]
            else:
                if hand == "left":
                    answer += 'L'
                    l_key = key[i]
                else:
                    answer += 'R'
                    r_key = key[i]
    
    return answer