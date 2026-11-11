from bs4 import BeautifulSoup
import requests

def main():

    url = "https://www.trebesin.cz"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    # .select a select_all používá CSS selectory ., #, atd.
    gym = soup.select_one("#favimagehover-title4")
    # gym = soup.find(id="favimagehover-title4")
    print(gym.text)


    headings = soup.select("h4")
    # headings = soup.find_all("h4")
    for heading in headings:
        print(heading.text.strip())

     # find a find_all a jsou alternativy k select_one a select

if __name__ == "__main__":
    main()