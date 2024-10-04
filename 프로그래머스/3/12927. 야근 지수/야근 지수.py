import heapq

def solution(n, works):
    
    answer = 0
    
    if sum(works) < n:
        return 0
    
    max_heap = [-x for x in works]
    heapq.heapify(max_heap)
    
    while n > 0:
        max_work = heapq.heappop(max_heap)
        if max_work >= 0:
            break
        max_work += 1
        n -= 1
        heapq.heappush(max_heap, max_work)
        
    for i in max_heap:
        answer += i*i
    
    return answer