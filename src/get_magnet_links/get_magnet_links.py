import requests
from bs4 import BeautifulSoup

def scrape_website(url):

    response = requests.get(url)


    if response.status_code == 200:
     
        soup = BeautifulSoup(response.text, 'html.parser')


        elements = soup.find_all(lambda tag: tag.name == 'a' and "Magnet" in tag.get_text())

        magnet_links = [element.attrs['href'] for element in elements]
        return magnet_links
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")