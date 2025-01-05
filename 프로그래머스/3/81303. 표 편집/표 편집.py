def solution(n, k, cmd):
    
    table = {i:[i-1, i+1] for i in range(n)}
    table[0][0] = None
    table[n-1][1] = None
    deleted = []  # 삭제 행
    
    pointer = k
    for command in cmd:
        if len(command) > 2:
            c, degree = command.split()
            degree = int(degree)
            if c == "D":
                for i in range(degree):
                    pointer = table[pointer][1]
            if c == "U":
                for i in range(degree):
                    pointer = table[pointer][0]
        else:
            if command == "C":
                idx, u_idx, d_idx = pointer, table[pointer][0], table[pointer][1]
                if u_idx != None:
                    table[u_idx][1] = d_idx
                if d_idx != None:
                    table[d_idx][0] = u_idx
                    
                if d_idx == None:
                    pointer = u_idx
                else:
                    pointer = d_idx
                    
                deleted.append((idx, u_idx, d_idx))
            else:  # command == "D"
                idx, u_idx, d_idx = deleted.pop()
                if u_idx != None:
                    table[u_idx][1] = idx
                if d_idx != None:
                    table[d_idx][0] = idx
    
    answer = ["O"] * n
    for d in deleted:
        answer[d[0]] = "X"
    
    return ''.join(answer)