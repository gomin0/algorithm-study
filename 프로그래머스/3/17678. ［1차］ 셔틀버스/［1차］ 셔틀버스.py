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
    
    return answer