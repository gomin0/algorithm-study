from itertools import combinations, product
from bisect import bisect_left, bisect_right

def solution(dice):
    n = len(dice)
    half = n // 2
    best_prob = -1
    best_choice = []
    
    for comb in combinations(range(n), half):
        a_dice = [dice[i] for i in comb]
        b_dice = [dice[i] for i in range(n) if i not in comb]
        a_sum = [sum(p) for p in product(*a_dice)]
        b_sum = [sum(p) for p in product(*b_dice)]
        a_sum.sort()
        b_sum.sort()
        
        win = 0
        total = len(a_sum) * len(b_sum)
        
        for a in a_sum:
            win += bisect_left(b_sum, a)
        prob = win / total
        if prob > best_prob:
            best_prob = prob
            best_choice = [i+1 for i in comb]
    
    return best_choice