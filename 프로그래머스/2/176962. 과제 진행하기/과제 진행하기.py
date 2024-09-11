def solution(plans):
    answer = []
    
    current_time = 0
    working = []
    
    # 시간 순 정렬
    plans = sorted(plans, key=lambda x: int(x[1].split(":")[0]) * 60 + int(x[1].split(":")[1]))
    
    for plan in plans:
        name = plan[0]
        hour, minute = map(int, plan[1].split(":"))
        start_time = hour * 60 + minute
        time = int(plan[2])
        
        # 과제 남아있고 아직 시작 시간 안됐으면 남은 과제 처리
        while working and current_time < start_time:
            work_name, work_time = working.pop() # 가장 최근 멈춘 과제 이름, 남은 시간
            
            # 새 과제 시작전 끝났다
            if current_time + work_time <= start_time:
                answer.append(work_name)
                current_time += work_time
            else:  # 새 과제 시작 전 못 끝냈다.
                working.append((work_name, work_time - (start_time - current_time)))
                current_time = start_time
                break
        
        # 새 과제 시작
        current_time = start_time
        working.append((name, time))
        
    # 새 과제 다 돌았는데 아직 남은 과제 있으면
    while working:
        answer.append(working.pop()[0])
            
            
    return answer