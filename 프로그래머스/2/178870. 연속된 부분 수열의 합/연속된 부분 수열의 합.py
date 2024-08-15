def solution(sequence, k):
    answer = []
    
    sum_list = []
    
    # for i in range(len(sequence)):
    #     sum_num = 0
    #     for j in range(i, len(sequence)):
    #         sum_num += sequence[j]
    #         if sum_num == k:
    #             sum_list.append((i, j))
    #             break
    start, end = 0, 0
    sum_num = 0
    while end < len(sequence):
        sum_num += sequence[end]
        while sum_num >= k:
            if sum_num == k:
                sum_list.append((start, end))
            
            sum_num -= sequence[start]
            start += 1
        
        end += 1
    
    a, b = sum_list[0]
    length = b-a
    if len(sum_list) > 1:
        for k in range(1, len(sum_list)):
            c, d = sum_list[k]
            if length > d - c:
                a, b = c, d
                length = d - c
    
    return [a, b]