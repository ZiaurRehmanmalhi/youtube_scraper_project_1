import time


def scroll_to_page_end(driver):
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)
        time.sleep(1.5)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def extract_videos_data(soup):
    video_elements = soup.find_all('ytd-rich-item-renderer')
    videos_data = []
    for videos in video_elements:
        thumbnail = videos.find('img', {"style": "background-color: transparent;"}).get('src')
        title = videos.find('yt-formatted-string', {"id": "video-title"}).text
        views = videos.find('span', {"class": "inline-metadata-item style-scope ytd-video-meta-block"}).text
        uploaded_at = videos.find(
            'div', {"class": "style-scope ytd-video-meta-block"}
        ).text.strip().split('\n')[-1::-3][0]

        video_duration = videos.find(
            'span', {"class": "style-scope ytd-thumbnail-overlay-time-status-renderer"}
        ).text.strip()

        all_video_data = {
            "Title": title,
            "Views": views,
            "Uploaded_at": uploaded_at,
            "Video Duration": video_duration,
            "Thumbnail Link": thumbnail
        }
        videos_data.append(all_video_data)
    return videos_data
