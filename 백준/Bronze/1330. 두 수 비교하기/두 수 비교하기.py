#1330

A,B = map(int,input().split(' '))

if A>B:
  print('>')
elif B>A:
  print('<')
elif A==B:
  print('==')