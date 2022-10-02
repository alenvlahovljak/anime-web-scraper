import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.animefillerlist.com/shows/one-piece"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

data_list = soup.find(name="table", class_="EpisodeList")
datat = data_list.find_all(name="tr")

data_list = []
for data in datat:
    try:
        num = data.select_one("td.Number").getText()
        title = data.select_one("td.Title a").getText()
        type = data.select_one("td.Type span").getText()
        date = data.select_one("td.Date").getText()
        data_list.append([num, title, type, date])

    except AttributeError:
        pass

with open('theMostImpData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Ep No.", "Name", "Type", "Date"])

    for data in data_list:
        writer.writerow([data[0], data[1], data[2], data[3]])
