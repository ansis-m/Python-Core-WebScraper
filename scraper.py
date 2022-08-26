import requests
from bs4 import BeautifulSoup

url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
url_base = "https://www.nature.com"

def main():

    file = open('source.html', 'wb')
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if not response:
        print("The URL returned {}!".format(response.status_code))
    else:
        try:
            # print(response.content)
            soup = BeautifulSoup(response.content, 'html.parser')
            for a in soup.find_all('article'):
                if a.find('span', {'class':'c-meta__type'}).text == 'News':
                    print(a.find('a').text)
                    print(a.find('a').get('href'))
                    article = requests.get(url_base + a.find('a').get('href'), headers={'Accept-Language': 'en-US,en;q=0.5'})
                    article_soup = BeautifulSoup(article.content, 'html.parser')
                    print("\n\n******************************************************")

                    print(article_soup.find('div', {'class':'c-article-body u-clearfix'}).text.strip().replace("\n", ""))

                    # for p in article_soup.find_all(lambda tag: tag.name == 'p' and not tag.attrs):
                    #     print(p.text)
                    print("\n\n******************************************************")





        # print(soup.find_all("a", {'data-track-action' : 'view article'}))
            # for PageElement in soup.find_all("a", {'data-track-action' : 'view article'}):
            #     print("*** {} ***".format(PageElement.contents.pop()))
            # print({"title" : soup.find("h1").contents.pop(), "description" : soup.find("span", {'data-testid': 'plot-xl'}).contents.pop()})
            # file.write(response.content)
            # file.close()
            print("Content saved.")
        except:
            # file.close()
            print("Error!")

if __name__ == "__main__":
    main()