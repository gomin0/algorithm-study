def solution(elements):
    answer: set[int] = set()
    length: int = len(elements)
    elements *= 2
    
    # 누적합 배열
    prefix: list[int] = [0] * (length * 2 + 1)
    for i in range(1, length * 2):
        prefix[i] = prefix[i-1] + elements[i]
    
    for start in range(length):
        for size in range(1, length + 1):
            end: int = start + size
            total_sum: int = prefix[end] - prefix[start]
            answer.add(total_sum)
    
    return len(answer)