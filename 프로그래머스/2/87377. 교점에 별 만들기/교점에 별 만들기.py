from itertools import combinations

# 교점 찾기
def intersect(a1, b1, c1, a2, b2, c2):
    parallel = a1 * b2 - a2 * b1
    
    if parallel == 0:  # 평행
        return None
    
    y = (a2 * c1 - a1 * c2) / parallel
    if a1 != 0:
        x = (-c1 -b1 * y) / a1
    else:
        x = (-c2 - b2 * y) / a2
    
    return (x, y)

def solution(line):
    star = []
    
    combination = list(combinations(line, 2))

    # 직선 선택
    for comb in combination:
        line1 = comb[0]
        line2 = comb[1]
        coordinate = intersect(line1[0], line1[1], line1[2], line2[0], line2[1], line2[2])
        
        # 정수 교점 찾기
        if coordinate is not None:
            x, y = coordinate
            if x.is_integer() and y.is_integer():
                star.append((int(x), int(y)))
    
    if not star:
        return []
    
    min_x = min(star, key=lambda s: s[0])[0]  # x값이 가장 작은 튜플의 x값
    max_x = max(star, key=lambda s: s[0])[0]
    min_y = min(star, key=lambda s: s[1])[1]
    max_y = max(star, key=lambda s: s[1])[1]
    
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    
    answer = [['.'] * width for _ in range(height)]
    
    for x, y in star:
        answer[max_y - y][x - min_x] = '*'

    answer = [''.join(row) for row in answer]
    
    return answer