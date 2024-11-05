def solution(enroll, referral, seller, amount):
    answer = []
    
    money = {e: 0 for e in enroll}
    ref = {enroll[i]: referral[i] for i in range(len(enroll))}
    
    def distribute(name, profit):
        if profit < 1 or name == "-":
            return
        commission = profit // 10
        money[name] += profit - commission
        # 상위 추천인에게 남은 금액 배분
        distribute(ref[name], commission)
    
    for i in range(len(seller)):
        profit = amount[i] * 100
        distribute(seller[i], profit)
    
    for price in money.values():
        answer.append(price)
    return answer