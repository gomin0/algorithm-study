def solution(n, lost, reserve):
    count = 0
    
    clothes = [1] * n
    for i in lost:
        clothes[i - 1] -= 1
    for j in reserve:
        clothes[j - 1] += 1
    
    for k in range(n):
        if clothes[k] == 1 or clothes[k] == 2:
            count += 1
        
        if clothes[k] == 0:
            if k > 0 and clothes[k - 1] == 2:
                clothes[k] = 1
                clothes[k - 1] = 1
                count += 1
            elif k < n - 1 and clothes[k + 1] == 2:
                clothes[k] = 1
                clothes[k + 1] = 1
                count += 1
                
    return count