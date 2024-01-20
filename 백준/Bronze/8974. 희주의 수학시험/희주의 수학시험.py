lst = []

for x in range(1,1001):
  for y in range(1, x+1):
    lst.append(x)

A,B = map(int,input().split()) #1 3
print(sum(lst[A-1:B])) #lst[start : end-1]. lst[1:3] =>1~2