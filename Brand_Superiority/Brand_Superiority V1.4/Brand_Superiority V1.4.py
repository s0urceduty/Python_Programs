# Brand_Superiority V1.4

# 📈 Rating and comparing global business brand attributes for superiority.

# ChatGPT provided generalized brand attribute rating based on global presence, market reputation, and known innovation practices up to it's last update in April 2023.

# Copyright (C) 2023, Sourceduty - All Rights Reserved.
# THE CONTENTS OF THIS PROJECT ARE PROPRIETARY.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Brand names data
brand_attributes = {
    "Apple": {"Description": "Highly regarded for its innovative technology, unique design aesthetics, and user-friendly ecosystem, which foster trust and relevance. Its product convenience is enhanced by seamless integration across its devices and services.",
     "Ratings": {
        "Trust": 8,
        "Quality": 7,
        "Reliability": 7,
        "Customer Service": 7,
        "Innovation": 8,
        "Authenticity": 7,
        "Value for Money": 7,
        "Ethical Practices": 7,
        "Brand Image": 7,
        "Consistency": 7
     }
    },
    "Amazon": {"Description": "A paradigm of convenience with its vast product range and swift delivery. Amazon's constant innovation, particularly in cloud computing and logistics, underpins its relevance and builds consumer trust.",
     "Ratings": {
        "Trust": 8.5,
        "Quality": 8,
        "Reliability": 8,
        "Customer Service": 8,
        "Innovation": 9,
        "Authenticity": 8,
        "Value for Money": 8.5,
        "Ethical Practices": 8,
        "Brand Image": 8.5,
        "Consistency": 8
     }
    },
    "Google": {"Description": "A leader in innovation with its search engine and Android OS, offering unique and convenient services. Its relevance is unquestionable, though trust varies due to concerns over data privacy.",
     "Ratings": {
        "Trust": 7.5,
        "Quality": 8,
        "Reliability": 8.5,
        "Customer Service": 7,
        "Innovation": 9,
        "Authenticity": 7.5,
        "Value for Money": 7,
        "Ethical Practices": 7,
        "Brand Image": 8,
        "Consistency": 8
     }
    },
    "Microsoft": {"Description": "Known for trustworthy software and services, with a constant drive for innovation in cloud computing and gaming, ensuring its relevance. Its product suite offers convenience through cross-platform integration.",
     "Ratings": {
        "Trust": 8,
        "Quality": 8,
        "Reliability": 8,
        "Customer Service": 7.5,
        "Innovation": 8.5,
        "Authenticity": 7.5,
        "Value for Money": 7.5,
        "Ethical Practices": 7.5,
        "Brand Image": 8,
        "Consistency": 8
     }
    },
    "Samsung": {"Description": "Trusted for its reliable electronics, Samsung's innovation in mobile technology and semiconductors keeps it relevant and convenient, offering a unique portfolio from phones to home appliances.",
     "Ratings": {
        "Trust": 7.5,
        "Quality": 8,
        "Reliability": 8.5,
        "Customer Service": 7,
        "Innovation": 8,
        "Authenticity": 7,
        "Value for Money": 7.5,
        "Ethical Practices": 7,
        "Brand Image": 7.5,
        "Consistency": 8
     }
    }
}


# GUI implementation
class BrandComparisonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Brand Superiority V1.4")
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
        self.result_text = tk.Text(self.root, height=30, width=150, state='disabled')
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

        # Calculate the overall rating for each brand
        brand1_ratings = brand1_data["Ratings"]
        brand2_ratings = brand2_data["Ratings"]
        brand1_overall_rating = sum(brand1_ratings.values()) / len(brand1_ratings)
        brand2_overall_rating = sum(brand2_ratings.values()) / len(brand2_ratings)

        # Prepare the comparison report
        comparison_report = f"Comparing {brand1_name} vs {brand2_name}\n\n"
        attributes = brand1_data["Ratings"].keys()
        
        for attr in attributes:
            brand1_value = brand1_data["Ratings"][attr]
            brand2_value = brand2_data["Ratings"][attr]
            difference = brand1_value - brand2_value
            comparison_report += f"{attr}:\n"
            comparison_report += f"{brand1_name}: {brand1_value}\t"
            comparison_report += f"{brand2_name}: {brand2_value}\t"
            comparison_report += f"Difference: {difference:.2f}\n\n"

        # Append the overall ratings for each brand
        comparison_report += f"{brand1_name} Overall Rating: {brand1_overall_rating:.2f}\n"
        comparison_report += f"{brand2_name} Overall Rating: {brand2_overall_rating:.2f}\n\n"

        # Determine the superior brand based on overall rating
        superior_brand = brand1_name if brand1_overall_rating > brand2_overall_rating else brand2_name
        comparison_report += f"The brand with a superior overall rating is: {superior_brand}\n\n"

        # Append the descriptions for each brand
        comparison_report += f"{brand1_name} Description:\n{brand1_data['Description']}\n\n"
        comparison_report += f"{brand2_name} Description:\n{brand2_data['Description']}\n\n"

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
