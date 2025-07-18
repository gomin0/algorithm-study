def solution(n, k, cmd):
    prev = [i - 1 for i in range(n)]
    next = [i + 1 for i in range(n)]
    next[-1] = -1
    remove = []
    is_deleted = [False] * n
    
    for c in cmd:
        if c[0] == "U":
            degree = int(c[2:])
            for _ in range(degree):
                k = prev[k]
        elif c[0] == "D":
            degree = int(c[2:])
            for _ in range(degree):
                k = next[k]
        elif c[0] == "C":
            remove.append(k)
            is_deleted[k] = True
            if prev[k] != -1:
                next[prev[k]] = next[k]
            if next[k] != -1:
                prev[next[k]] = prev[k]
            k = next[k] if next[k] != -1 else prev[k]
        elif c[0] == "Z":
            restore = remove.pop()
            is_deleted[restore] = False
            if prev[restore] != -1:
                next[prev[restore]] = restore
            if next[restore] != -1:
                prev[next[restore]] = restore
    
    answer = ''.join('X' if x else 'O' for x in is_deleted)
    return answer