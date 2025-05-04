# Google Chrome Terminal V1.0
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import requests
from bs4 import BeautifulSoup

def print_welcome_message():
    print("Welcome to the Google Search Program!")
    print("You can use this program to search the web and display results in the terminal.")
    print("Follow the steps to perform a search.")

def get_search_query():
    query = input("Enter your search query: ")
    return query

def select_search_engine():
    print("\nSelect the search engine to use:")
    print("1. Google")
    print("2. Exit")
    choice = input("Enter the number corresponding to your choice: ")
    return choice

def fetch_google_results(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    # Make an HTTP request to Google search page
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve search results.")
        return None

def parse_results(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Find all search result divs
    result_divs = soup.find_all("div", class_="tF2Cxc")
    results = []
    
    for div in result_divs:
        title = div.find("h3")
        link = div.find("a")
        snippet = div.find("span", class_="aCOpRe")
        
        if title and link:
            result = {
                "title": title.get_text(),
                "url": link.get("href"),
                "snippet": snippet.get_text() if snippet else "No snippet available"
            }
            results.append(result)
    
    return results

def display_search_results(results):
    if not results:
        print("No results found.")
        return
    
    print("\nSearch Results:")
    for index, result in enumerate(results, start=1):
        print(f"{index}. {result['title']}")
        print(f"URL: {result['url']}")
        print(f"Snippet: {result['snippet']}")
        print("-" * 80)

def main():
    print_welcome_message()
    while True:
        choice = select_search_engine()
        
        if choice == "1":
            query = get_search_query()
            html_content = fetch_google_results(query)
            
            if html_content:
                results = parse_results(html_content)
                display_search_results(results)
                break
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
