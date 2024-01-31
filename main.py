import tkinter as tk
from tkinter import ttk
import requests

class NewsApp:
    def __init__(self, root):
        self.root = root
        root.title("News API App")

        self.search_label = ttk.Label(root, text="Enter your interest:", font=("Arial", 14))
        self.search_label.pack(pady=10)

        self.search_entry = ttk.Entry(root, font=("Arial", 14), width=50)
        self.search_entry.pack(pady=10)

        self.search_button = ttk.Button(root, text="Search News", command=self.load_news)
        self.search_button.pack(pady=10)

        self.news_label = ttk.Label(root, text="Top Headlines", font=("Arial", 20))
        self.news_label.pack(pady=10)

        self.listbox = tk.Listbox(root, width=100, height=20)
        self.listbox.pack(pady=20)

        self.api_key = "835dd37ded0e4cbdaf600af4d6664d3b"  # Replace with your News API key

    def fetch_news(self, query):
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={self.api_key}"
        response = requests.get(url)
        news = response.json()
        return news['articles']

    def load_news(self):
        self.listbox.delete(0, tk.END)
        query = self.search_entry.get()
        if not query:
            self.listbox.insert(tk.END, "Please enter a topic of interest.")
            return
        try:
            articles = self.fetch_news(query)
            for article in articles:
                self.listbox.insert(tk.END, article['title'])
        except Exception as e:
            self.listbox.insert(tk.END, f"Error: {e}")

def main():
    root = tk.Tk()
    app = NewsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
