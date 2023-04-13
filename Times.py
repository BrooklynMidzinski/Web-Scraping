import requests
from bs4 import BeautifulSoup


url = f"https://www.swimcloud.com/api/splashes/top_times/?dont_group=false&event=150&eventcourse=Y&gender=M&page=1&region=state_hi&season_id=26"
response = requests.get(url)
print(response.json()['results'] [0]) 