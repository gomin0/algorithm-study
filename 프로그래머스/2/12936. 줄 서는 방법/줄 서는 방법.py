# k번째 순열을 직접 계산
def solution(n, k):
    people = list(range(1, n+1))
    answer = []
    k -= 1  # 0-based index로 변환
    
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n-1)
    
    for i in range(n, 0, -1):
        fact = factorial(i - 1) # 첫 자리 경우 수
        index = k // fact
        k %= fact
        
        answer.append(people[index])
        people.pop(index)
    
    return answer


# 모든 경우 다 구하니까 시간초과
# import itertools

# def solution(n, k):
#     answer = []
    
#     people = []
#     for i in range(n):
#         people.append(i+1)
    
#     people_list = list(itertools.permutations(people))
    
#     return people_list[k-1]