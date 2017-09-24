# Premise: Get all hyperlinks for future looping  and data requests ##

# Import requisite libraries #
import requests
from bs4 import BeautifulSoup
import time
import csv

# Open file to write results to #
filename = "wineries.csv"
f = open(filename, 'w')
headers = "premises_name, wine_region, website, premises_address, premises_suburb, premises_state&postcode, phone, fax, opening_hours, winemaker, established, dozen, yineyards\n"
f.write(headers)

# Set url variable
winery_websites = []
for page_number in range(1, 350):
    url = ("http://www.winecompanion.com.au/search?t=2&q=&page={}".format(page_number))

# Import urls into a BeautifulSoup Object #
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    
# Select the divider for parsing #
    div_contents = soup.find_all('div', {'class': 'info-main'})

# Set for loop to extract web address with sleep to space out requests #
    for link in div_contents:
        try:
            web_link = ("http://www.winecompanion.com.au"+link.h3.a.get('href'))
            
        except:
            pass

        winery_websites.append(web_link)
        time.sleep(3)

    # Now that winery_website list has a value, perform a for loop to extract contents and write to file. #

for website in winery_websites:
    
    # Import urls into a BeautifulSoup Object #
    r = requests.get(website)
    soup = BeautifulSoup(r.content)
    
    # Select the elements required for parsing #
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
    
    f.write(premises_name + "," + wine_region + "," + winery_website + ",")
    
    # Select address elements from within a divider #
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
            f.write(details + ",")
            
    except:
        pass
        
    f.write('\n')
    
    # Sleep to space out requests #
    time.sleep(3)
    
f.close()