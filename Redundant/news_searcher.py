import time
import json

# Pseudo function to get the latest news links. Replace with actual API calls.
def get_latest_news():
    # This would be replaced with an API call to a news service.
    news_links = ["https://news_link_1.com", "https://news_link_2.com"]
    return news_links

def save_to_file(news_links):
    with open("data.txt", "a") as file:
        for link in news_links:
            file.write(link + "\n")

def main():
    while True:
        news_links = get_latest_news()
        save_to_file(news_links)
        time.sleep(10)  # Wait for 10 seconds before the next operation

if __name__ == "__main__":
    main()
