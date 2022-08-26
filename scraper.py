import requests
from bs4 import BeautifulSoup

def main():

    response = requests.get(input("Input the URL:"), headers={'Accept-Language': 'en-US,en;q=0.5'})
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        print({"title" : soup.find("h1").contents.pop(), "description" : soup.find("span", {'data-testid': 'plot-xl'}).contents.pop()})
    except:
        print("Invalid movie page!")

if __name__ == "__main__":
    main()