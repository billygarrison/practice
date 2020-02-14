from tkinter import *
from PIL import ImageTk, Image  # Non-standard library `Pillow`

import numpy as np
import matplotlib.pyplot as plt


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)  # 50 bins
    plt.show()


# Create root with title and favicon
root = Tk()
root.title("Plots Exercise")
root.iconbitmap("images/favicon.ico")
root.geometry("400x200")

# Button to plot house prices
btn = Button(root, text="Graph It!", command=graph)
btn.pack()

# Main loop
root.mainloop()