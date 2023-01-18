tc = int(input())

for i in range(tc):
    num, arr = input().split()
    for j in arr:
        print(j*int(num), end='')
    print()