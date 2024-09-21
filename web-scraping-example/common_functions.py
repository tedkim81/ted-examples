from bs4 import BeautifulSoup
import re

def extract_info(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        title_tag = soup.find('meta', property='og:title')
        if title_tag and 'content' in title_tag.attrs:
            title = title_tag['content']
        else:
            title_tag = soup.find('title')
            title = title_tag.string
        
        description_tag = soup.find('meta', property='og:description')
        if description_tag and 'content' in description_tag.attrs:
            description = description_tag['content']
        else:
            description = None

        image_tag = soup.find('meta', property='og:image')
        if image_tag and 'content' in image_tag.attrs:
            image = image_tag['content']
        else:
            image = None
            img_tags = soup.find_all('img')
            for img_tag in img_tags:
                if 'src' in img_tag.attrs and img_tag['src'].startswith('https'):
                    image = img_tag['src']
                    break
        return {'title': title, 'description': description, 'image': image}
    except Exception as e:
        print(f"Error extracting info from HTML: {e}")
        return None

def remove_unneedful_tags(html):
    cleaned_html = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', html)
    cleaned_html = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', cleaned_html)
    cleaned_html = re.sub(r'<path\b[^<]*(?:(?!<\/path>)<[^<]*)*<\/path>', '', cleaned_html)
    cleaned_html = re.sub(r'<a\b[^<]*(?:(?!<\/a>)<[^<]*)*<\/a>', '', cleaned_html)
    cleaned_html = re.sub(r'<button\b[^<]*(?:(?!<\/button>)<[^<]*)*<\/button>', '', cleaned_html)
    cleaned_html = re.sub(r'class=\"[^\"]*\"', '', cleaned_html)
    return cleaned_html