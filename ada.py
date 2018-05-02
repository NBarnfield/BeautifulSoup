import time
from bs4 import BeautifulSoup
import requests


def get_links(url, final_page, start_page=1):
    """Get search page urls for scraping individual pages"""

    links = []

    for page in range(start_page, final_page):
        r = requests.get(url.format(page))
        soup = BeautifulSoup(r.content, "html.parser")

        # Define the html attribute that needs parsing.
        div = soup.find_all('li')

        for link in div:
            try:
                links.append('https://www.ada.org.au' + link.h4.a.get('href'))
                print(links)
                time.sleep(10)

            except:
                pass

    return links


def contents(url_list):
    """Collect contact and address details for each page."""
    for link in url_list:
        # Import urls into a BeautifulSoup Object #
        r = requests.get(link)
        soup = BeautifulSoup(r.content, "html.parser")

        # Select the elements required for parsing #
        try:
            premises_name = soup.find('span', {'id': 'p_lt_WebPartZone8_ZonePlaceholder_pageplaceholder_p_lt_ctl02_ADASearchPracticeDetails_lblPracticeName'}).text.strip()
        except:
            premises_name = "None"
        try:
            address_one = soup.find('span', {'id': 'p_lt_WebPartZone8_ZonePlaceholder_pageplaceholder_p_lt_ctl02_ADASearchPracticeDetails_lblAddressLine1'}).text.strip()
        except:
            address_one = "None"
        try:
            address_two = soup.find('span', {'id': 'p_lt_WebPartZone8_ZonePlaceholder_pageplaceholder_p_lt_ctl02_ADASearchPracticeDetails_lblAddressLine2'}).text.strip()
        except:
            address_two = "None"
        try:
            citystatepostcode = soup.find('span', {'id': 'p_lt_WebPartZone8_ZonePlaceholder_pageplaceholder_p_lt_ctl02_ADASearchPracticeDetails_lblCityStatePostcode'}).text.strip()
        except:
            citystatepostcode = "None"
        try:
            Telephone = soup.find('span', {'id': 'p_lt_WebPartZone8_ZonePlaceholder_pageplaceholder_p_lt_ctl02_ADASearchPracticeDetails_lblTelephone'}).text.strip()
        except:
            Telephone = "None"
        try:
            Website = soup.find('span', {'id': 'p_lt_WebPartZone8_ZonePlaceholder_pageplaceholder_p_lt_ctl02_ADASearchPracticeDetails_lblWebsite'}).text.strip()
        except:
            Website = "None"
        try:
            Email = soup.find('span', {'id': 'p_lt_WebPartZone8_ZonePlaceholder_pageplaceholder_p_lt_ctl02_ADASearchPracticeDetails_lblEmail'}).text.strip()
        except:
            Email = "None"

        f.write(premises_name + "," + address_one + "," + address_two + "," + citystatepostcode + "," + Email + "," + Telephone  + "," + Website + "\n")

        # Sleep to space out requests #
        print("Still looping...")
        time.sleep(10)



filename = "dentists.csv"
f = open(filename, 'w')
headers = "premises_name, address_one, address_two, citystatepostecode, email, telephone, website\n"
f.write(headers)
dentist_url = ("https://www.ada.org.au/Directory/CompanySearch?searchtext=IndividualData__Specialties=a*%20b*%20c*%20d*%20e*%20f*%20g*%20h*%20i*%20j*%20k*%20l*%20m*%20n*%20o*%20p*%20q*%20r*%20s*%20t*%20u*%20v*%20w*%20x*%20y*%20z*;&searchmode=anyword&stype=location&radius=3&postcode=2000&location=SYDNEY,%202000%20-%20NSW&page={}")
urls = get_links(dentist_url, 25)
print("Complete: {}".format(urls))
f.write(contents(urls))
f.close()