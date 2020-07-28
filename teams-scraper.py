import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    SCRAPE_URL = 'https://en.wikipedia.org/wiki/List_of_professional_sports_teams_in_the_United_States_and_Canada'
    # Get the html content
    html_content = requests.get(SCRAPE_URL).text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Get the table content
    gdp_table = soup.find("table", attrs={"class": "wikitable"})
    gdp_table_data = gdp_table.tbody.find_all("tr")

    # Get all the headers
    headers = []
    for th in gdp_table_data[0].find_all("th"):
        headers.append(th.text.replace('\n', '').strip())
    print(headers)

    # Get all the rows
    teams = []
    for tr in gdp_table_data:
        table_row = []
        for td in tr.find_all("td"):
            table_row.append(td.text.replace('\n', '').strip())
        if len(table_row) > 0:
            teams.append(table_row)
    print(teams)
