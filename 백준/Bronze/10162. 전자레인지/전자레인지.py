T=int(input())

A = 300
B = 60
C = 10

if T%10 != 0:
  print(-1)

else:
  Abutton = T//A
  Bbutton = (T%A)//B
  Cbutton = ((T%A)%B)//C

  print(Abutton,Bbutton,Cbutton)