from selenium import webdriver
import json
import time

from common_functions import extract_info, remove_unneedful_tags

def get_html(url):
    # Create a new instance of the Firefox driver
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)

    # Navigate to the specified URL
    driver.get(url)

    # Get the HTML content of the page
    html = driver.page_source
    current_size = len(html)

    # Wait for the page content to load
    for _ in range(5):
        time.sleep(1)
        page_source = driver.page_source
        if len(page_source) != current_size:
            html = page_source
            break
    
    # Close the browser
    driver.quit()

    return html

def get_info_and_print(url):
    html = remove_unneedful_tags(get_html(url))
    if html:
        info = extract_info(html)
        if info:
            print(json.dumps(info, indent=4))


get_info_and_print('https://ai.google.dev/competition')  # success
get_info_and_print('https://m.sports.naver.com/wbaseball/article/477/0000512065')  # success