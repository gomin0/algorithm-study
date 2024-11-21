def is_valid(structures):
    for x, y, a in structures:
        if a == 0:  # 기둥
            # 바닥 위, 다른 기둥 위, 보 위
            if y == 0 or (x, y-1, 0) in structures or (x-1, y, 1) in structures or (x, y, 1) in structures:
                continue
            return False
        elif a == 1:  # 보
            # 한쪽 끝 기둥 위, 양쪽 끝이 다른 보와 연결
            if (x, y-1, 0) in structures or (x+1, y-1, 0) in structures or ((x-1, y, 1) in structures and (x+1, y, 1) in structures):
                continue
            return False
    return True

def solution(n, build_frame):    
    structures = set()
    
    for x, y, a, b in build_frame:
        if b == 0:  # 삭제
            structures.remove((x, y, a))
            if not is_valid(structures):
                structures.add((x, y, a))
        else:  # 설치
            structures.add((x, y, a))
            if not is_valid(structures):
                structures.remove((x, y, a))
    
    answer = sorted(structures, key=lambda item: (item[0], item[1], item[2]))
    
    return answer