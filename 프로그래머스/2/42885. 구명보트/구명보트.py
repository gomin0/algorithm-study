def solution(people, limit):
    boat: int = 0
    people.sort()
    i: int = 0
    j: int = len(people) - 1
    
    while i <= j:
        if limit - people[j] >= people[i]:
            i += 1
        j -= 1
        boat += 1
    return boat