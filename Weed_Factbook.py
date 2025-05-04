# Weed Factbook V1.0
# Copyright (C) 2024, Sourceduty - All Rights Reserved.

import sys

def print_help_menu():
    print("Main Menu\n")
    print("1. Cultivation")
    print("2. Business and Sales")
    print("3. Packaging")
    print("4. Consumption")
    print("5. Help")
    print("6. Exit\n")
    print("-----------------------------------------------------------\n")
    print("Enter the number corresponding to your choice to learn more.")

def cultivation_info():
    print("Weed Cultivation Information\n")
    print("1. Soil Requirements: Cannabis thrives in well-draining, nutrient-rich soil.")
    print("2. Light: Requires 12-18 hours of light during vegetative growth.")
    print("3. Temperature: Ideal range is 70-85°F (21-29°C).")
    print("4. Humidity: Optimal levels vary by growth stage (e.g., 40-70%).")
    print("5. Watering: Consistent watering without over-saturating the soil.")
    print("6. Nutrients: Balanced fertilizers with nitrogen, phosphorus, and potassium.")
    print("7. Harvesting: Usually occurs 6-12 weeks after flowering begins.")

def business_sales_info():
    print("Weed Business and Sales Information\n")
    print("1. Licensing: Check local laws for cultivation, production, and sales permits.")
    print("2. Market Analysis: Understand target demographics and industry trends.")
    print("3. Product Types: Offer flower, edibles, concentrates, and topicals.")
    print("4. Compliance: Adhere to packaging, labeling, and advertising regulations.")
    print("5. Security: Implement inventory control and secure storage measures.")
    print("6. Marketing: Focus on branding, social media, and community engagement.")
    print("7. Taxes: Understand state and federal tax obligations for cannabis businesses.")

def packaging_info():
    print("Weed Packaging Information\n")
    print("1. Compliance: Packaging must be child-resistant, tamper-proof, and resealable.")
    print("2. Labeling: Include THC/CBD content, usage instructions, and health warnings.")
    print("3. Sustainability: Use recyclable or biodegradable materials if possible.")
    print("4. Branding: Design visually appealing and professional packaging.")
    print("5. Storage: Ensure packaging maintains product freshness and potency.")
    print("6. Regulations: Follow local laws for packaging size and labeling language.")

def consumption_info():
    print("Weed Consumption Information\n")
    print("1. Smoking: Traditional method using joints, pipes, or bongs.")
    print("2. Vaping: Heating cannabis oil or flower to inhale vapor.")
    print("3. Edibles: Infused foods and drinks with delayed effects (30-120 minutes).")
    print("4. Topicals: Cannabis-infused creams and balms for localized relief.")
    print("5. Tinctures: Concentrated cannabis extracts taken sublingually.")
    print("6. Dosage: Start low and go slow, especially for new users.")
    print("7. Effects: Vary by strain and consumption method (e.g., relaxation or focus).")

def main():
    print("Weed Factbook")
    print("-----------------------------------------------------------\n")
    print_help_menu()
    
    while True:
        try:
            choice = int(input("\n> "))
            if choice == 1:
                cultivation_info()
            elif choice == 2:
                business_sales_info()
            elif choice == 3:
                packaging_info()
            elif choice == 4:
                consumption_info()
            elif choice == 5:
                print_help_menu()
            elif choice == 6:
                print("Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please select a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()