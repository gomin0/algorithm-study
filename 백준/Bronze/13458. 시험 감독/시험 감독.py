n = int(input())

people = list(map(int, input().split()))
b, c = map(int, input().split())

answer = n

for i in range(n):
    people[i] -= b
    if people[i] > 0:
        if people[i] % c == 0:
            answer += people[i] // c
        else:
            answer += people[i] // c + 1

print(answer)