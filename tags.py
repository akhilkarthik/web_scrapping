import requests
from bs4 import BeautifulSoup  # importing Beautifulsoup 

with open ("E:\\vs code\\beautifulsoup\\data\\times.html","r",encoding="utf-8") as file:
    html_doc=file.read()               # opening the times.html file as html_doc

                             
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/  - for more resources of Beautifulsoup


soup = BeautifulSoup(html_doc, 'html.parser')   

#print("\n" ,soup.title.string)               # to get the title of the website
#print("\n",soup.title.parent.string)

#for link in soup.find_all('a'):  # to get all the links using iteration 
    #print(link.get('href'))

# print(soup.a)
#print(soup.find_all("a"))

print(soup.get_text()) # for getting all the texts from page