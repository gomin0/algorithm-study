def check(struct):
    for x, y, a in struct:
        if a == 0:
            if y == 0 or (x, y-1, 0) in struct or (x-1, y, 1) in struct or (x,y, 1) in struct:
                continue
            return False
        else:
            if (x, y-1, 0) in struct or (x+1, y-1, 0) in struct or ((x-1, y, 1) in struct and (x+1, y, 1) in struct):
                continue
            return False
    return True

def solution(n, build_frame):
    struct: set[tuple[int, int ,int]] = set()
    
    for x, y, a, b in build_frame:
        if b == 0:
            struct.remove((x, y, a))
            if not check(struct):
                struct.add((x, y, a))
        else:
            struct.add((x, y, a))
            if not check(struct):
                struct.remove((x, y, a))
    
    return sorted(struct, key=lambda item: (item[0], item[1], item[2]))

# 가로좌표, 세로좌표, (0기둥, 1 보), (0 삭제, 1 설치)
# 기둥 -> 바닥 위 or 보의 한쪽 끝 위 or 다른 기둥 위
# 보 -> 한쪽 끝이 기둥 위 or 양 쪽 끝이 다른 보와 연결