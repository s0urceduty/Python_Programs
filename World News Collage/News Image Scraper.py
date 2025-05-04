# News Images

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import time

# List of news websites with subdomains
news_sites = {
    "NY Times": ["https://www.nytimes.com", "https://cooking.nytimes.com"],
    "CNN": ["https://edition.cnn.com", "https://money.cnn.com"],
    "Reuters": ["https://www.reuters.com", "https://graphics.reuters.com"],
    "BBC": ["https://www.bbc.com", "https://news.bbc.co.uk"],
    "WSJ": ["https://www.wsj.com", "https://blogs.wsj.com"],
    "Fox News": ["https://www.foxnews.com", "https://video.foxnews.com"],
    "NPR": ["https://www.npr.org", "https://text.npr.org"],
    "Google News": ["https://news.google.com", "https://news.google.com/covid19"],
    "Yahoo News": ["https://news.yahoo.com", "https://news.yahoo.com/politics"],
    "NBC News": ["https://www.nbcnews.com", "https://www.nbcnews.com/pop-culture"]
}

# Directory to save images
output_dir = "news_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def is_valid_image(url):
    """Check if URL is valid and points to an image."""
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme) and url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))

def download_image(url, folder):
    """Download image and save to folder."""
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            filename = os.path.join(folder, os.path.basename(urlparse(url).path))
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download image: {url}")
    except Exception as e:
        print(f"Error: {e}")

def scrape_images_from_site(website_url, site_name):
    """Scrape images from a specific site."""
    print(f"Scraping images from {site_name} - {website_url}")
    try:
        response = requests.get(website_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        image_tags = soup.find_all('img')
        
        for img in image_tags:
            img_url = img.attrs.get('src') or img.attrs.get('data-src')
            if img_url:
                img_url = urljoin(website_url, img_url)
                if is_valid_image(img_url):
                    download_image(img_url, output_dir)
        time.sleep(1)  # To avoid making too many requests in a short time
    except Exception as e:
        print(f"Failed to scrape {site_name}: {e}")

# Start scraping process
for site_name, urls in news_sites.items():
    for url in urls:
        scrape_images_from_site(url, site_name)

print("Image scraping completed.")
