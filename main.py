import requests
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1Session
from settings import *

twitter = OAuth1Session(CK, CS, AT, AS)


def main(data, context):
    response = requests.get("https://github.com/users/NekoSarada1101/contributions")
    print(response)
    print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")

    contributions = []  # type: list
    for tags in soup.find_all("rect"):
        if tags.get('data-count') is not None:
            contributions.append(tags.get('data-count'))
    contributions.reverse()
    print(contributions)

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

    text = "GitHub Contributions\n\n" \
           "今日のContributions\n" \
           "　{} contributions\n\n" \
           "今日と昨日の比較\n" \
           "　{} contributions\n\n" \
           "連続Contributions日数\n" \
           "　{}日".format(today, comparison, streak)  # type: str

    endpoint_url = "https://api.twitter.com/1.1/statuses/update.json"  # type: str
    params = {'status': text}  # type: dict
    response = twitter.post(url=endpoint_url, params=params)  # type: response
    print(response)
    print(response.text)


if __name__ == "__main__":
    main("data", "context")
