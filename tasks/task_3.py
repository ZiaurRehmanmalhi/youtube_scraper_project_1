from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from utils import scroll_to_page_end, extract_videos_data

url = input("Enter Any Youtube Chanel URL : ")
url += "/videos"
driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(url)
scroll_to_page_end(driver)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
data = extract_videos_data(soup)

dataframe = pd.DataFrame(data)
dataframe.to_csv(f"{url.split('/')[-2]}.csv", index=False)
print("Data saved to csv file")
