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

    comparison = int(contributions[0]) - int(contributions[1])
    if comparison < 0:
        comparison = str(comparison)
    elif comparison >= 0:
        comparison = "+" + str(comparison)
    print("comparison=" + comparison)

    streak = 0
    for i in contributions:
        if i == "0":
            break
        streak = streak + 1
    streak = str(streak)
    print("streak=" + streak)


if __name__ == "__main__":
    main()
