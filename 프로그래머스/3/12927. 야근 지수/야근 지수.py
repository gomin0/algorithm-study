import heapq

def solution(n, works):
    max_work = [-w for w in works]
    heapq.heapify(max_work)
    for i in range(n):
        if not max_work:
            break
        work = heapq.heappop(max_work)
        work = -work
        if work > 1:
            heapq.heappush(max_work, -work + 1)
    answer = 0
    for w in max_work:
        answer += w*w
    return answer