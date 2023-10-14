import requests

import requests



# creating a function to save webhtml text
def fetchandsavetofile(url,path):                        # creating a function for saving the text as a file from wsbsite "url"= link, path="file path"
    r=requests.get(url)                                       # fetching url using the reqquests
    with open (path,"w",encoding="utf-8") as file:        # opening the file path as write mode we need to specify the utf code else show error
        file.write(r.text)                                # writing the text content from website to file 





url  = "https://timesofindia.indiatimes.com/city/mumbai" # url of times of india news page

fetchandsavetofile(url,"data/times.html")         # calling the function And giving file name as "times.html"