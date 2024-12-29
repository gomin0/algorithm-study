def key_rotation(key):  # 키 돌리기
    m = len(key)
    rotation = []
    
    for i in range(m):
        key_line = []
        for j in range(m):
            key_line.append(key[m-1-j][i])
        rotation.append(key_line)
    return rotation

def check(key, expanded_lock, a, b, n, m):
    test_lock = [row[:] for row in expanded_lock]
    
    for i in range(m):
        for j in range(m):
            if 0 <= a + i < n + 2 * (m - 1) and 0 <= b + j < n + 2 * (m - 1):
                test_lock[a+i][b+j] += key[i][j]
                
    for i in range(n):
        for j in range(n):
            if test_lock[m-1+i][m-1+j] != 1:
                return False
    return True

def solution(key, lock):
    
    m, n = len(key), len(lock)
    expanded_len = n + 2 * (m - 1)
    expanded_lock = [[0] * expanded_len for _ in range(expanded_len)]
    
    for i in range(n):
        for j in range(n):
            expanded_lock[m-1+i][m-1+j] = lock[i][j]  # 기존 자물쇠 값 이식
    
    for _ in range(4):  # 네 방향으로 열쇠 돌리기
        key = key_rotation(key)
        for a in range(n+m-1):
            for b in range(n+m-1):
                if check(key, expanded_lock, a, b, n, m):
                    return True
    
    return False