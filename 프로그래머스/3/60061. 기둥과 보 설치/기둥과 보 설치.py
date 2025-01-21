def check(structures):  # 현재 구조물이 유효한지 체크
    for x, y, a in structures:
        if a == 0:  #기둥
            if y == 0 or (x, y-1, 0) in structures or (x-1, y, 1) in structures or (x,y, 1) in structures:  # 바닥 위 or 다른 기둥 위 or 왼쪽 보 위 or 오른쪽 보 위
                continue  # 통과
            return False  # 유효하지 않음
        elif a == 1:  # 보
            if (x, y-1, 0) in structures or (x+1, y-1, 0) in structures or ((x-1, y, 1) in structures and (x+1, y, 1) in structures):  # 왼쪽 기둥 위 or 오른쪽 기둥 위 or 양쪽이 보로 연결
                continue  # 통과
            return False  # 유효하지 않음
    return True  # 유효한 경우
    
def solution(n, build_frame):
    structures = set()
    
    for x, y, a, b in build_frame:
        if b == 0:  # 삭제
            structures.remove((x, y, a))  # 삭제
            if not check(structures):  # 유효하지 않으면
                structures.add((x, y, a))  # 복구
        else:  # 설치
            structures.add((x, y, a))  # 설치
            if not check(structures):  # 유효하지 않으면
                structures.remove((x, y, a))  # 삭제
        
        answer = sorted(structures, key=lambda item: (item[0], item[1], item[2]))
        
    return answer