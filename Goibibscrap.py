
import requests
from bs4 import BeautifulSoup
import pandas as pd

# target URL to scrap
url = "https://www.goibibo.com/hotels/hotels-in-shimla-ct/"

# headers
headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }

# send request to download the data
response = requests.request("GET", url, headers=headers)

# parse the downloaded data
data = BeautifulSoup(response.text, 'html.parser')

cards_data = data.find_all('div', attrs={'class', 'HotelCardstyles__WrapperSectionMetaDiv-sc-1s80tyk-3 fLGqLz'})

# total number of cards
print('Total Number of Cards Found : ', len(cards_data))

scraped_data=[]

for card in cards_data:

    card_details = {}
    # get the hotel name
    hotel_name = card.find('a')
    #print(hotel_name.text)

    # get the room price
    room_price = card.find('p', attrs={'class': 'HotelCardstyles__CurrentPrice-sc-1s80tyk-28 inUyrJ'})
    #room_price = card.find('p')

    card_details['hotel_name'] = hotel_name.text
    card_details['room_price'] = room_price.text

    # append the scraped data to the list
    scraped_data.append(card_details)

    #print(hotel_name.text, room_price.text)
    # create a data frame from the list of dictionaries
    dataFrame = pd.DataFrame.from_dict(scraped_data)

    # save the scraped data as CSV file
    dataFrame.to_csv('hotels_data.csv', index=False)

