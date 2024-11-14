from multiprocessing import Process
import requests

url="https://picsum.photos/2000/3000"


def download_images(url,name):

    print(f"start downloading image {name}") 


    r=requests.get(url)
    open(f"random_images/{name}file.jpg","wb").write(r.content)


    print(f"finish downloading image {name}") 


#rather we download one image at a time we use multiporcessing module to achieve this task at much higher performance


if __name__=='__main__':
 processes=[]
 for i in range(6):
   p=Process(target=download_images,  args=(url,i+1))
   p.start()
   processes.append(p)


 for p in processes:
   p.join()




