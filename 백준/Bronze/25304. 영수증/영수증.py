x = int(input())
n = int(input())
t = 0

for i in range(n):
  a,b = map(int, input().split())
  t = a*b + t

if t == x:
  print('Yes')
else:
  print('No')