def solution(numbers):
    sums = set()  # 중복 방지 집합
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            sums.add(numbers[i] + numbers[j])
    answer = sorted(sums)
    return answer