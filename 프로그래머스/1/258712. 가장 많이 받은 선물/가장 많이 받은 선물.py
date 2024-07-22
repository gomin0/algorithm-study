def solution(friends, gifts):
    give_gift = {user: [] for user in friends}
    get_gift = {user: [] for user in friends}
    
    for i in gifts:
        give, get = i.split(" ")
        give_gift[give].append(get)
        get_gift[get].append(give)

    # 선물 지수
    gift_level = {}
    
    for j in friends:
        give_count = len(give_gift[j])
        get_count = len(get_gift[j])
        gift_level[j] = give_count - get_count
    
    next_gift = {user: 0 for user in friends}
        
    for i, giver in enumerate(friends):
        for getter in friends[i+1:]:
            give_to = give_gift[giver].count(getter)
            get_to = give_gift[getter].count(giver)
        
            if give_to > get_to:
                next_gift[giver] += 1
            elif give_to < get_to:
                next_gift[getter] += 1
            else:
                if gift_level[giver] > gift_level[getter]:
                    next_gift[giver] += 1
                elif gift_level[giver] < gift_level[getter]:
                    next_gift[getter] += 1
    
    answer = max(next_gift.values())
    
    return answer