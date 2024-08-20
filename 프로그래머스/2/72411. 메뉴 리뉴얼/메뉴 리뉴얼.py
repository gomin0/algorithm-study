import itertools

def solution(orders, course):
    answer = []
    
    for c in course:
        order_comb = {}
        for order in orders:
            for comb in itertools.combinations(sorted(order), c):
                sorted_comb = ''.join(comb)
                if sorted_comb in order_comb:
                    order_comb[sorted_comb] += 1
                else:
                    order_comb[sorted_comb] = 1
        
        if order_comb:
            max_count = max(order_comb.values())
            if max_count >= 2:
                answer += [k for k, v in order_comb.items() if v == max_count]
                    
    return sorted(answer)