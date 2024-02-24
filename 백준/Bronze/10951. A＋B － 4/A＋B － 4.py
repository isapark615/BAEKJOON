while(True):
  try:
    A,B = map(int,input().split(' '))
    print(A+B)
  except: #run if the code in the try part is an error
    break