def solution(weights):
    answer = 0
    
    max_value = max(weights) * 4
    count = [0] * (max_value + 1)
    
    weight_dict = {}
    for weight in weights:
        if weight in weight_dict:
            weight_dict[weight] += 1
        else:
            weight_dict[weight] = 1
    for value in weight_dict.values():
        if value > 1:
            answer += value * (value-1) // 2 # 같은 값인 경우 처리
    
    for w in weight_dict:
        for ratio in [2/3, 2/4, 3/4]:
            other_weight = w * ratio
            if other_weight in weight_dict:
                answer += weight_dict[w] * weight_dict[other_weight]
    
    return answer