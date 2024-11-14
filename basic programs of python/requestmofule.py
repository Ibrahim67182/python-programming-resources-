import requests
from bs4 import BeautifulSoup


url= "https://www.w3schools.com/python/numpy/numpy_data_types.asp"

r= requests.get(url)

soup=BeautifulSoup(r.text,'html.parser')


h2_tags= soup.find_all("h2")

for h2 in h2_tags:
    p_tag= h2.find_next_sibling("p")

    if p_tag:
        print(f"paragraph under the tag {h2.get_text()} is :  {p_tag.get_text()}")


# in this code we are scraping all the h2 headings and their line paragraphs p  using html parser by beautiful soup 
