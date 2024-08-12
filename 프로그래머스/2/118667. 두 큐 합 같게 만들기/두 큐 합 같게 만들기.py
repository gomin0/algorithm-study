from collections import deque

def solution(queue1, queue2):
    answer = 0
    q_sum = sum(queue1) + sum(queue2)
    if not q_sum % 2 == 0:
        return -1
    goal = (sum(queue1) + sum(queue2)) // 2
    
    max_change = (len(queue1) + len(queue2)) * 2
    current_sum = sum(queue1)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # while 문안에서 계속 sum으로 구하기 보다 +-로 갱신
    while current_sum != goal:
        
        if answer > max_change:
            return -1
        
        if current_sum > goal:
            pop_num = queue1.popleft()
            queue2.append(pop_num)
            current_sum -= pop_num
            answer += 1
        elif current_sum < goal:
            pop_num = queue2.popleft()
            queue1.append(pop_num)
            current_sum += pop_num
            answer += 1
    
    return answer