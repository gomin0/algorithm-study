from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer: list[int] = []
    
    multi_level: defaultdict[str, str] = defaultdict(str)
    total_money: defaultdict[str, int] = defaultdict(int)
    for i in range(len(enroll)):
        multi_level[enroll[i]] = referral[i]
    
    for s, a in zip(seller, amount):
        money: int = a * 100
        current: str = s
        
        while True:
            give = money // 10
            keep = money - give
            total_money[current] += keep
            
            if multi_level[current] == "-" or give < 1:
                break
            current = multi_level[current]
            money = give
    
    for person in enroll:
        answer.append(total_money[person])
    
    return answer
