import json
from playwright.sync_api import sync_playwright
import time

from common_functions import extract_info, remove_unneedful_tags

# Run the `playwright install` command to install the browser.

def get_html(url):
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto(url)
        html = page.content()
        current_size = len(html)

        # Wait for the page content to load
        for _ in range(5):
            time.sleep(1)
            content = page.content()
            if len(content) != current_size:
                html = content
                break

        browser.close()

    return html

def get_info_and_print(url):
    html = remove_unneedful_tags(get_html(url))
    if html:
        info = extract_info(html)
        if info:
            print(json.dumps(info, indent=4))


get_info_and_print('https://ai.google.dev/competition')  # success
get_info_and_print('https://m.sports.naver.com/wbaseball/article/477/0000512065')  # success