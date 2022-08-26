import requests
from bs4 import BeautifulSoup

url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"

def main():

    file = open('source.html', 'wb')
    response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    if not response:
        print("The URL returned {}!".format(response.status_code))
    else:
        try:
            # print(response.content)
            soup = BeautifulSoup(response.content, 'html.parser')
            print(soup.find_all("a", {'data-track-action' : 'view article'}))

            for PageElement in soup.find_all("a", {'data-track-action' : 'view article'}):
                print("*** {} ***".format(PageElement.contents.pop()))
            print({"title" : soup.find("h1").contents.pop(), "description" : soup.find("span", {'data-testid': 'plot-xl'}).contents.pop()})
            # file.write(response.content)
            # file.close()
            print("Content saved.")
        except:
            # file.close()
            print("Error!")

if __name__ == "__main__":
    main()