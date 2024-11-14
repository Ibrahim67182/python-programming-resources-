
n=6
sp =n
x=n
y=1
flag =0
for i in range(n):
  for j in range(sp):
     print(" ",end="")

  sp+=1

  for k in range(x,0,-1):
     

     if(y<=9):
       print(y,end=" ")
       y+=1
     else:
        if(flag==0):
           print(0,end=" ")
           flag=1
        elif(flag==1):
           print(9,end=" ") 
           flag=0 

  x-=1
  print()

h=2
fc=1
y-=1
for a in range (2,n+1):
   fc+=a

for l in range(n-1):
   for c in range(sp-2):
      print(" ",end="")
   sp-=1

   for s in range(h):
      
       if(fc<11 and y>0):
         print(y,end=" ")
         y-=1
       elif(flag==0):
        print(0,end=" ")
        flag=1

       elif(flag==1):
        print(9,end=" ")
        flag=0
       
       fc-=1
   h+=1  
      
   print()

