
import random 
game=       [['D','W','L'],
             ['L','D','W'],
             ['W','L','D']]

points= 0 

condition = True


while condition:
       try: 
        num = int(input("enter any number b/w 0 and 2"))
       except Exception as e:
           print(e)

       comp = random.randint(0,2)
       
       print("you got ",num ," comp got ",comp)

       if(game[num][comp]=='D'):
           print("Game DRAWS","  points : ",points)
           

       elif(game[num][comp]=='L'):
           points-=10
           print("You LOSE!!","  points : ",points)
           
       elif(game[num][comp]=='W'):
           points+=10
           print("You WIN","  points : ",points)
           
        
       an=(input("you want to play again ?? press Y/y"))
       if(an=='y'or an=='Y'):
           condition =True
       else:
           condition = False    
           
              
      
