import tkinter as tk
from tkinter import messagebox
import pyshorteners
import pyperclip

class URLShortenerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kenny URL Shortener")

        self.label = tk.Label(master, text="Enter the URL to shorten:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, width=40)
        self.entry.pack(pady=10)

        self.button = tk.Button(master, text="Shorten URL", command=self.shorten_url)
        self.button.pack(pady=10)

        self.copy_button = tk.Button(master, text="Copy Shortened URL", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=10)

    def shorten_url(self):
        long_url = self.entry.get()

        if not long_url:
            messagebox.showwarning("Warning", "Please enter a valid URL.")
            return

        try:
            # Shorten the URL using TinyURL
            s = pyshorteners.Shortener()
            short_url = s.tinyurl.short(long_url)

            # Display the shortened URL in a messagebox
            messagebox.showinfo("Shortened URL", f"The shortened URL is:\n{short_url}")

            # Store the shortened URL for later copying
            self.short_url = short_url
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def copy_to_clipboard(self):
        try:
            # Copy the shortened URL to the clipboard
            pyperclip.copy(self.short_url)
            messagebox.showinfo("Copy Successful", "Shortened URL copied to clipboard!")
        except AttributeError:
            messagebox.showerror("Error", "Copying to clipboard is not supported on your system.")

if __name__ == "__main__":
    root = tk.Tk()
    app = URLShortenerApp(root)
    root.mainloop()
