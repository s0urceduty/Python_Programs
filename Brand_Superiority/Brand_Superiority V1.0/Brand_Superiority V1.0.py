# Brand_Superiority V1.0

# 📈 Rating and comparing global business brand attributes for superiority.

# ChatGPT provided generalized brand attribute ratings based on global presence, market reputation, and known innovation practices up to it's last update in April 2023.

# Copyright (C) 2023, Sourceduty - All Rights Reserved.
# THE CONTENTS OF THIS PROJECT ARE PROPRIETARY.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Brand names data
brand_attributes = {
    "Apple": {
        "trustworthiness": 9.0,
        "relevance": 9.1,
        "innovation": 9.2,
        "uniqueness": 9.1,
        "convenience": 9.0,
        "overall_rating": 8.6,
        "description": "Highly regarded for its innovative technology, unique design aesthetics, and user-friendly ecosystem, which foster trust and relevance. Its product convenience is enhanced by seamless integration across its devices and services."
    },
    "Amazon": {
        "trustworthiness": 8.7,
        "relevance": 9.0,
        "innovation": 9.2,
        "uniqueness": 8.4,
        "convenience": 9.3,
        "overall_rating": 8.8,
        "description": "A paradigm of convenience with its vast product range and swift delivery. Amazon's constant innovation, particularly in cloud computing and logistics, underpins its relevance and builds consumer trust."
    },
    "Facebook (Meta Platforms)": {
        "trustworthiness": 7.1,
        "relevance": 8.4,
        "innovation": 8.0,
        "uniqueness": 7.9,
        "convenience": 7.5,
        "overall_rating": 7.6,
        "description": "Offers convenient social networking and is striving to be innovative with its focus on VR. Its relevance is high, though trust varies with public sentiment on privacy and content management."
    },
    "Walmart": {
        "trustworthiness": 8.1,
        "relevance": 8.0,
        "innovation": 7.9,
        "uniqueness": 7.7,
        "convenience": 8.3,
        "overall_rating": 8.0,
        "description": "Combines convenience with a broad retail presence and e-commerce platform. Its trustworthiness is supported by strong customer service, and it stays relevant and innovative through tech-driven shopping solutions."
    },
    "ICBC": {
        "trustworthiness": 8.0,
        "relevance": 7.7,
        "innovation": 7.6,
        "uniqueness": 7.5,
        "convenience": 7.9,
        "overall_rating": 7.8,
        "description": "Trusted within its market, offering relevant financial services. It's enhancing convenience through digital banking, reflecting a commitment to innovation in the financial sector."
    },
    "Verizon": {
        "trustworthiness": 8.1,
        "relevance": 7.9,
        "innovation": 7.8,
        "uniqueness": 7.5,
        "convenience": 8.0,
        "overall_rating": 7.8,
        "description": "A trustworthy provider of telecommunications, relevant for its broad service offerings. It's innovating with 5G technology and focuses on convenience with various consumer plans."
    },
    "China Construction Bank": {
        "trustworthiness": 8.0,
        "relevance": 7.8,
        "innovation": 7.7,
        "uniqueness": 7.5,
        "convenience": 7.8,
        "overall_rating": 7.6,
        "description": "Trusted for its financial services in China, relevant to its vast customer base, with a push toward convenience and innovation through digital banking technologies."
    },
    "AT&T": {
        "trustworthiness": 8.1,
        "relevance": 7.9,
        "innovation": 7.7,
        "uniqueness": 7.6,
        "convenience": 7.9,
        "overall_rating": 7.8,
        "description": "Trustworthy in telecommunications, relevant for its range of services, and innovative with media and digital solutions, aiming to increase convenience for customers."
    },
    "Toyota": {
        "trustworthiness": 8.5,
        "relevance": 8.2,
        "innovation": 8.3,
        "uniqueness": 8.1,
        "convenience": 8.0,
        "overall_rating": 8.2,
        "description": "Trusted for manufacturing reliable vehicles and relevant for its pioneering hybrid technology. Toyota's innovation in automotive tech enhances the convenience and uniqueness of its brand."
    },
    "Coca-Cola": {
        "trustworthiness": 8.2,
        "relevance": 8.1,
        "innovation": 7.9,
        "uniqueness": 8.3,
        "convenience": 8.2,
        "overall_rating": 8.0,
        "description": "A trusted beverage brand known for its unique flavor, staying relevant through a diverse product range and innovative marketing campaigns, ensuring global convenience and recognition."
    },
    "Mercedes-Benz": {
        "trustworthiness": 8.6,
        "relevance": 8.5,
        "innovation": 8.7,
        "uniqueness": 8.9,
        "convenience": 8.2,
        "overall_rating": 8.4,
        "description": "Synonymous with trust in the automotive industry, Mercedes-Benz's relevance is underscored by its luxury status, innovative technology, and unique brand prestige."
    },
    "Disney": {
        "trustworthiness": 8.8,
        "relevance": 9.0,
        "innovation": 8.7,
        "uniqueness": 8.9,
        "convenience": 8.8,
        "overall_rating": 8.7,
        "description": "A leader in entertainment trusted for its family-friendly content. Its relevance spans generations, with innovative storytelling and unique character IPs offering convenient access through various media platforms."
    }
}

# GUI implementation
class BrandComparisonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Brand Comparison Tool")
        self.root.geometry("1000x800")  # Set the initial size of the window

        # Brand selection frames
        self.frame1 = ttk.Frame(self.root)
        self.frame1.pack(padx=10, pady=5, fill='x', expand=True)

        self.frame2 = ttk.Frame(self.root)
        self.frame2.pack(padx=10, pady=5, fill='x', expand=True)

        # Dropdown for first brand
        self.brand1_label = ttk.Label(self.frame1, text="Select Brand 1:")
        self.brand1_label.pack(side='left', padx=5, pady=5)
        self.brand1 = ttk.Combobox(self.frame1, values=list(brand_attributes.keys()), state="readonly")
        self.brand1.pack(side='left', fill='x', expand=True, padx=5, pady=5)

        # Dropdown for second brand
        self.brand2_label = ttk.Label(self.frame2, text="Select Brand 2:")
        self.brand2_label.pack(side='left', padx=5, pady=5)
        self.brand2 = ttk.Combobox(self.frame2, values=list(brand_attributes.keys()), state="readonly")
        self.brand2.pack(side='left', fill='x', expand=True, padx=5, pady=5)

        # Compare button
        self.compare_button = ttk.Button(self.root, text="Compare", command=self.compare_brands)
        self.compare_button.pack(padx=10, pady=10)

        # Result display
        self.result_text = tk.Text(self.root, height=30, width=150, state='disabled')  # Adjusted size
        self.result_text.pack(padx=10, pady=10)

    def compare_brands(self):
        # Get selected brand names
        brand1_name = self.brand1.get()
        brand2_name = self.brand2.get()

        # Validate if two different brands are selected
        if not brand1_name or not brand2_name or brand1_name == brand2_name:
            messagebox.showerror("Error", "Please select two different brands.")
            return

        # Fetch brand data
        brand1_data = brand_attributes[brand1_name]
        brand2_data = brand_attributes[brand2_name]

        # Prepare the comparison report
        comparison_report = f"Comparing {brand1_name} vs {brand2_name}\n\n"
        attributes = ['trustworthiness', 'relevance', 'innovation', 'uniqueness', 'convenience', 'overall_rating']
        
        superior_brand = None  # Variable to store the name of the superior brand based on overall_rating
        for attr in attributes:
            brand1_value = brand1_data[attr]
            brand2_value = brand2_data[attr]
            difference = brand1_value - brand2_value
            comparison_report += f"{attr.capitalize()}:\n"
            comparison_report += f"{brand1_name}: {brand1_value}\t"
            comparison_report += f"{brand2_name}: {brand2_value}\t"
            comparison_report += f"Difference: {difference:.2f}\n\n"
            
            # Determine the superior brand based on overall_rating
            if attr == 'overall_rating':
                if brand1_value > brand2_value:
                    superior_brand = brand1_name
                elif brand2_value > brand1_value:
                    superior_brand = brand2_name

        # Append the superior brand's name if one is found
        if superior_brand:
            comparison_report += f"The brand with a superior overall rating is: {superior_brand}\n\n"

        # Append the descriptions for each brand
        comparison_report += f"{brand1_name} Description:\n{brand1_data['description']}\n\n"
        comparison_report += f"{brand2_name} Description:\n{brand2_data['description']}\n\n"

        # Display the comparison report
        self.result_text.config(state='normal')
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, comparison_report)
        self.result_text.config(state='disabled')


# Create the application window
root = tk.Tk()
app = BrandComparisonApp(root)

# Start the application
root.mainloop()
