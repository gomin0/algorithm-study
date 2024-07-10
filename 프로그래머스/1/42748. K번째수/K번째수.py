def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        k_nums = []
        
        for num in range(commands[i][0] - 1, commands[i][1]):
            k_nums.append(array[num])
        k_nums.sort()
        print(k_nums)
        answer.append(k_nums.pop(commands[i][2] - 1))
    
    return answer