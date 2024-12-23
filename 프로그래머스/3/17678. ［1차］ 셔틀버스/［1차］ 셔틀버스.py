def time_to_minute(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def minute_to_time(minute):
    h = minute // 60
    m = minute % 60
    return f"{h:02}:{m:02}"

def solution(n, t, m, timetable):
    answer = ''
    
    timetable.sort()
    
    time = 9*60
    idx = 0
    for i in range(n):
        crew = 0
        while idx < len(timetable):
            bus = time_to_minute(timetable[idx])
            if bus <= time:
                idx += 1
                crew += 1
                if crew == m:
                    break
            else:
                break
        time += t
    
    if crew < m:
        answer = minute_to_time(time - t)
    else:
        answer = minute_to_time(time_to_minute(timetable[idx-1]) - 1)
        # answer = minute_to_time(time_to_minute(timetable[-1]) - 1) 이렇게 하면 마지막 사람이 마지막 버스에 못타는 사람일 수도 있으니까 idx로 해야함
    
    return answer