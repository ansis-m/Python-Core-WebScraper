import requests

def main():

    url = input("Input the URL:")
    response = requests.get(url)
    if not response:
        print("Invalid quote resource!")
    else:
        try:
            print(response.json()["content"])
        except:
            print("Invalid quote resource!")

if __name__ == "__main__":
    main()