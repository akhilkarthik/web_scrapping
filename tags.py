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

# print(soup.get_text()) # for getting all the texts from page

# Find the table element, if it exists
table = soup.find("table")

if table is not None:
    # Extract data and organize it into a tabular format
    data = []

    # Extract data from table rows
    rows = table.find_all("tr")

    for row in rows:
        cols = row.find_all("td")
        cols = [col.text.strip() for col in cols]
        data.append(cols)
else:
    print("Table not found on the page")  # here we dont have any tables