import heapq

def solution(n, works):
    answer: int = 0
    works: list[int] = [-work for work in works]
    heapq.heapify(works)
    
    while n > 0:
        if not works:
            break
        num: int = heapq.heappop(works)
        num += 1
        if num < 0:
            heapq.heappush(works, num)
        n -= 1
    
    for work in works:
        answer += work*work
    return answer