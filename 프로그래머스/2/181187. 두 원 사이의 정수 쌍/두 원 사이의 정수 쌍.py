def count_points(r):
    count = 0
    on_circle = 0
    for x in range(r + 1):
        y = int((r * r - x * x) ** 0.5)  # 피타고라스 -> x에 대해 가능한 최대 y
        count += y + 1
        if x * x + y * y == r * r:
            on_circle += 1
    return count * 4 - 4 * r - 3, on_circle*4 - 4  # 4사분면 이라 * 4, x|y축 중복 -4r, 원점 중복 -3

def solution(r1, r2):
    r1_count, r1_on = count_points(r1)[0], count_points(r1)[1]
    return count_points(r2)[0] - r1_count + r1_on