import requests
import json

from common_functions import extract_info, remove_unneedful_tags

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        return html
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_info_and_print(url):
    html = remove_unneedful_tags(get_html(url))
    if html:
        info = extract_info(html)
        if info:
            print(json.dumps(info, indent=4))


get_info_and_print('https://ai.google.dev/competition')  # success
get_info_and_print("https://m.sports.naver.com/wbaseball/article/477/0000512065")  # fail