n = int(input())
number = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())


def dfs(i, current, add, sub, mul, div, max_value, min_value):
    if i == n:
        return max(max_value, current), min(min_value, current)

    results = []

    if add > 0:
        results.append(dfs(i + 1, current + number[i], add - 1, sub, mul, div, max_value, min_value))
    if sub > 0:
        results.append(dfs(i + 1, current - number[i], add, sub - 1, mul, div, max_value, min_value))
    if mul > 0:
        results.append(dfs(i + 1, current * number[i], add, sub, mul - 1, div, max_value, min_value))
    if div > 0:
        if current < 0:
            results.append(dfs(i + 1, -(-current // number[i]), add, sub, mul, div - 1, max_value, min_value))
        else:
            results.append(dfs(i + 1, current // number[i], add, sub, mul, div - 1, max_value, min_value))

    for result in results:
        max_value = max(max_value, result[0])
        min_value = min(min_value, result[1])

    return max_value, min_value


max_result, min_result = dfs(1, number[0], add, sub, mul, div, -float('inf'), float('inf'))
print(max_result)
print(min_result)