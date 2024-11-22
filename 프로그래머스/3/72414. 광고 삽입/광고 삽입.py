# 누적합, 시작 시간 부터 끝 시간 - 1
def solution(play_time, adv_time, logs):
    answer = ''
    
    def time_to_seconds(time):
        h, m, s = map(int, time.split(":"))
        return h * 3600 + m * 60 + s
    
    def seconds_to_time(seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        
        return f"{h:02}:{m:02}:{s:02}"
    
    play_seconds = time_to_seconds(play_time)
    adv_seconds = time_to_seconds(adv_time)
    
    viewers = [0] * (play_seconds + 1)  # 누적합 배열
    
    for log in logs:
        start, end = log.split("-")
        start_seconds = time_to_seconds(start)
        end_seconds = time_to_seconds(end)
        viewers[start_seconds] += 1
        viewers[end_seconds] -= 1
    
    # 누적 합 계산
    for i in range(1, play_seconds + 1):
        viewers[i] += viewers[i-1]
    
    # 누적 시청 시간 계산
    for i in range(1, play_seconds + 1):
        viewers[i] += viewers[i-1]
    
    max_view_time = 0
    max_start_time = 0
    
    for start_time in range(play_seconds - adv_seconds + 1):
        end_time = start_time + adv_seconds - 1
        current_view_time = viewers[end_time] - (viewers[start_time-1] if start_time > 0 else 0)
        if current_view_time > max_view_time:
            max_view_time = current_view_time
            max_start_time = start_time
    
    return seconds_to_time(max_start_time)