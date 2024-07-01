def solution(array, commands):
    answer = []
    
    for arr in range(len(commands)):
        i = commands[arr][0]
        j = commands[arr][1]
        k = commands[arr][2]
        k_nums = []
        
        for num in range(i - 1, j):
            k_nums.append(array[num])
        k_nums.sort()
        print(k_nums)
        answer.append(k_nums.pop(k - 1))
    
    return answer