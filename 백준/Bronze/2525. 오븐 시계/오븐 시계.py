A,B = map(int, input().split())
C = int(input())

if B+C<60:
  print(A,B+C)
else:
  H = (B+C)//60
  M = (B+C)%60
  
  if A+H>23:
    print(A+H-24,M)
  else:
    print(A+H,M)
    