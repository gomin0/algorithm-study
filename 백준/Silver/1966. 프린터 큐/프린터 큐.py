import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    count = 1
    n, idx = map(int, sys.stdin.readline().split())
    queue = deque(map(int, sys.stdin.readline().split()))
    while True:
        max_pri = max(queue)
        now = queue.popleft()
        if max_pri > now:
            queue.append(now)
            if idx == 0:
                idx = len(queue) - 1
            else:
                idx -= 1
        else:
            if idx == 0:
                print(count)
                break
            else:
                idx -= 1
            count += 1
