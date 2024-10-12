def solution(arr):
    
    n = (len(arr) + 1) // 2  # 숫자 개수
    
    nums = [int(arr[i]) for i in range(0, len(arr), 2)]
    ops = [arr[i] for i in range(1, len(arr), 2)]
    
    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp_max[i][i] = nums[i]
        dp_min[i][i] = nums[i]
        
    for length in range(1, n):  # 구간의 길이
        for i in range(n-length):
            j = i + length
            
            dp_max[i][j] = float('-inf')
            dp_min[i][j] = float('inf')
            
            for k in range(i, j):
                if ops[k] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+1][j])
                elif ops[k] == '-':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+1][j])
    
    return dp_max[0][n-1]