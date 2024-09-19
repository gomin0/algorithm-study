def solution(name):
    # 각 문자를 변경하는데 필요한 상하 조작 횟수
    change = [min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name]
    answer = sum(change)
    
    n = len(name)
    move = n - 1  # 초기 이동 횟수: 오른쪽으로 쭉 이동하는 경우
    
    for i in range(n):
        next_i = i + 1
        # 연속된 A의 끝 지점 찾기
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        # 현재 위치에서 되돌아가는 경우와 그냥 쭉 가는 경우 중 최소값 선택
        move = min(move, i + n - next_i + min(i, n - next_i))
    
    answer += move
    return answer