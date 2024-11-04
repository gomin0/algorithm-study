def time_to_minute(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)

def minute_to_time(minute):
    h = str(minute // 60)
    m = str(minute % 60)
    h = h.zfill(2)
    m = m.zfill(2)
    time = ""
    time += h + ':' + m
    return time

def solution(n, t, m, timetable):
    answer = ''
    
    sorted_arrive = sorted([time_to_minute(time) for time in timetable])
    bus_time = [9*60 + t * i for i in range(n)]
    
    idx = 0
    for bt in bus_time:
        count = 0
        
        while idx < len(sorted_arrive) and sorted_arrive[idx] <= bt and count < m:
            idx += 1
            count += 1
        
        if bt == bus_time[-1]:  # 마지막 버스이면
            if count < m:
                return minute_to_time(bt)
            else:
                return minute_to_time(sorted_arrive[idx-1] - 1)  # 마지막 사람보다 1분 빨리 도착해야함