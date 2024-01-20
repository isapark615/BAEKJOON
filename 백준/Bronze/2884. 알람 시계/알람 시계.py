H,M = map(int,input().split())
if M>=45:
  print(H,M-45)
elif(M-45<0):
  M = 60+(M-45)   # "negative minutes" minused from H
  H -= 1
  if(H<0):
    H = 23
  print(H,M)