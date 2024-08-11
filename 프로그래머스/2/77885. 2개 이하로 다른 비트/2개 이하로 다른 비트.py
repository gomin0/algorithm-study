# 가장 오른쪽에 처음으로 나오는 0을 1으로 바꾸고
# 그 바로 오른쪽 자리를 0으로 바꾸기
def solution(numbers):
    answer = []
    
    for num in numbers:
        # num이 짝수면 그냥 +1
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            bin_num = list(bin(num)[2:])
            
            if '0' not in bin_num:
                bin_num.insert(0, '0')
            
            for i in range(len(bin_num) - 1, -1 , -1):
                if bin_num[i] == '0':
                    bin_num[i] = '1'
                    bin_num[i+1] = '0'
                    break
            new_num = ''.join(bin_num)
            answer.append(int(new_num, 2))
    return answer


# 시간 초과
# def solution(numbers):
#     answer = []
    
#     for i in numbers:
#         num = i
#         while True:
#             num += 1
#             count = bin(i^num)[2:].count('1')
#             if 1 <= count <= 2:
#                 answer.append(num)
#                 break
        
#     return answer