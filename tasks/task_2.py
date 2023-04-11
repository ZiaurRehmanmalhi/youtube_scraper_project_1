from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

url = "https://www.youtube.com/@zusmani78/videos"
driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(url)
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
    time.sleep(1.5)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
all_content = soup.find_all('ytd-rich-item-renderer')

data = []
for videos in all_content:
    thumbnail = videos.find('img', {"style": "background-color: transparent;"}).get('src')
    title = videos.find('yt-formatted-string', {"id": "video-title"}).text
    views = videos.find('span', {"class": "inline-metadata-item style-scope ytd-video-meta-block"}).text
    upload_time = videos.find('span', {"class": "inline-metadata-item style-scope ytd-video-meta-block"}).get('before')
    video_duration = videos.find(
        'span', {"class": "style-scope ytd-thumbnail-overlay-time-status-renderer"}
    ).text.strip()
 
    all_data = {
        "Title": title,
        "Views": views,
        "Video Duration": video_duration,
        "Thumbnail Link": thumbnail
    }
    data.append(all_data)

df = pd.DataFrame(data)
df.to_csv('youtube_data.csv', index=False)
print("Data saved to csv file")
