import requests
import bs4

# create a session
session = requests.Session()
# send login request

# selections
month = 3
day = 6
year = 2024

# urls
search_url = f"https://www.spotery.com/search?psLangId=EN&psAddrCity=San%20Francisco&psReservationDateStr={month}/{day}/{year}&psTimeRangeId=MORNING&psSourceFlow=SPOT&psOrgaSk=2654382&psIsGridView=false&psFavorites=false"

# search urls require that you click a button to get availability so may be more challenging to scrape. I can either send a request for each spot (in the UI, you click on an a tag) or load all your favorite spots to see

# testing pulling the data
search_page = requests(search_url)

# Basic ideas:
'''
Need to be able to login (if you login, you might be able to save favorite places)
Should be able to look for a date (or dates) and a time range
Need to limit to near you (could pre-configure the close urls or the names of places)
If it's available, should book
It should only book one
'''