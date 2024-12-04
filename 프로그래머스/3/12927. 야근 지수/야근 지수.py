import heapq

def solution(n, works):
    answer = 0
    
    max_heap = [-x for x in works]
    heapq.heapify(max_heap)
    
    for i in range(n):
        if max_heap:
            max_value = heapq.heappop(max_heap)
            if max_value + 1 < 0:
                heapq.heappush(max_heap, max_value + 1)
    
    for i in max_heap:
        answer += i*i
    
    return answer