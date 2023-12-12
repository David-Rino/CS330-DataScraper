from Controller import Controller
from PandasModel import PandasModel
import DataScraperModel as model
import tkinter as tk
from View import View

#root = tk.Tk()
#app = View(root)
#root.mainloop()

if __name__ == "__main__":
    userData = PandasModel()
    root = tk.Tk()
    userView = View(root)
    userController = Controller(userView, userData)

    userController.runScraper()
    userController.loadDataFrame()
    userController.runWindow()



