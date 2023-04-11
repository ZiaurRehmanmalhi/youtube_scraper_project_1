from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from utils import scroll_to_page_end, extract_videos_data

url = "https://www.youtube.com/@zusmani78/videos"
driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(url)
scroll_to_page_end(driver)       # utils function_1 call

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
data = extract_videos_data(soup)      # utils function_2 call

dataframe = pd.DataFrame(data)
dataframe.to_csv('zusmani78.csv', index=False)
print("Data saved to csv file")
