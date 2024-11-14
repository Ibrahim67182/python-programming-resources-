import threading
import time

def func(sec):
  time.sleep(sec)

  print(f"sleeping for {sec} seconds ")


tim1=time.time()
func(3)
func(4)
func(6)
tim2=time.time()

print(tim2-tim1)

tim3=time.time()
t1=threading.Thread(target=func,args=[3])
t2=threading.Thread(target=func,args=[4])
t3=threading.Thread(target=func,args=[6])
   
t1.start()
t2.start()
t3.start()   

tim4=time.time()

print(tim4-tim3)
