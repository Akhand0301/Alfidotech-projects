"""
Task:- 
Create a Web Scraper 

Objective:- 
Develop a web scraper that collects data from a website and stores 
it in a structured format..

Features:- 
User input to specify the URL and type of data to scrape 
(e.g., headlines, product details, or job listings).
Parse HTML content to extract the required information.
Handle pagination and scrape multiple pages if necessary.
Save the data to a CSV file or a database.

Technologies:-
Python, BeautifulSoup and requests libraries for web scraping, 
and optionally pandas or sqlite3 for data handling.

"""
#_______________My_code_________________________________

import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Function to scrape data from a single page
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: scraping article headlines (modify according to your target website)
    headlines = []
    for article in soup.find_all('h2'):  # Example tag 'h2' for headlines
        headline = article.get_text().strip()
        headlines.append(headline)
    
    return headlines

# Function to handle pagination
def scrape_all_pages(base_url, pages=1):
    all_data = []
    
    for page in range(1, pages + 1):
        # Construct the URL for the page (modify this part based on the website)
        url = f"{base_url}?page={page}"  # Example pagination structure
        data = scrape_page(url)
        all_data.extend(data)
    
    return all_data

# Function to save data to CSV
def save_to_csv(data, filename="scraped_data.csv"):
    df = pd.DataFrame(data, columns=["Headline"])
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
    return filename

# Function to start scraping from GUI
def start_scraping():
    url = url_entry.get()
    pages = pages_entry.get()

    # Input validation
    if not url or not pages:
        messagebox.showerror("Input Error", "Please fill in both fields.")
        return

    try:
        pages = int(pages)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for pages.")
        return

    # Start scraping process
    try:
        all_data = scrape_all_pages(url, pages)
        if all_data:
            filename = save_to_csv(all_data)
            messagebox.showinfo("Success", f"Data scraped and saved to {filename}")
        else:
            messagebox.showwarning("No Data", "No data found on the given pages.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI Setup
root = tk.Tk()
root.title("Web Scraper")

# URL Input
url_label = tk.Label(root, text="Enter Website URL:")
url_label.pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Pages Input
pages_label = tk.Label(root, text="Enter Number of Pages:")
pages_label.pack(pady=5)
pages_entry = tk.Entry(root, width=50)
pages_entry.pack(pady=5)

# Scraping Button
scrape_button = tk.Button(root, text="Start Scraping", command=start_scraping)
scrape_button.pack(pady=20)

# Run the GUI
root.mainloop()