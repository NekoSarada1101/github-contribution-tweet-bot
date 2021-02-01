import requests
from bs4 import BeautifulSoup


def main():
    response = requests.get("https://github.com/users/NekoSarada1101/contributions")
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")

    for tags in soup.find_all("rect"):
        print(tags.get('data-count'))


if __name__ == "__main__":
    main()
