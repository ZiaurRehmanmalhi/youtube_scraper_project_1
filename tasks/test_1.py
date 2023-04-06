from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="chromedriver")
driver.get("https://www.youtube.com/@zusmani78/videos")

scroll_distance = 2000
i = 0

while True:
    driver.execute_script("window.scrollBy(0, 2000);")
    time.sleep(0.5)
    i += 1

driver.quit()
