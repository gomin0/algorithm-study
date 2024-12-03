import heapq

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    
    for operation in operations:
        op, n = operation.split()
        n = int(n)
        if op == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
        else:
            if n == 1 and max_heap:
                min_heap.remove(-heapq.heappop(max_heap))
            elif n == -1 and min_heap:
                max_heap.remove(-heapq.heappop(min_heap))
    
    if min_heap and max_heap:
        return [-max_heap[0], min_heap[0]]
    else:
        return [0, 0]