import itertools

def solution(expression):
    answer = 0
    
    num = []
    operator = []
    
    n = ''
    for i in expression:
        
        if i.isdigit():
            n += i
        else:
            num.append(int(n))
            operator.append(i)
            n = ''
    num.append(int(n)) # 마지막 숫자
    
    operator_priority = itertools.permutations(['*', '+', '-'])
    
    def calculate(nums, ops, order):
        nums = nums[:]
        ops = ops[:]
        for op in order:
            i = 0
            while i < len(ops):
                if ops[i] == op:
                    result = 0
                    if op == '*':
                        nums[i] = nums[i] * nums[i+1]
                    elif op == '+':
                        nums[i] = nums[i] + nums[i+1]
                    else:
                        nums[i] = nums[i] - nums[i+1]
                    nums.pop(i+1)
                    ops.pop(i)
                else:
                    i += 1      
        return abs(nums[0])
    
    for order in operator_priority:
        result = calculate(num, operator, order)
        answer = max(answer, result)
    
    return answer