def clean(str):
    return str.replace("\\n", "").strip()

import requests, bs4

r = requests.get('http://stats.nhlnumbers.com/players/index_griddle.json?perPage=700')
soup = bs4.BeautifulSoup(r.text, "html.parser")

for tr in soup.find_all('tr'):
    tds = tr.find_all('td')
    print ("Player: " + clean(tds[0].text))
    print ("Team: " + clean(tds[1].text))
    print ("Position: " + clean(tds[2].text))
    print ("17/18: " + clean(tds[3].text))
    print ("18/19: " + clean(tds[4].text))
    print ("17/18: " + clean(tds[5].text))
    print ("18/19: " + clean(tds[6].text))
    print ("19/20: " + clean(tds[7].text))
    print ("20/21: " + clean(tds[8].text))
    print ("21/22: " + clean(tds[9].text))
    print("")
    print("")