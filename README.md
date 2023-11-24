The Web Scraping Project is a simple yet powerful script that utilizes the requests library in Python to fetch the HTML content of a specified URL. The script is designed to save this content into a local file, providing an efficient way to gather and store web data for further analysis or archival purposes.

Scrapping Times of india website with python and BeautifulSoup

    url  = "https://timesofindia.indiatimes.com/city/mumbai" # url of times of india news page


    after fetching the file use "Format Document" on right click  to format the html file


    print("\n" ,soup.title.string)               # to get the title of the website
    #print("\n",soup.title.parent.string)

    for link in soup.find_all('a'):              # to get all the links using iteration 
    print(link.get('href'))



    print(soup.get_text())      # for getting all the texts from page

    Flexible URL Input: The script accepts a URL as input, allowing users to specify the web page from which they want to retrieve HTML content.

Function-Driven Approach: The core functionality is encapsulated in a function named fetch_and_save_to_file. This function takes care of making the HTTP request, retrieving the content, and saving it to a file.

UTF-8 Encoding: The script ensures that the file is opened with UTF-8 encoding, accommodating websites with various character sets.

Sample Usage: A practical example is provided within the script, demonstrating how to use the function to fetch and save the HTML content of the "Times of India" news page.
