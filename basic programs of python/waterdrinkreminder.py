
from plyer import notification
import time
import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
  notification.notify(
    title= "Water Drink reminder",
    message="Its time to get a break to drink water and get yourself hydrated !!!",
    app_name="Water Drink APP",
    timeout=10
     )
   
  mytext= "Its time to drink some water"
  speaker.speak(mytext)
 
  time.sleep(10)

  
