# xkcddownloader.py
# automated download of xkcd comics from website


import requests
import os
import bs4

# Setup the url for xkcd

url = "https://xkcd.com"

# Create a folder to store the comics
os.makedirs("xkcd_pictures", exist_ok=True)


# Loop to download all the comics

while not url.endswith("#"):
    # TODO: download the page (html)
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # TODO: Find the URL of picture using bs4
    # TODO: Download the image
    # TODO: Save the image
    # TODO: Get the Previous button URL
    prev_link = soup.select('a[rel="prev"]')[0] #/2396
    url = "https://xkcd.com" + prev_link.get("href")

print("Done")

