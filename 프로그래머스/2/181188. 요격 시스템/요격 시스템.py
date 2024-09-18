def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x: x[1])
    bomb = -1  # 요격 포인트
    
    for start, end in targets:
        if start > bomb:  # 마지막 요격 포인트보다 start가 크면 무조건 하나는 쏴야함
            answer += 1
            bomb = end - 0.1
    
    return answer