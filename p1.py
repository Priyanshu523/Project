import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XpbN6_gzbDc")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup) for content
#print(soup.find_all('a')) for ancher tage

week = soup.find(id="seven-day-forecast-body")
#print(week) for content of week by id of html

#items = week.find_all('li') for list of seven days
items = week.find_all(class_="tombstone-container")
#print(items) all seven days data
#print(items[0])

#print(items[0].find(class_="period-name")) for content of day
print(items[0].find(class_="period-name").get_text())
print(items[0].find(class_="short-desc").get_text())
print(items[0].find(class_="temp").get_text())

# all values in list
period_name = [item.find(class_="period-name").get_text() for item in items]
short_description = [item.find(class_="short-desc").get_text() for item in items]
temperature = [item.find(class_="temp").get_text() for item in items]
print(period_name)
print(short_description)
print(temperature)

#Tried
weather_stuff = pd.DataFrame({
    'period':period_name,
     'short_description':short_description,
    'temperature':temperature,

}
)
print(weather_stuff)
weather_stuff.to_csv('weather.csv')