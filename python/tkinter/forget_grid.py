"""https://www.youtube.com/watch?v=XuNKxXS3Sdc&list=
PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=38
"""
import tkinter as tk


def click_button():
    global lbl

    lbl.destroy()

    hello = "Hello " + e.get()
    lbl = tk.Label(root, text=hello)
    lbl.grid(row=3, column=0, pady=10)
    e.delete(0, "end")

    # btn_create_lbl["state"] = "disabled"


# def delete_button():
#     global lbl

#     # pack_forget just takes it off screen
#     # grid_forget does the same for grid objects
#     # use destroy to permanently destroy the widget
#     lbl.grid_forget()

#     btn_create_lbl["state"] = "normal"


root = tk.Tk()
root.title("Entry Height Exercise")
root.geometry("600x600")

e = tk.Entry(root, width=17, font=("Helvetica 32 bold"))
e.grid(row=0, column=0, padx=10, pady=10)

lbl = tk.Label(root)

btn_create_lbl = tk.Button(root, text="Enter Your Name", command=click_button)
btn_create_lbl.grid(row=1, column=0, pady=10)

# btn_delete_lbl = tk.Button(root, text="Delete Text", command=delete_button)
# btn_delete_lbl.grid(row=2, column=0, pady=10)

root.mainloop()