import sys

n = int(sys.stdin.readline().strip())
sang = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
card = list(map(int, sys.stdin.readline().split()))

for i in range(len(card)):
    if card[i] in sang:
        card[i] = '1'
    else:
        card[i] = '0'

print(" ".join(card))