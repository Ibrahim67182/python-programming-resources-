
def pyramid(n):
  space=n
  x=1
  for i in range(n):
     for j in range(space):
        print(" ",end="")
     for k in range(x):
        print("X",end="")
     x+=2
     space-=1   
     print()



pyramid(7)


