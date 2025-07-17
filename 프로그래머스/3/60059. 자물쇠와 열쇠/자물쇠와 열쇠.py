
def rotate(matrix):
    return list(zip(*matrix[::-1]))


def check(expanded_lock, M, N):
    # 자물쇠의 원래 중심 영역만 확인
    for i in range(N):
        for j in range(N):
            if expanded_lock[i + M - 1][j + M - 1] != 1:
                return False
    return True


def solution(key, lock):
    M: int = len(key)
    N: int = len(lock)
    size: int = N + 2 * (M - 1)
    
    for _ in range(4):
        key = rotate(key)
        
        for x in range(size - M + 1):
            for y in range(size - M + 1):
                expanded_lock: list[list[int]] = [[0] * size for _ in range(size)]
                
                # 중앙에 자물쇠 넣기
                for i in range(N):
                    for j in range(N):
                        expanded_lock[i + M -1][j + M -1] = lock[i][j]
                
                # 열쇠 맞추기
                for i in range(M):
                    for j in range(M):
                        expanded_lock[x + i][y + j] += key[i][j]
                
                if check(expanded_lock, M, N):
                    return True
    
    return False