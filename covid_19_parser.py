from bs4 import BeautifulSoup
import requests

r = requests.get("https://google.org/crisisresponse/covid19-map")
c = r.content
table = BeautifulSoup(c, "html.parser")
table_body = table.find('tbody')
rows = table_body.findAll('tr')


# Params cases ( yes or no to display), recovered ( yes or no to display)
def covidaustria(cases: int, recovered: int):
    for row in rows:
        if row.td.img['src'] == "https://www.gstatic.com/onebox/sports/logos/flags/austria_icon_square.svg":
            if cases == 1:
                cases = row.findAll('td', {"class": "table_card_cell_col_1 table_card_cell_int_type"})
                for tag in cases:
                    casesstr = str(tag.contents[0])
                    casesstr = casesstr.strip()
                    casesstr = casesstr.replace(',', '')
                    print("Total Cases in Austria: {}".format(casesstr))
            elif cases == 0:
                casesstr = "No search for Cases"
            else:
                pass

            if recovered == 1:
                recovered = row.findAll('td', {"class": "table_card_cell_col_3 table_card_cell_int_type"})
                for tag2 in recovered:
                    recovstr = str(tag2.contents[0])
                    recovstr = recovstr.strip()
                    recovstr = recovstr.replace(',', '')
                    print("Total Recovered in Austria: {}".format(recovstr))
            elif recovered == 0:
                recovstr = "No search for Recovered"
            else:
                pass

            return casesstr, recovstr
