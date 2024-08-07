def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        price = prices[i]
        count = -1
        for j in range(i, len(prices)):
            if price <= prices[j]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    return answer