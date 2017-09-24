## Premise: Import CSV as variable array values and then loop to get contents of each link ###

## Import requisite libraries ##
import requests
from bs4 import BeautifulSoup
import time
import csv

## Open file to write results to ##
filename = "wineries.csv"
f = open(filename, 'w')
headers = "premises_name, wine_region, website, premises_address, premises_suburb, premises_state&postcode, phone, fax, opening_hours, winemaker, established, dozen, yineyards\n"
f.write(headers)

## import hyperlinks from csv ##
with open("wineries_hyperlinks_sc.csv", "r") as winery_hyperlinks:
    reader = csv.reader(winery_hyperlinks)
    for row in reader:
        url = row[0]
        r = requests.get(url)
        soup = BeautifulSoup(r.content)
    
    
        try:
            f.write(premises_name + "," + wine_region + "," + winery_website + ",")
        except:
            pass
        
    ## Select the elements required for parsing ##
    
        try:
            premises_name = soup.find('h1', {'class': 'section-title'}).text.strip()
        except:
            pass
        try:
            wine_region = soup.find('p', {'class': 'location'}).text.strip()
        except:
            pass
        try:
            winery_website = soup.find('p', {'class': 'website'}).text.strip()
        except:
            pass
    
    ## Select address elemts from within a divider ##
        try:
            wineryinfo_div = soup.find('div', {'id': 'winery-info'})
        except:
            pass
        try:
            winery_info = wineryinfo_div.find_all('dd')
        except:
            pass
        try:
            for dd in winery_info:
                details = (dd.text.strip().replace("\n","").replace("\t","").replace("\r",""))
                print(details)
                f.write(details + ",")     
        except:
            pass
        
        try:
            f.write('\n')
        except:
            pass
    
    ## Sleep to space out requests ##
        time.sleep(3)
    
f.close()
