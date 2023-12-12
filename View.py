import tkinter as tk
from pandastable import Table
class View:
    def __init__(self, root):
        self.root = root
        self.controller = None

        root.geometry("500x500")
        root.title("Fast People Search Scraper")

        self.setMainMenu()

    def setMainMenu(self):
        self.label = tk.Label(self.root, text="FUCK FUCK FUCK", font=('Arial', 18))
        self.label.pack()

        self.textbox = tk.Text(self.root, height=2, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Import File & Start", font=('Arial', 16), command=self.buttonPress)
        self.button.pack(padx=10, pady=10)

    def setController(self, controller):
        self.controller = controller

    def buttonPress(self):
        self.controller.setFilename(self.textbox.get('1.0', tk.END))
        self.controller.runScraper()
        self.controller.loadDataFrame()
        self.textbox.pack_forget()
        self.button.pack_forget()
        self.displayPhones()

    def displayPhones(self):

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.table = Table(self.frame, dataframe=self.controller.getDataFrame())
        self.table.show()


    def openWindow(self):
        self.root.mainloop()



