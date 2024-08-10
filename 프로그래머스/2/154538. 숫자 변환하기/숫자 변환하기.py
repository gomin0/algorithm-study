def solution(x, y, n):
    
    if x == y:
        return 0
    
    queue = [(x, 0)]
    visited = set()
    
    while queue:
        current_value, count = queue.pop(0)
        for next_value in (current_value * 2, current_value * 3, current_value + n):
            if next_value == y:
                return count + 1
            
            if next_value < y and next_value not in visited:
                visited.add(next_value)
                queue.append((next_value, count + 1))
    
    return -1