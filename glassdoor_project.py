from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen

try:
    html_text = Request('https://www.glassdoor.co.in/Overview/Working-at-Gilead-Sciences-EI_IE2016.11,26.htm',headers={'User-Agent': 'Mozilla/5.0'})

    webpage = urlopen(html_text).read()
    soup = BeautifulSoup(webpage,'html.parser')
    

    head = soup.find(attrs={'data-test':'employer-headquarters'}).text
    for heads in head:
    
        webpage = soup.find(attrs={'data-test':'employer-website'}).text
        size = soup.find(attrs={'data-test':'employer-size'}).text
        page_type = soup.find(attrs={'data-test':'employer-type'}).text
        ravenue = soup.find(attrs={'data-test':'employer-revenue'}).text
        fouded = soup.find(attrs={'data-test':'employer-founded'}).text
        industry = soup.find(attrs={'data-test':'employer-industry'}).text


    print(webpage,size,page_type,ravenue,fouded,industry,head)
    
    
    

except Exception as e:
    print(e)