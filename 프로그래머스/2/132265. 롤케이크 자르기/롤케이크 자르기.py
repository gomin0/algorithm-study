#O(n) 이 되게 풀어야 함
def solution(topping):
    answer = 0
    length = len(topping)
    lcake = set()
    lcount = [0] * length
    rcake = set()
    rcount = [0] * length
    
    for i in range(length):
        lcake.add(topping[i])
        lcount[i] = len(lcake)
        
    for j in range(length-1, -1, -1):
        rcake.add(topping[j])
        rcount[j] = len(rcake)
    
    for k in range(1, length):
        if lcount[k - 1] == rcount[k]:
            answer += 1
    
    return answer


# 시간 초과 O(n^2)
# def solution(topping):
#     answer = 0
    
#     for i in range(1, len(topping) - 1):
#         if len(set(topping[:i])) == len(set(topping[i:])):
#             answer += 1
    
#     return answer

# 살짝 빨라짐 for문 안에 pop때문에 O(n^2)
# def solution(topping):
#     answer = 0
#     cake = set()
#     for _ in range(len(topping)):
#         cake.add(topping.pop(0))
#         if len(cake) == len(set(topping)):
#             answer += 1
    
#     return answer