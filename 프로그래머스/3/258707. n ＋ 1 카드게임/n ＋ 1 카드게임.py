from collections import deque

def solution(coin, cards):
    n = len(cards)
    target = n+1
    hand = set(cards[:n//3])
    deck = deque(cards[n//3:])
    possible = set()
    
    def removable(a, b):
        for i in list(a):
            if target - i in b:
                a.remove(i)
                b.remove(target-i)
                return True
        return False
    
    _round = 1
    while deck:
        for i in range(2):
            possible.add(deck.popleft())
        if removable(hand, hand):
            _round += 1
        elif coin >= 1 and removable(hand, possible):
            coin -= 1
            _round += 1
        elif coin >=2 and removable(possible, possible):
            coin -= 2
            _round += 1
        else:
            break
            
    return _round