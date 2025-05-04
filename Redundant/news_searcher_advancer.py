import time
import json
import os

# Pseudo function to get the latest news links. Replace with actual API calls.
def get_latest_news():
    # This would be replaced with an API call to a news service.
    news_links = ["https://news_link_3.com", "https://news_link_4.com"]
    return news_links

def save_to_file(news_links):
    with open("data.txt", "a") as file:
        for link in news_links:
            file.write(link + "\n")

def advance_first_script():
    # This would need to be an IPC mechanism or a signaling method to tell
    # the first script to perform its next operation.
    pass

def main():
    while True:
        news_links = get_latest_news()
        save_to_file(news_links)
        advance_first_script()  # Signal the first script to advance
        time.sleep(10)  # Wait for 10 seconds before the next operation

if __name__ == "__main__":
    main()
