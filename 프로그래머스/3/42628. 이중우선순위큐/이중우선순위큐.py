import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    for op in operations:
        command, num = op.split()
        num = int(num)
        if command == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if not min_heap:
                continue
            if num == 1:
                n = -heapq.heappop(max_heap)
                min_heap.remove(n)
            else:
                n = -heapq.heappop(min_heap)
                max_heap.remove(n)
    min_num = 0
    max_num = 0
    if min_heap:
        min_num = heapq.heappop(min_heap)
        max_num = -heapq.heappop(max_heap)

    return [max_num, min_num]