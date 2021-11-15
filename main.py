import json
import re
import sys

import requests

from requests import Response
from bs4 import BeautifulSoup, Tag


def download_holiday_html(state: str, year: int) -> str:
    """
    download the holidays from the providing website

    :param state: federal state of germany
    :param year: year of the holidays
    :return: html string
    """
    lower_state = state.lower()
    url = f"https://www.ferienkalender.com/ferien_deutschland/{state}/{year}-ferien-{lower_state}.htm"

    # retry http gets -> frequently failures
    # use a timeout for faster overall download
    for retry in range(10):
        try:
            resp: Response = requests.get(url, allow_redirects=True, timeout=5.00)
            return bytes.decode(resp.content)
        except:
            print_retry = retry + 1
            print(f"retry={print_retry}")


def get_holidays(state: str, year: int, include_names: bool) -> [str]:
    """
    get the holidays for the given federal state in Germany for the given year

    :param state: federal state of Germany
    :param year: year of the holidays
    :param include_names: true, if should include the names
    :return: list of holidays in the year in the state
    """
    html = download_holiday_html(state, year)
    html_tree = BeautifulSoup(html, 'lxml')

    holidays = []
    for card in html_tree.findAll("div"):
        if len(card["class"]) == 1 and 'kasten' in card["class"]:  # check for kasten class div

            card_tree = BeautifulSoup(card.prettify(), 'lxml')
            headline: Tag = card_tree.find('p')

            display_state = re.sub("ue", "ü", state)  # for Thüringen

            # check the headline
            if headline is not None and headline.text.__contains__(f"Feiertage {display_state} {year}"):
                rows = card_tree.findAll('tr', recursive=True)

                for row in rows:  # every row contains one holiday
                    row_tree = BeautifulSoup(row.prettify(), 'lxml')
                    row_part = row_tree.findAll('td', recursive=True)

                    # strip new lines, spaces, etc.
                    holiday_name = row_part[0].text.strip()

                    # replace everything but the date value
                    date_only = re.sub(r"[^=.0123456789]*", "", row_part[1].text)

                    if include_names:
                        add_obj = {
                            "holiday": holiday_name,
                            "date": date_only
                        }
                    else:
                        add_obj = date_only

                    holidays.append(add_obj)

    return holidays


def parse_all_holidays(year: int, include_names: bool) -> dict:
    """
    parse the holidays for every federal state in Germany

    :param year: year to get the holidays of
    :param include_names: true, if should include the names
    :return: list of holidays per federal state in Germany
    """
    states = ["Baden-Wuerttemberg", "Bayern", "Berlin", "Brandenburg", "Bremen", "Hamburg", "Hessen",
              "Mecklenburg-Vorpommern", "Niedersachsen", "Nordrhein-Westfalen", "Rheinland-Pfalz", "Saarland",
              "Sachsen", "Sachsen-Anhalt", "Schleswig-Holstein", "Thueringen", ]

    holidays = {}
    for state in states:
        state_holidays = get_holidays(state, year, include_names)
        holidays[state] = state_holidays
        print(f"finished state={state} for year={year}")
    return holidays


def main(include_names: bool):
    """
    main entry point - for clean scope
    :param include_names: true, if should include the names
    """
    years = [2021, 2022]
    for year in years:
        file = open(f"results/{year}.json", "w")
        file.write(json.dumps(parse_all_holidays(year, include_names), indent=2))
        file.close()
        print(f"completed for year={year}")
    print("success")


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == "true":
        include_names_param = True
    else:
        include_names_param = False
    main(include_names_param)
