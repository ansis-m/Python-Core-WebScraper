import requests
import string
from bs4 import BeautifulSoup
import os

url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page="
url_base = "https://www.nature.com"


def main():

    while True:
        try:
            pages = int(input("enter number of pages: "))
            article_type = input("enter article type: ")
            break
        except:
            print("bad input! try again!")

    for i in range(1, pages + 1):
        response = requests.get(url + str(i), headers={'Accept-Language': 'en-US,en;q=0.5'})
        if not response:
            print("The URL returned {}!".format(response.status_code))
        else:
            try:
                dir_name = "Page_" + str(i)
                os.mkdir(dir_name)
                soup = BeautifulSoup(response.content, 'html.parser')
                for a in soup.find_all('article'):
                    if a.find('span', {'class':'c-meta__type'}).text == article_type:
                        filename = a.find('a').text.strip().translate(str.maketrans('', '', string.punctuation)).replace(" ", "_") + ".txt"
                        file = open(os.path.join(dir_name, filename), 'wb')
                        article = requests.get(url_base + a.find('a').get('href'), headers={'Accept-Language': 'en-US,en;q=0.5'})
                        article_soup = BeautifulSoup(article.content, 'html.parser')
                        content = article_soup.find('div', {'class':'c-article-body u-clearfix'}).text.strip().replace("\n", "")
                        file.write(content.encode())
                        file.close()
                print("Content saved.")
            except Exception as e:
                print("***********Error!***********\n")
                print(e)

if __name__ == "__main__":
    main()