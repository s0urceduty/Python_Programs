# Hacker Wiki Terminal V1.0
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import sys

# Data storage for the wiki entries
wiki_entries = {
    'Hacking Techniques': {
        'Phishing': 'A social engineering method to trick users into revealing personal information.',
        'SQL Injection': 'Techniques that exploit vulnerabilities in SQL databases to manipulate data.',
        'Cross-Site Scripting (XSS)': 'Involves injecting malicious scripts into trusted websites to bypass access controls.',
        'Buffer Overflow': 'A common software vulnerability that occurs when more data is written to a buffer than it can hold.',
        'Spoofing': 'Includes various forms such as IP, ARP, and DNS spoofing, each involving impersonation of another device.',
        'Man-in-the-Middle Attack': 'A cyber attack where the attacker secretly intercepts and relays communication between two parties.',
        'Denial-of-Service (DoS)': 'An attack intended to make a service unavailable by overwhelming it with traffic.',
        'Distributed Denial-of-Service (DDoS)': 'A DoS attack that uses multiple systems to flood the target with traffic.',
        'Privilege Escalation': 'The act of exploiting a vulnerability to gain elevated access to system resources.',
        'Zero-Day Exploit': 'An attack that exploits a previously unknown vulnerability in software.',
        'Rootkit': 'A type of malicious software designed to gain unauthorized access to a computer system while concealing its existence.',
        'Trojan Horse': 'Malicious software disguised as legitimate software, often used to create backdoors for hackers.',
        'Ransomware': 'Malware that locks or encrypts a user’s files and demands a ransom for their release.',
        'Keylogger': 'Software that records the keystrokes of a user, often used to steal sensitive information.',
        'Credential Stuffing': 'The use of stolen username and password pairs to gain unauthorized access to user accounts.',
        'Cryptojacking': 'The unauthorized use of someone’s computing resources to mine cryptocurrency.',
        'Brute Force Attack': 'A trial-and-error method used to decode encrypted data such as passwords.',
        'Clickjacking': 'A malicious technique that tricks a user into clicking something different from what they intended.',
        'Session Hijacking': 'The exploitation of a web session to gain unauthorized access to a web server or service.',
        'DNS Spoofing': 'A type of attack where the attacker corrupts the DNS cache to redirect a victim to malicious websites.'
    },
    'Hacker Culture': {
        'Hackathons': 'Competitive events where programmers develop new software projects within a short period.',
        'Open Source': 'The practice of making the source code of a software available freely so that anyone can modify or enhance it.',
        'The Cathedral and the Bazaar': 'Key essays by Eric S. Raymond on open-source software development models.',
        'Hacker Ethic': 'Core principles include accessibility, freedom of information, and improvement to quality of life.',
        'Crypto-anarchism': 'Philosophy promoting the use of cryptography to enforce privacy and political freedom.',
        'Underground Economy': 'The illegal trade of data, software, and services that facilitate hacking.',
        'Dark Web': 'A part of the internet that requires special software to access and often hosts illicit activities.',
        'White Hat Hacker': 'A hacker who uses their skills for ethical and legal purposes, often to find vulnerabilities and report them.',
        'Black Hat Hacker': 'A hacker who uses their skills for malicious and illegal purposes, typically for personal gain.',
        'Gray Hat Hacker': 'A hacker who may violate ethical standards or laws but without the intention of causing harm.',
        'Hacktivism': 'Using hacking to promote political, social, or environmental causes.',
        'Script Kiddie': 'A derogatory term for an inexperienced or unskilled hacker who uses existing tools or scripts created by others.',
        'Ethical Hacking': 'The practice of testing systems for vulnerabilities with the permission of the system owner.',
        'Penetration Testing': 'A simulated cyberattack used to assess the security of a system or network.',
        'Security Auditing': 'The process of evaluating a system’s security by reviewing its infrastructure, policies, and controls.',
        'Cybersecurity Awareness': 'Training and initiatives to help individuals and organizations understand security risks and best practices.',
        'Digital Footprint': 'The trail of data left by users’ online activities, including browsing history, social media posts, and communications.',
        'Social Engineering': 'The use of deception to manipulate individuals into divulging confidential information.',
        'Cryptocurrency': 'A digital or virtual form of currency that uses cryptography for security, often used in illicit transactions.',
        'Deep Web': 'The portion of the web that is not indexed by search engines and requires special tools or credentials to access.'
    },
    'Famous Hacks': {
        'The Morris Worm': 'The first computer worm on the internet which inadvertently caused widespread damage.',
        'Operation Aurora': 'A series of cyber attacks in 2009 aimed at stealing intellectual property from high-profile companies.',
        'Stuxnet': "Sophisticated malware that targeted industrial control systems in Iran's nuclear facilities.",
        'Sony Pictures Hack': 'A significant breach in 2014 that led to major leaks of personal information and corporate data.',
        'The DNC Hack': 'Cyber attacks during the 2016 U.S. election cycle targeting the Democratic National Committee.',
        'Target Data Breach': 'A 2013 attack that exposed credit and debit card information of 40 million customers.',
        'Yahoo Data Breach': 'A breach in 2013-2014 that exposed personal information of 3 billion Yahoo users.',
        'Ashley Madison Hack': 'A 2015 attack on the extramarital affair website that exposed sensitive user data.',
        'Equifax Data Breach': 'A 2017 hack that exposed personal and financial data of 147 million Americans.',
        'WannaCry Ransomware Attack': 'A global ransomware attack in 2017 that affected more than 200,000 systems.',
        'NotPetya Ransomware Attack': 'A destructive ransomware attack in 2017 that primarily targeted Ukraine but spread globally.',
        'The ILOVEYOU Virus': 'A 2000 computer virus spread via email that caused significant damage worldwide.',
        'Stuxnet Attack on Iran': 'A sophisticated cyber attack that targeted Iran’s nuclear facilities, reportedly developed by the U.S. and Israel.',
        'The Panama Papers Leak': 'A massive leak of financial documents that exposed offshore tax havens used by politicians and business leaders.',
        'Facebook Data Breach': 'A 2018 breach involving Cambridge Analytica that exposed millions of Facebook users’ data.',
        'The WannaCry Attack': 'A ransomware attack that used an NSA tool to infect Windows computers and demand a ransom.',
        'Operation Shady RAT': 'A global cyber espionage campaign that lasted from 2006 to 2011, involving multiple countries and organizations.',
        'The Capital One Breach': 'A 2019 data breach that exposed over 100 million Capital One customers’ data.',
        'The LinkedIn Breach': 'A 2012 breach that exposed personal data of 6.5 million LinkedIn users.',
        'Uber Data Breach': 'A 2016 hack that exposed personal information of 57 million Uber users and drivers.'
    },
    'Security Tools': {
        'Firewalls': 'Hardware or software solutions that block unauthorized access to networks.',
        'Antivirus Software': 'Programs that protect computers from malware such as viruses, worms, and trojans.',
        'Intrusion Detection Systems (IDS)': 'Tools that monitor network traffic for suspicious activities and known threats.',
        'Cryptographic Tools': 'Includes encryption algorithms, cryptographic protocols, and key management systems.',
        'Network Scanners': 'Software tools that assess and analyze network infrastructure for vulnerabilities.',
        'Virtual Private Network (VPN)': 'A service that encrypts internet traffic and routes it through a remote server to hide the user’s IP address.',
        'Encryption Algorithms': 'Mathematical procedures used to encode data, ensuring confidentiality during transmission.',
        'Wireshark': 'A network protocol analyzer that helps in capturing and analyzing packets of data on a network.',
        'Metasploit': 'A penetration testing tool used to exploit known vulnerabilities in systems.',
        'Nmap': 'A network scanning tool used to discover hosts and services on a computer network.',
        'Kali Linux': 'A Debian-based Linux distribution that includes tools for penetration testing, security research, and digital forensics.',
        'Aircrack-ng': 'A tool used to crack WEP and WPA-PSK keys, commonly used for Wi-Fi network security testing.',
        'John the Ripper': 'A password cracking software tool designed to identify weak passwords in a system.',
        'Hydra': 'A fast network logon cracker that supports numerous protocols.',
        'Burp Suite': 'A suite of tools for web application security testing, including a proxy and vulnerability scanner.',
        'OpenVAS': 'An open-source vulnerability scanner that detects security issues in network systems.',
        'ClamAV': 'An open-source antivirus engine for detecting malware and viruses.',
        'Fail2ban': 'A software tool that helps protect servers from brute force attacks by banning IP addresses after failed login attempts.',
        'Shodan': 'A search engine for internet-connected devices, often used for security research.',
        'ZAP Proxy': 'An open-source web application security scanner used for penetration testing.'
    },
    'Programming and Development': {
        'Python': 'A high-level programming language known for its readability and use in web development, data science, and automation.',
        'JavaScript': 'A scripting language that enables dynamic content on websites and is essential for front-end development.',
        'C++': 'A general-purpose programming language that is widely used in software development, game development, and system programming.',
        'Ruby': 'A dynamic, object-oriented programming language used for web development, particularly with the Ruby on Rails framework.',
        'Go': 'A statically typed, compiled programming language designed for system programming and scalable web services.',
        'Rust': 'A systems programming language that aims to provide memory safety, concurrency, and performance.',
        'Java': 'A class-based, object-oriented programming language widely used for building platform-independent applications.',
        'PHP': 'A server-side scripting language commonly used for web development and creating dynamic web pages.',
        'Swift': 'A powerful and intuitive programming language used to develop applications for iOS, macOS, and more.',
        'Kotlin': 'A modern, statically typed programming language designed to be fully interoperable with Java, commonly used for Android development.',
        'Ruby on Rails': 'A web application framework written in Ruby, known for its simplicity and developer-friendly design.',
        'Django': 'A high-level Python web framework that encourages rapid development and clean, pragmatic design.',
        'Flask': 'A micro web framework written in Python that is lightweight and easy to use for small web applications.',
        'Node.js': 'A runtime environment that allows for server-side programming in JavaScript, known for its performance and scalability.',
        'TypeScript': 'A superset of JavaScript that adds static types to the language, enabling better code quality and tooling support.',
        'HTML': 'The standard markup language for creating web pages, used to structure content on the web.',
        'CSS': 'A stylesheet language used to describe the presentation of a document written in HTML or XML.',
        'SASS': 'A preprocessor scripting language that extends CSS with features like variables, nested rules, and mixins.',
        'SQL': 'A domain-specific language used to manage and manipulate relational databases.'
    }
}

def print_help_menu():
    print("Hacker Wiki\n")
    print("1. View Wiki Entry")
    print("2. Add Wiki Entry")
    print("3. Update Wiki Entry")
    print("4. Delete Wiki Entry")
    print("5. Search Wiki Entry")
    print("6. Export Wiki to File")
    print("7. Import Wiki from File")
    print("8. View Specific Entry by Name")
    print("9. Manage Categories")
    print("10. Help")
    print("11. Exit\n")
    print("-----------------------------------------------------------\n")
    print("Enter the number corresponding to your choice.")
    print("Press 'M' at any time to return to the main menu.\n")

def display_categories():
    print("Categories:")
    for index, category in enumerate(wiki_entries, start=1):
        print(f"{index}. {category}")

def view_entry():
    display_categories()
    category = input("Select the category number to view entries or 'M' to return to the main menu: ").strip().upper()
    if category == 'M':
        return
    try:
        category_index = int(category) - 1
        category_name = list(wiki_entries.keys())[category_index]
        print(f"\n{category_name} Entries:")
        for entry, description in wiki_entries[category_name].items():
            print(f"{entry}: {description}")
    except (ValueError, IndexError):
        print("Invalid category number.")

def add_entry():
    display_categories()
    category = input("Select the category number to add an entry or 'M' to return to the main menu: ").strip().upper()
    if category == 'M':
        return
    try:
        category_index = int(category) - 1
        category_name = list(wiki_entries.keys())[category_index]
        entry_name = input("Enter the name of the new entry: ")
        entry_description = input("Enter the description of the new entry: ")
        wiki_entries[category_name][entry_name] = entry_description
        print("Entry added successfully.")
    except (ValueError, IndexError):
        print("Invalid category number.")

def update_entry():
    display_categories()
    category = input("Select the category number to update an entry or 'M' to return to the main menu: ").strip().upper()
    if category == 'M':
        return
    try:
        category_index = int(category) - 1
        category_name = list(wiki_entries.keys())[category_index]
        print("Existing entries:")
        for entry in wiki_entries[category_name]:
            print(entry)
        entry_name = input("Enter the name of the entry to update: ")
        new_description = input("Enter the new description: ")
        if entry_name in wiki_entries[category_name]:
            wiki_entries[category_name][entry_name] = new_description
            print("Entry updated successfully.")
        else:
            print("Entry not found.")
    except (ValueError, IndexError):
        print("Invalid category number.")

def delete_entry():
    display_categories()
    category = input("Select the category number to delete an entry or 'M' to return to the main menu: ").strip().upper()
    if category == 'M':
        return
    try:
        category_index = int(category) - 1
        category_name = list(wiki_entries.keys())[category_index]
        print("Existing entries:")
        for entry in wiki_entries[category_name]:
            print(entry)
        entry_name = input("Enter the name of the entry to delete: ")
        if entry_name in wiki_entries[category_name]:
            del wiki_entries[category_name][entry_name]
            print("Entry deleted successfully.")
        else:
            print("Entry not found.")
    except (ValueError, IndexError):
        print("Invalid category number.")

def search_entry():
    keyword = input("Enter a keyword to search for in the wiki: ").strip().lower()
    found = False
    for category, entries in wiki_entries.items():
        for entry, description in entries.items():
            if keyword in entry.lower() or keyword in description.lower():
                print(f"Category: {category}")
                print(f"{entry}: {description}")
                print("-----------------------------------------------------------")
                found = True
    if not found:
        print("No entries found matching that keyword.")

def export_wiki():
    filename = input("Enter the filename to export the wiki to (e.g., wiki.txt): ").strip()
    with open(filename, 'w') as file:
        for category, entries in wiki_entries.items():
            file.write(f"Category: {category}\n")
            for entry, description in entries.items():
                file.write(f"{entry}: {description}\n")
            file.write("\n")
    print(f"Wiki exported successfully to {filename}.")

def import_wiki():
    filename = input("Enter the filename to import the wiki from (e.g., wiki.txt): ").strip()
    try:
        with open(filename, 'r') as file:
            category = None
            for line in file:
                line = line.strip()
                if line.startswith("Category:"):
                    category = line.split(":")[1].strip()
                    if category not in wiki_entries:
                        wiki_entries[category] = {}
                elif line and ':' in line:
                    entry, description = line.split(":", 1)
                    wiki_entries[category][entry.strip()] = description.strip()
            print(f"Wiki imported successfully from {filename}.")
    except FileNotFoundError:
        print(f"File {filename} not found.")

def view_specific_entry():
    entry_name = input("Enter the name of the entry to view: ").strip()
    found = False
    for category, entries in wiki_entries.items():
        if entry_name in entries:
            print(f"\n{category} - {entry_name}: {entries[entry_name]}")
            found = True
            break
    if not found:
        print("Entry not found.")

def manage_categories():
    print("\nCategory Management:")
    print("1. Add Category")
    print("2. Delete Category")
    choice = input("Choose an option (1 or 2): ").strip()
    if choice == '1':
        new_category = input("Enter the name of the new category: ").strip()
        if new_category not in wiki_entries:
            wiki_entries[new_category] = {}
            print(f"Category '{new_category}' added successfully.")
        else:
            print("Category already exists.")
    elif choice == '2':
        display_categories()
        category_to_delete = input("Enter the category name to delete: ").strip()
        if category_to_delete in wiki_entries:
            del wiki_entries[category_to_delete]
            print(f"Category '{category_to_delete}' deleted successfully.")
        else:
            print("Category not found.")
    else:
        print("Invalid choice.")

def main():
    print_help_menu()
    while True:
        try:
            choice = input("\n> ").strip().upper()
            if choice == 'M':
                print_help_menu()
            elif choice == '1':
                view_entry()
            elif choice == '2':
                add_entry()
            elif choice == '3':
                update_entry()
            elif choice == '4':
                delete_entry()
            elif choice == '5':
                search_entry()
            elif choice == '6':
                export_wiki()
            elif choice == '7':
                import_wiki()
            elif choice == '8':
                view_specific_entry()
            elif choice == '9':
                manage_categories()
            elif choice == '10':
                print_help_menu()
            elif choice == '11':
                print("Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please select a number between 1 and 11 or press 'M' to return to the main menu.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'M' to return to the main menu.")

if __name__ == "__main__":
    main()