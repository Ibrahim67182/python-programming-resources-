import requests

api_key="586101545d2d46908e2da0ea5376bf8e"


url ="https://newsapi.org/v2/top-headlines?country=us&apiKey=586101545d2d46908e2da0ea5376bf8e"



parameters= {
 
  'country': 'us',

 'category': 'technology',

 'apikey':api_key

}

#fethcing all top news in us related to technology using our own api key at apinews 

r=requests.get(url,params=parameters)

if r.status_code==200:      #if request is successful from web 
    news=r.json()           #convert the data of web into json file 

    articles=news.get('articles')       #fetch articles from data which is a list of dictionaries 

    for article in articles:                        #for each article print its relevant values from keys like title ,author ,etc
      print(f"source :{article['source']['name']}")
      print(f"title : {article['title']}")
      print(f"author name : {article['author']}")
      print(f"url of article : {article['url']}")
      print(f"publish date : {article['publishedAt']}")
else :
   print(f"error fetching the news : {r.status_code}")




