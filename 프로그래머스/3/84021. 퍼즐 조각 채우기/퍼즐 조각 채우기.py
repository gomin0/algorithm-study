def normalize_puzzle(puzzle):
    # 모든 x좌표의 최소값, y좌표의 최소값을 찾음
    min_x = min(x for x, y in puzzle)
    min_y = min(y for x, y in puzzle)
    
    # 최소값을 빼서 정규화
    return sorted([(x - min_x, y - min_y) for x, y in puzzle])

def dfs(node, graph, target, visited):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = []
    stack.append(node)
    n = len(graph)
    visited[node[0]][node[1]] = True
    puzzle = [(0, 0)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            dx, dy = direction[i]
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == target:
                visited[nx][ny] = True
                rel_x = nx - node[0]
                rel_y = ny - node[1]
                puzzle.append((rel_x, rel_y))
                stack.append((nx, ny))
                
    return normalize_puzzle(puzzle), visited

def puzzle_rotate(puzzle):
    rotations = []
    current = puzzle
    
    # 4번의 회전 (0, 90, 180, 270도)
    for _ in range(4):
        rotations.append(current)
        # 다음 회전을 위한 변환
        current = normalize_puzzle([(y, -x) for x, y in current])
    
    return rotations

def solution(game_board, table):
    answer = 0
    
    n = len(game_board)
    g_visited = [[False] * n for _ in range(n)]
    t_visited = [[False] * n for _ in range(n)]
    puzzle_list = []
    
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not t_visited[i][j]:
                puzzle, t_visited = dfs((i, j), table, 1, t_visited)
                puzzle_list.append(puzzle_rotate(puzzle))
    
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not g_visited[i][j]:
                board, g_visited = dfs((i, j), game_board, 0, g_visited)
                for idx, rotations in enumerate(puzzle_list):
                    if board in rotations:
                        answer += len(board)
                        puzzle_list.pop(idx)
                        break
                    
    return answer