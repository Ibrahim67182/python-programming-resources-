import os

def clear_the_clutter(dir):
        
        files= os.listdir(dir)
        i=0
        tmp=files[0]
        ext=tmp[-4:len(tmp)]

        for file in files:
               if(file.endswith(ext)):
                       os.rename(f"{dir}/{file}",f"{i}{ext}")
                       i+=1
                
           
            
        

        
               
                
     
dire="xpics"

clear_the_clutter(dire)


