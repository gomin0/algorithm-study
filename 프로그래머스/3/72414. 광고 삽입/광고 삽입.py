def solution(play_time, adv_time, logs) -> int:
    def time_to_seconds(time: str) -> int:
        h: int
        m: int
        s: int
        h, m, s = map(int, time.split(":"))
        return h * 3600 + m * 60 + s
    
    def seconds_to_time(seconds):
        h: int = seconds // 3600
        m: int = (seconds % 3600) // 60
        s: int = seconds % 60
        return f"{h:02}:{m:02}:{s:02}"
    
    play: int = time_to_seconds(play_time)
    adv: int = time_to_seconds(adv_time)
    viewers = [0] * (play + 1)
    
    for log in logs:
        start_time: str
        end_time: str
        start_time, end_time = log.split("-")
        start: int = time_to_seconds(start_time)
        end: int = time_to_seconds(end_time)
        viewers[start] += 1
        viewers[end] -= 1
        
    for i in range(1, play + 1):
        viewers[i] += viewers[i-1]
    for i in range(1, play + 1):
        viewers[i] += viewers[i-1]
    
    max_view: int = 0
    max_start: int = 0
    
    for start_time in range(play - adv + 1):
        end_time: int = start_time + adv - 1
        current_view: int = viewers[end_time] - (viewers[start_time-1] if start_time > 0 else 0)
        if current_view > max_view:
            max_view = current_view
            max_start = start_time
    
    return seconds_to_time(max_start)