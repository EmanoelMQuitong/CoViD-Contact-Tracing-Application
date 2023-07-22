import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Welcome")

label = tk.Label(root, text="Hello World", font=("Times New Roman",20))
label.pack(padx=30, pady=40)

textbox = tk.Text(root, height=3, font=("Times New Roman",20))
textbox.pack(padx=10,pady=10)

nextbutton = tk.Button(root, text="Next >",font=("Arial",12))
nextbutton.pack(padx=10, pady=30)

root.mainloop()