from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from os import getenv

load_dotenv()

login = getenv("LOGIN")
password = getenv("PASSWORD")


def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.moodle-trebesin.cz")

        page.click("span.login.pl-2")
        page.fill("input#username", login)
        page.fill("input#password", password)

        page.click("button#loginbtn")

        # page.wait_for_timeout(1000) # čeká 1 sekundu
        # page.wait_for_selector("#nahodny_prvek") # čeká na konkrétní element
        # element = page.locator("#nahodny_prvek") # ulolží element pod proměnnou
        # text_elementu = element.text_content() # získá textový obsah elementu


        input("Zmáčkni cokoliv pro zavření")
        browser.close()


if __name__ == "__main__":
    main()
