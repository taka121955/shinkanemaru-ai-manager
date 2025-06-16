import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_today_venues():
    url = "https://www.boatrace.jp/owpc/pc/race/index"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    today = datetime.now().strftime("%m/%d")  # 例: 06/17
    venues = []

    for race in soup.select(".raceListArea .raceList"):
        date_info = race.select_one(".date")
        if date_info and today in date_info.text:
            venue_name_tag = race.select_one(".venue")
            if venue_name_tag:
                venues.append(venue_name_tag.text.strip())

    return venues
