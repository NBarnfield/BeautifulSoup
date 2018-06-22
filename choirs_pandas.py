from collections import defaultdict
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

data = defaultdict(list)

for page in range(1, 15):
    time.sleep(5)
    r = requests.get("http://anca.org.au/index.php?page=choir-search&choir_name=&choir_state=nsw&choir_rehearsal_day=0&page_num={}".format(page))
    soup = BeautifulSoup(r.content, "html.parser")

    choir_data = soup.find_all("div", {"class": "choirListContainer"})

    for choir_div in choir_data:

        try:
            choir_name = choir_div.find("a")
            data['choir'].append(choir_name.text)

        except ValueError:
            data['choir'].append('NaN')

        try:
            contact_name = choir_div.find("td", string="Contact").find_next_sibling("td")
            data['contact'].append(contact_name.text)

        except ValueError:
            data['contact'].append('NaN')

        try:
            venue_name = choir_div.find_all("td", {"class": "label"})[1].find_next_sibling("td")
            data['venue'].append(venue_name.text)

        except ValueError:
            data['venue'].append('NaN')

        try:
            phone_details = choir_div.find_all("td", {"class": "label"})[2].find_next_sibling("td")
            data['phone'].append(phone_details.text)

        except ValueError:
            data['phone'].append('NaN')

        try:
            url = choir_div.find_all("a")[1].get('href')
            if 'http:' not in url:
                data['website'].append('NaN')
            else:
                data['website'].append(url)

        except ValueError:
            data['website'].append('NaN')


df = pd.DataFrame(data)
print(df)
df.to_csv("choirs.csv")
