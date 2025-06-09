import heapq

def solution(operations):
    answer: list[int] = [0, 0]
    
    max_heap: list[int] = []
    min_heap: list[int] = []
    
    for op in operations:
        command: str
        num: str
        command, num = op.split()
        
        if command == 'I':
            heapq.heappush(max_heap, -int(num))
            heapq.heappush(min_heap, int(num))
        elif num == "1" and max_heap:
            min_heap.remove(-heapq.heappop(max_heap))
        elif num == "-1" and min_heap:
            max_heap.remove(-heapq.heappop(min_heap))
    
    if max_heap:
        answer[0] = -heapq.heappop(max_heap)
    if min_heap:
        answer[1] = heapq.heappop(min_heap)
    
    return answer
    