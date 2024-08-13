# 4칸 내려가 -> 3칸 오른쪽 -> 2칸 대간선 왼 -> 1칸 내려가
# 5칸 내려가 -> 4칸 오른쪽 -> 3칸 대각선 위 -> 2칸 내려가 -> 1칸 오른쪽
# 왜안올라가
def solution(n):
    answer = []
    
    max_value = n * (n+1) // 2
    snail = [[0] * i for i in range(1, n + 1)]
    direction = ["down", "right", "up"]
    d = 0
    
    num = 1
    x, y = 0, 0
    change = n
    while num <= max_value:
        
        for i in range(change):
            # print('x, y = ', x, y)
            snail[x][y] = num
            # print('snail[x][y] = ', snail[x][y])
            num += 1
            if i < change - 1:
                if direction[d] == "down":
                    x += 1
                elif direction[d] == "right":
                    y += 1
                else:
                    x -= 1
                    y -= 1
                    
        d = (d + 1) % 3
        
        if direction[d] == "down":
            x += 1
        elif direction[d] == "right":
            y += 1
        elif direction[d] == "up":
            x -= 1
            y -= 1
        # print("change")
        change -= 1
        
    # print(snail)
    
    for number in snail:
        answer.extend(number)
    
    return answer