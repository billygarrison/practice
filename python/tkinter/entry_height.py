"""https://www.youtube.com/watch?v=XuNKxXS3Sdc&list=
PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=38
"""
import tkinter as tk


def click_button():
    hello = "Hello " + e.get()
    lbl = tk.Label(root, text=hello)
    lbl.pack(pady=10)
    e.delete(0, "end")


root = tk.Tk()
root.title("Entry Height Exercise")
root.geometry("600x600")

e = tk.Entry(root, width=50, font=("Helvetica 32 bold"))
e.pack(padx=10, pady=10)

btn = tk.Button(root, text="Enter Your Name", command=click_button)
btn.pack(pady=10)

root.mainloop()