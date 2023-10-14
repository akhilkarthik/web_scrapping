

Scrapping Times of india website with python and BeautifulSoup

    url  = "https://timesofindia.indiatimes.com/city/mumbai" # url of times of india news page


    after fetching the file use "Format Document" on right click  to format the html file


    print("\n" ,soup.title.string)               # to get the title of the website
    #print("\n",soup.title.parent.string)

    for link in soup.find_all('a'):              # to get all the links using iteration 
    print(link.get('href'))



    print(soup.get_text())      # for getting all the texts from page