import requests
from bs4 import BeautifulSoup

def main():

    file = open('source.html', 'wb')
    response = requests.get(input("Input the URL:"), headers={'Accept-Language': 'en-US,en;q=0.5'})
    if not response:
        print("The URL returned {}!".format(response.status_code))
    else:
        try:
            # soup = BeautifulSoup(response.content, 'html.parser')
            # print({"title" : soup.find("h1").contents.pop(), "description" : soup.find("span", {'data-testid': 'plot-xl'}).contents.pop()})
            file.write(response.content)
            file.close()
            print("Content saved.")
        except:
            file.close()
            print("Error!")

if __name__ == "__main__":
    main()