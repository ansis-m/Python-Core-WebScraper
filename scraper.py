import requests
import string
from bs4 import BeautifulSoup

url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
url_base = "https://www.nature.com"


def main():

    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if not response:
        print("The URL returned {}!".format(response.status_code))
    else:
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            for a in soup.find_all('article'):
                if a.find('span', {'class':'c-meta__type'}).text == 'News':
                    filename = a.find('a').text.strip().translate(str.maketrans('', '', string.punctuation)).replace(" ", "_") + ".txt"
                    file = open(filename, 'wb')
                    article = requests.get(url_base + a.find('a').get('href'), headers={'Accept-Language': 'en-US,en;q=0.5'})
                    article_soup = BeautifulSoup(article.content, 'html.parser')
                    content = article_soup.find('div', {'class':'c-article-body u-clearfix'}).text.strip().replace("\n", "")
                    file.write(content.encode())
                    file.close()
            print("Content saved.")
        except:
            print("Error!")

if __name__ == "__main__":
    main()