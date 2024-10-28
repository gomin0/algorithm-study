import heapq

def solution(jobs):
    answer = 0
    
    jobs.sort()
    
    current_time = 0
    total_time = 0
    n = len(jobs)
    idx = 0
    
    job_heap = []
    
    while idx < n or job_heap:
        while idx < n and jobs[idx][0] <= current_time:
            heapq.heappush(job_heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1
            
        if job_heap:
            time, start_time = heapq.heappop(job_heap)
            current_time += time
            total_time += current_time - start_time
        else:
            current_time = jobs[idx][0]
    
    return total_time // n