word = input().upper()
slist = list(set(word))

cnt = []
for i in slist:
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(slist[(cnt.index(max(cnt)))])