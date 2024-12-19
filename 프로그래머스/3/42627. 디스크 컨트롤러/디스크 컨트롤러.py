import heapq

def solution(jobs):
    answer = 0
    
    n = len(jobs)
    current_time = 0
    jobs.sort()
    disk = []
    
    idx = 0
    while idx < n or disk:
        while idx < n and jobs[idx][0] <= current_time:
            start = jobs[idx][0]
            time = jobs[idx][1]
            heapq.heappush(disk, (time, start, idx))
            idx += 1
        if disk:
            t, s, i = heapq.heappop(disk)
            current_time += t
            answer += current_time - s
        else:
            current_time = jobs[idx][0]
        
    return answer // n