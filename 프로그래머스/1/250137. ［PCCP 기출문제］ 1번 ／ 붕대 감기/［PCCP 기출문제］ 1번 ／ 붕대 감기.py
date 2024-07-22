def solution(bandage, health, attacks):
    answer = 0
    last_attack = attacks[-1][0]
    now_health = health
    success_count = 0
    
    for i in range(1, last_attack + 1):
        attacked = False
        
        for j in range(len(attacks)):
            if i == attacks[j][0]:
                now_health -= attacks[j][1]
                success_count = 0
                attacked = True
                if now_health <= 0:
                    return -1
        
        if not attacked:
            success_count += 1
            now_health += bandage[1]
            if success_count == bandage[0]:
                now_health += bandage[2]
                success_count = 0
            if now_health > health:
                now_health = health
    
    return now_health