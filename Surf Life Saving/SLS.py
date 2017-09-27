# Premise: Get all hyperlinks from directory, loop through individual page contents and export to csv.

# Import requisite libraries
import requests
from bs4 import BeautifulSoup
import time

# Create list and set url variable
sls_websites = []
url = "https://sls.com.au/club_directory/?term="

# Import urls into a BeautifulSoup Object
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')

# Select the element for parsing
span_contents = soup.find_all('span', {'class': 'name'})

# Set for loop to extract web address
for link in span_contents:
    try:
        web_link = ("https://sls.com.au/club_directory/" + link.a.get('href'))
        sls_websites.append(web_link)

    except:
        pass

# Test that websites have been collected correctly
#print(sls_websites)


# Open file to write results to
filename = "sls.csv"
f = open(filename, 'w')
headers = "branch_name, premises_phone, premises_fax, email, website, premises_address, premises_suburb, premises_state, premises_postcode, local_beach\n"
f.write(headers)


# Create for loop to scrape individual pages
for website in sls_websites:
    r = requests.get(website)
    soup = BeautifulSoup(r.content, 'lxml')

    # Set variables
    branch = soup.find('div', {'id': 'cd-parent'}).find('span', {'class': 'detail'}).text
    phone = soup.find('div', {'id': 'cd-phone'}).find('span', {'class': 'detail'}).text
    fax = soup.find('div', {'id': 'cd-fax'}).find('span', {'class': 'detail'}).text
    email = soup.find('div', {'id': 'cd-email'}).find('span', {'class': 'detail'}).text
    website = soup.find('div', {'id': 'cd-website'}).find('span', {'class': 'detail'}).text
    address = soup.find('div', {'id': 'cd-address'}).find('span', {'class': 'detail'}).text
    suburb = soup.find('div', {'id': 'cd-suburb'}).find('span', {'class': 'detail'}).text
    state = soup.find('div', {'id': 'cd-state'}).find('span', {'class': 'detail'}).text
    local_beach = soup.find('div', {'id': 'cd-beach'}).find('span', {'class': 'detail'}).text
    post_code = soup.find('div', {'id': 'cd-postcode'}).find('span', {'class': 'detail'}).text

    # Write variables to file
    f.write(branch + ", " + phone + ", " + fax + ", " + email + ", " + website + ", " + address + ", " + suburb + ", " + state + ", " + local_beach + ", " + post_code + "\n")

    # Sleep to space out requests
    time.sleep(2)

# Close file
f.close()
