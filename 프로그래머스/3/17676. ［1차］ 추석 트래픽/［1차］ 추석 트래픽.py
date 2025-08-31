def solution(lines):
    logs = []
    for line in lines:
        date, time, duration = line.split()
        h, m, s = time.split(":")
        end = (int(h) * 60 * 60 + int(m) * 60 + float(s)) * 1000
        duration = float(duration[:-1]) * 1000
        start = end - duration + 1
        logs.append((start, end))
    
    _max = 0
    for s, e in logs:
        for t in (s, e):
            t_end = t + 1000
            count = 0
            for ss, ee in logs:
                if ss < t_end and ee >= t:
                    count += 1
            _max = max(_max, count)
    
    return _max