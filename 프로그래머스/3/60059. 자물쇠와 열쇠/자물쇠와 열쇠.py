def key_rotation(key):
    m = len(key)
    rotation = []
    
    for i in range(m):
        key_line = []
        for j in range(m):
            key_line.append(key[m - 1 - j][i])
        rotation.append(key_line)
    return rotation

def check(key, expanded_lock, x, y, n, m):
    test_lock = [row[:] for row in expanded_lock]
    
    for i in range(m):
        for j in range(m):
            if 0 <= x + i < n + 2 * (m - 1) and 0 <= y + j < n + 2 * (m - 1):
                test_lock[x+i][y+j] += key[i][j]
    
    for i in range(n):
        for j in range(n):
            if test_lock[m-1+i][m-1+j] != 1:
                return False
    return True
    

def solution(key, lock):
    m, n = len(key), len(lock)
    expanded_lock = [[0] * (n + 2 * (m-1)) for _ in range(n + 2 * (m-1))]
    
    for i in range(n):
        for j in range(n):
            expanded_lock[m-1+i][m-1+j] = lock[i][j]
    
    for _ in range(4):
        key = key_rotation(key)
        for x in range(n+m-1):
            for y in range(n+m-1):
                if check(key, expanded_lock, x, y, n, m):
                    return True
    
    return False