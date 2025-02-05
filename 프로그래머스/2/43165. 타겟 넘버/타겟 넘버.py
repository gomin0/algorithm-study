def solution(numbers, target):
    answer = 0
    
    n = len(numbers)
    
    def dfs(index, current):
        if index == n:
            if current == target:
                return 1
            else:
                return 0
        return dfs(index+1, current + numbers[index]) + dfs(index+1, current - numbers[index])
    
    return dfs(0, 0)