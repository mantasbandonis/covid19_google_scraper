from bs4 import BeautifulSoup
import requests

r = requests.get("https://google.org/crisisresponse/covid19-map")
c = r.content
table = BeautifulSoup(c, "html.parser")
table_body = table.find('tbody')
rows = table_body.findAll('tr')


# Parameters 1 = display , 0 = dont display

def covidaustria(cases: int, recovered: int, dead: int):
    for row in rows:
        if row.td.img['src'] == "https://www.gstatic.com/onebox/sports/logos/flags/austria_icon_square.svg":
            if cases == 1:
                cases = row.findAll('td', {"class": "table_card_cell_col_1 table_card_cell_int_type"})
                for tag in cases:
                    cases = str(tag.contents[0])
                    cases = cases.strip()
                    cases = cases.replace(',', '')
                    print("Total Cases in Austria: {}".format(cases))
            elif cases == 0:
                cases = "No search for Cases"
            else:
                raise ValueError("Please put either 1 (yes, display) or 0 (no display)")


            if recovered == 1:
                recovered = row.findAll('td', {"class": "table_card_cell_col_3 table_card_cell_int_type"})
                for tag2 in recovered:
                    recovered = str(tag2.contents[0])
                    recovered = recovered.strip()
                    print("Total Recovered in Austria: {}".format(recovered))
            elif recovered == 0:
                recovered = "No search for Recovered"

            else:
                raise ValueError("Please put either 1 (yes, display) or 0 (no display)")

            if dead == 1:
                dead = row.findAll('td', {"class": "table_card_cell_col_4 table_card_cell_int_type"})
                for tag3 in dead:
                    dead = str(tag3.contents[0])
                    dead = dead.strip()
                    print("Total Deaths in Austria: {}".format(dead))
            elif dead == 0:
                dead = "No search for Dead"

            else:
                raise ValueError("Please put either 1 (yes, display) or 0 (no display)")

            return cases, recovered, dead
