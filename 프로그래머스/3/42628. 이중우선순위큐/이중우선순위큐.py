import heapq

def solution(operations):
    answer = []
    
    min_heap = []
    max_heap = []
    
    for operation in operations:
        op, val = operation.split()
        val = int(val)
        
        if op == 'I':
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -val)
        else:
            if val == 1 and max_heap:
                min_heap.remove(-heapq.heappop(max_heap))
            elif val == -1 and min_heap:
                max_heap.remove(-heapq.heappop(min_heap))
    
    if min_heap and max_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]