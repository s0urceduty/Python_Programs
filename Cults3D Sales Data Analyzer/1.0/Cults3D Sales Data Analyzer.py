# Cults3D Sales Data Analyzer
# Open Cults3D CSV sale data files, view the processed data, and export a detailed statistical report.
# 🛈 This software is free and open-source; anyone can redistribute it and/or modify it.


import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

def load_and_clean_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Remove rows where all elements are NaN
    data_cleaned = data.dropna(how='all')

    # Fill missing values with 0 for numerical columns and empty string for others
    data_cleaned = data_cleaned.fillna({
        'Date': '',
        'User': '',
        'Buyer country': '',
        'Design': '',
        'Total before tax (EUR)': 0,
        'VAT (%)': '0%',
        'VAT base (% of Total before tax)': '0%',
        'VAT EUR': 0,
        'Total including VAT EUR': 0,
        'Cults Commission EUR': 0,
        'Income EUR': 0,
        'Total in currency': 0,
        'Currency': '',
        'Status': ''
    })

    # Convert columns to appropriate data types
    data_cleaned['Date'] = pd.to_datetime(data_cleaned['Date'], errors='coerce')
    data_cleaned['Total before tax (EUR)'] = pd.to_numeric(data_cleaned['Total before tax (EUR)'])
    data_cleaned['VAT EUR'] = pd.to_numeric(data_cleaned['VAT EUR'])
    data_cleaned['Total including VAT EUR'] = pd.to_numeric(data_cleaned['Total including VAT EUR'])
    data_cleaned['Cults Commission EUR'] = pd.to_numeric(data_cleaned['Cults Commission EUR'])
    data_cleaned['Income EUR'] = pd.to_numeric(data_cleaned['Income EUR'])
    data_cleaned['Total in currency'] = pd.to_numeric(data_cleaned['Total in currency'])

    return data_cleaned

def analyze_data(data):
    # Summary statistics
    summary_stats = data.describe()

    # Sort data by Date and Total including VAT EUR
    data_sorted = data.sort_values(by=['Date', 'Total including VAT EUR'], ascending=[True, False])

    # Group by User and Buyer country
    grouped_by_user = data.groupby('User').agg({
        'Total before tax (EUR)': 'sum',
        'Total including VAT EUR': 'sum',
        'Cults Commission EUR': 'sum',
        'Income EUR': 'sum'
    })

    grouped_by_country = data.groupby('Buyer country').agg({
        'Total before tax (EUR)': 'sum',
        'Total including VAT EUR': 'sum',
        'Cults Commission EUR': 'sum',
        'Income EUR': 'sum'
    })

    return summary_stats, data_sorted, grouped_by_user, grouped_by_country

def generate_report(summary_stats, data_sorted, grouped_by_user, grouped_by_country):
    # Create the statistics report
    report = f"""
Sales Data Statistics Report

Summary Statistics:
-------------------
Total before tax (EUR):
- Count: {summary_stats.loc['count', 'Total before tax (EUR)']}
- Mean: {summary_stats.loc['mean', 'Total before tax (EUR)']}
- Min: {summary_stats.loc['min', 'Total before tax (EUR)']}
- Max: {summary_stats.loc['max', 'Total before tax (EUR)']}

VAT EUR:
- Count: {summary_stats.loc['count', 'VAT EUR']}
- Mean: {summary_stats.loc['mean', 'VAT EUR']}
- Min: {summary_stats.loc['min', 'VAT EUR']}
- Max: {summary_stats.loc['max', 'VAT EUR']}

Total including VAT EUR:
- Count: {summary_stats.loc['count', 'Total including VAT EUR']}
- Mean: {summary_stats.loc['mean', 'Total including VAT EUR']}
- Min: {summary_stats.loc['min', 'Total including VAT EUR']}
- Max: {summary_stats.loc['max', 'Total including VAT EUR']}

Cults Commission EUR:
- Count: {summary_stats.loc['count', 'Cults Commission EUR']}
- Mean: {summary_stats.loc['mean', 'Cults Commission EUR']}
- Min: {summary_stats.loc['min', 'Cults Commission EUR']}
- Max: {summary_stats.loc['max', 'Cults Commission EUR']}

Income EUR:
- Count: {summary_stats.loc['count', 'Income EUR']}
- Mean: {summary_stats.loc['mean', 'Income EUR']}
- Min: {summary_stats.loc['min', 'Income EUR']}
- Max: {summary_stats.loc['max', 'Income EUR']}

Top Transaction:
----------------
- Date: {data_sorted.iloc[0]['Date']}
- User: {data_sorted.iloc[0]['User']}
- Buyer country: {data_sorted.iloc[0]['Buyer country']}
- Design: {data_sorted.iloc[0]['Design']}
- Total before tax (EUR): {data_sorted.iloc[0]['Total before tax (EUR)']}
- Total including VAT EUR: {data_sorted.iloc[0]['Total including VAT EUR']}
- Cults Commission EUR: {data_sorted.iloc[0]['Cults Commission EUR']}
- Income EUR: {data_sorted.iloc[0]['Income EUR']}

Grouped by User:
----------------
{grouped_by_user.to_string()}

Grouped by Buyer country:
-------------------------
{grouped_by_country.to_string()}
    """
    return report

def save_report(report, output_path):
    # Save the report to a text file
    with open(output_path, 'w') as file:
        file.write(report)

class SalesDataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sales Data Analyzer")
        self.data = None
        self.create_widgets()

    def create_widgets(self):
        self.open_button = tk.Button(self.root, text="Open CSV", command=self.open_file)
        self.open_button.pack(pady=10)

        self.text_area = ScrolledText(self.root, wrap=tk.WORD, width=100, height=30)
        self.text_area.pack(pady=10)

        self.export_button = tk.Button(self.root, text="Export Report", command=self.export_report)
        self.export_button.pack(pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.data = load_and_clean_data(file_path)
            self.show_data()

    def show_data(self):
        if self.data is not None:
            self.text_area.delete(1.0, tk.END)
            summary_stats, data_sorted, grouped_by_user, grouped_by_country = analyze_data(self.data)
            report = generate_report(summary_stats, data_sorted, grouped_by_user, grouped_by_country)
            self.text_area.insert(tk.END, report)

    def export_report(self):
        if self.data is not None:
            output_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if output_path:
                summary_stats, data_sorted, grouped_by_user, grouped_by_country = analyze_data(self.data)
                report = generate_report(summary_stats, data_sorted, grouped_by_user, grouped_by_country)
                save_report(report, output_path)
                messagebox.showinfo("Export Report", f"Report successfully exported to {output_path}")
        else:
            messagebox.showwarning("Export Report", "No data to export")

def main():
    root = tk.Tk()
    app = SalesDataApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
