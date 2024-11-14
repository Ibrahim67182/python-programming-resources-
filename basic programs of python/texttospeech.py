from gtts import gTTS
import os





lis= ["ibrahim","khan","bilal"]

language= "en"
i=1

for item in lis:
    
    mytext="shout out to "+ item
    myvoice= gTTS(text=mytext ,lang=language,slow=False)
    myvoice.save(f"mysound{i}.mp3")
    i+=1
    os.system(f"start mysound{i}.mp3")


    
