# Google Chrome Terminal V1.5
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import requests
from bs4 import BeautifulSoup
import logging
import time

# Configure logging
logging.basicConfig(filename="search_program.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def print_welcome_message():
    print("=================== Google Chrome Terminal ===================\n")
    print("You can search the web using Google, display results in the terminal, and scrape content from webpages.\n")
    print("Follow the steps to perform a search.\n")
    print("==============================================================\n")

def get_search_query():
    query = input("Search query: ")
    return query

def fetch_google_results(query, start=0):
    url = f"https://www.google.com/search?q={query}&start={start}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    try:
        # Make an HTTP request to Google search page
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx/5xx responses
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching Google search results: {e}")
        print("Error fetching Google search results. Please try again.")
        return None

def parse_results(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Find all search result divs in Google
    result_divs = soup.find_all("div", class_="tF2Cxc")
    results = []
    
    for div in result_divs:
        title = div.find("h3")
        link = div.find("a")
        
        # Adding the link title here instead of the snippet
        link_title = link.get("title", "No title available")
        
        if title and link:
            result = {
                "title": title.get_text(),
                "url": link.get("href"),
                "link_title": link_title
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
        print(f"Link Title: {result['link_title']}")
        print(f"URL: {result['url']}")
        print("-" * 80)

def scrape_page_content(url):
    print(f"\nScraping content from: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for invalid responses
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract content from various elements for the entire page
        content = []
        
        # Collecting text from headings (h1, h2, h3, etc.)
        for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
            content.append(heading.get_text())
        
        # Collecting text from paragraphs (p)
        for paragraph in soup.find_all("p"):
            content.append(paragraph.get_text())
        
        # Collecting text from anchor tags (a), excluding the links
        for link in soup.find_all("a"):
            content.append(link.get_text())
        
        # Collecting text from lists (ul, ol)
        for list_item in soup.find_all(["ul", "ol"]):
            for li in list_item.find_all("li"):
                content.append(li.get_text())
        
        # Join all the collected content into a single string
        full_content = " ".join(content)
        
        return full_content
    except requests.RequestException as e:
        logging.error(f"Error scraping page {url}: {e}")
        return f"Error scraping page: {e}"

def scrape_multiple_pages(query, total_pages=3):
    all_results = []
    for page in range(total_pages):
        start = page * 10
        html_content = fetch_google_results(query, start)
        
        if html_content:
            results = parse_results(html_content)
            all_results.extend(results)
        time.sleep(2)  # To avoid hitting the server too quickly
    
    return all_results

def export_results(results, scraped_content, export_type="txt"):
    filename = input("Enter a filename to save the results: ")
    
    try:
        if export_type == "txt":
            with open(filename + ".txt", 'w', encoding='utf-8') as file:
                for index, result in enumerate(results, start=1):
                    file.write(f"{index}. {result['title']}\n")
                    file.write(f"Link Title: {result['link_title']}\n")
                    file.write(f"URL: {result['url']}\n")
                    file.write("-" * 80 + "\n")
                
                file.write("\nScraped Content:\n")
                file.write(scraped_content)
        elif export_type == "csv":
            with open(filename + ".csv", 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ["Title", "Link Title", "URL"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for result in results:
                    writer.writerow({"Title": result["title"], "Link Title": result["link_title"], "URL": result["url"]})
        elif export_type == "json":
            with open(filename + ".json", 'w', encoding='utf-8') as jsonfile:
                json.dump(results, jsonfile, indent=4)
        print(f"Results exported to {filename}")
    except Exception as e:
        logging.error(f"Error exporting results: {e}")
        print("Error exporting results. Please try again.")

def keep_going():
    print("\nWould you like to scrape content from another page?")
    print("1. Yes")
    print("2. No")
    choice = input("Enter the number corresponding to your choice: ")
    return choice

def main():
    print_welcome_message()
    
    while True:
        query = get_search_query()
        results = scrape_multiple_pages(query)

        if not results:
            print("No results found.")
            continue
        
        display_search_results(results)
        
        while True:
            choice = input("\nEnter the number of the result you want to scrape, or type 'exit' to quit: ")
            if choice.lower() == 'exit':
                break
                
            try:
                result_index = int(choice) - 1
                if 0 <= result_index < len(results):
                    url = results[result_index]["url"]
                    scraped_content = scrape_page_content(url)
                    print("\nMain content of the page:")
                    print(scraped_content[:1000])  # Print the first 1000 characters for brevity
                    
                    # Ask the user if they want to export results
                    export_choice = input("\nWould you like to export the results? (y/n): ")
                    if export_choice.lower() == 'y':
                        export_type = input("Enter export type (txt, csv, json): ")
                        export_results(results, scraped_content, export_type)
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number or 'exit'.")
            
            # Prompt to continue scraping or not
            continue_choice = keep_going()
            if continue_choice != "1":
                break
        
        print("Returning to main menu.")
    
if __name__ == "__main__":
    main()