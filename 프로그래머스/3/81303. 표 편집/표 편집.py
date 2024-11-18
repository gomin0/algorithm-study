def solution(n, k, cmd):
    print(n)
    
    table = {i: [i - 1, i + 1] for i in range(n)}  # 연결 리스트 처럼
    table[0][0] = None  # 첫 번째 행은 이전이 없음
    table[n-1][1] = None  # 마지막 행은 다음이 없음
    
    stack = []  # 삭제된 행 정보
    current = k
    
    for c in cmd:
        parts = c.split()
        if parts[0] == 'U':
            x = int(parts[1])
            while x > 0:
                current = table[current][0]
                x -= 1
        elif c[0] == 'D':
            x = int(parts[1])
            while x > 0:
                current = table[current][1]
                x -= 1
        elif parts[0] == 'C':
            prev_link, next_link = table[current]
            stack.append((current, prev_link, next_link))
            
            if prev_link is not None:
                table[prev_link][1] = next_link
            if next_link is not None:
                table[next_link][0] = prev_link
            
            current = next_link if next_link is not None else prev_link
        elif parts[0] == 'Z':
            restore, prev_link, next_link = stack.pop()
            
            if prev_link is not None:
                table[prev_link][1] = restore
            if next_link is not None:
                table[next_link][0] = restore
    
    answer = ['O' for _ in range(n)]
    while stack:
        deleted_row = stack.pop()[0]
        answer[deleted_row] = 'X'
    
    return ''.join(answer)