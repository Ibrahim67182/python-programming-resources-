
def func():

    
    try:
     
     x=int(input("enter num"))
     return x*x
    except:
        print("INVALID NUM")
        return -1
    
    finally:
       print("i am executed anyway i am used to close databases and files in case of exception")


y=func()
print(y)




     
