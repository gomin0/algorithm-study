def solution(n, left, right):
    answer = []

    for k in range(left, right + 1):
        i = k // n
        j = k % n
        answer.append(max(i, j) + 1)
    
    return answer


# def solution(n, left, right):
#     answer = []
#     array = [[0] * n for _ in range(n)]
    
#     for i in range(n):
#         for j in range(n):
#             array[i][j] = max(i, j) + 1

#     for k in range(left, right + 1):
#         answer.append(array[k//n][k%n])
#     return answer

# def solution(n, left, right):
#     array = ""
#     for i in range(n):
#         array += str(i+1)
#     num = int(array)

#     for j in range(n-1):
#         num += sum(10**(n-1-k) for k in range(j+1))
#         array += str(num)
    
#     number_list = [int(char) for char in array]
    
#     return number_list[left:right+1]