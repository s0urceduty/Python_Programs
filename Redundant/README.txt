### Redundant

👥 Python data concept for experimental redundancy.

### CONCEPT

Two similar scripts run and save data simultaneously on command. The first script's operation is followed by the second script that repeats the same operation as the first script and also advances the first script.

### CODE

Script 1: news_searcher.py

This script is responsible for periodically fetching the latest news article links that pertain to North American news. It simulates an API call to a news service provider and saves the retrieved links to a file named data.txt.

Script 2: news_searcher_advancer.py

This script performs the same operations as the first script—fetching and saving news links—but it also contains a mechanism to "advance" the operation of the first script, potentially by signaling it to fetch new data or to perform the next step in its operation.

#

Script 1: The Search Initiator (searcher.py)

The first script, searcher.py, acts as the search initiator. It uses the Google Custom Search JSON API to query the latest articles on British history. Upon receiving the search results, the script writes the article links to a file named data.txt. This script runs in a loop, performing a new search every 60 seconds, ensuring that the most recent content is continually sought out.

Key Features:

1. API Simulation

The script contains a function get_latest_news() which is a placeholder for an actual API call to a news service. This function is expected to return a list of URLs as strings.

2. Data Persistence

It includes a function save_to_file(news_links) that takes the list of news links and appends them to data.txt, ensuring that each link is on a new line.

3. Periodic Operation

The main() function orchestrates the script's operation in an infinite loop, calling get_latest_news() and save_to_file(news_links) every 10 seconds.

Synchronization and Coordination:

The script runs indefinitely and is designed to be executed in parallel with another script. It does not include any advanced concurrency mechanisms but relies on the file system to handle concurrent writes to data.txt.

#

Script 2: The Search Follower (follower.py)

The second script, follower.py, is designed to detect when searcher.py has updated the data.txt file with new search results. Once it notices a change in the file size (indicating new content), it reads the updated data. It can then perform its own search to gather additional results or process the existing links further. This script checks for updates every 30 seconds and can be programmed to trigger searcher.py for another search iteration, creating a responsive and dynamic search system.

Key Features:

1. API Simulation: 

Similar to the first script, it simulates fetching news links with a get_latest_news() function, which should be replaced with an actual API call.

2. Data Persistence: 

It also appends the fetched news links to the same data.txt file using the save_to_file(news_links) function.

3. Advancing Mechanism: 

The script includes an advance_first_script() function, which is a placeholder for an inter-process communication (IPC) mechanism. This function is intended to signal the first script to perform its next operation or to fetch new data.

Synchronization and Coordination:

This script also runs indefinitely and is designed to work in tandem with the first script. It must handle the file access in a thread-safe manner to avoid conflicts with the first script.

#

Concurrency Considerations: 

This script also runs indefinitely and is designed to work in tandem with the first script. It must handle the file access in a thread-safe manner to avoid conflicts with the first script.

#

Setup Requirements:

A valid Google API key and a custom search engine ID are required to use the Google Custom Search JSON API.

The googleapiclient.discovery library must be installed to run these scripts.

### SCRIPTS

Using two scripts instead of one can enhance concurrency, modularity, and error handling, allowing for simultaneous operations and clearer separation of tasks. This approach can lead to better maintainability, scalability, reliability and testing, as well as more efficient resource management. Redundancy adds together and equals more reliability. It also allows for flexible scheduling and can speed up development in team settings. However, it's important to manage the added complexity and ensure proper coordination to prevent inconsistencies. 
