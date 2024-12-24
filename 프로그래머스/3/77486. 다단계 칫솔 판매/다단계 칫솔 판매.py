def solution(enroll, referral, seller, amount):
    n = len(enroll)
    
    money = {e: 0 for e in enroll}
    ref = {enroll[i]: referral[i] for i in range(n)}
    
    def distribute(name, price):
        if price < 1 or name == "-":
            return
        give = price // 10
        money[name] += price - give
        distribute(ref[name], give)
        
    for i in range(len(seller)):
        price = amount[i] * 100  # 개당 100원
        distribute(seller[i], price)
        
    return [money[e] for e in enroll]