S1, S2, S3, S4 = map(int, input().split())
T1, T2, T3, T4 = map(int, input().split())

S = sum([S1, S2, S3, S4])
T = sum([T1, T2, T3, T4])

if S >T:
  print(S)
elif T>S:
  print(T)
else:
  print(S)