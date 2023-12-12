import tkinter as tk
class View:
    def __init__(self, root):
        self.root = root
        root.geometry("500x500")
        root.title("Fast People Search Scraper")


root = tk.Tk()
app = View(root)
root.mainloop()