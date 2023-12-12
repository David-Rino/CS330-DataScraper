import tkinter as tk
class View:
    def __init__(self, root):
        self.root = root
        root.geometry("500x500")
        root.title("Fast People Search Scraper")
        Label = tk.Label(root, text="FUCK FUCK FUCK FUCK", font=('Arial',18))
        Label.pack()

    def openWindow(self):
        self.root.mainloop()

