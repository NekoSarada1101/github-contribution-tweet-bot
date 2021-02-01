import requests
from bs4 import BeautifulSoup


def main():
    response = requests.get("https://github.com/users/NekoSarada1101/contributions")
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")

    contributions = []  # type: list
    for tags in soup.find_all("rect"):
        contributions.append(tags.get('data-count'))
    contributions.reverse()

    today = contributions[0]  # type: str
    print("today=" + today)

if __name__ == "__main__":
    main()
