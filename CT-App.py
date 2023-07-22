import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Covid Contact Tracing Application")

label = tk.Label(root, text="Welcome!", font=("Times New Roman",20))
label.pack(padx=10,pady=10)

welc_msg_frame = tk.Frame(width="200",height="300",bg="white") 
welc_msg_frame.pack(padx=10,pady=10)

welc_msg = tk.Label(welc_msg_frame, text="This program aims to trace possible personnels who enters xyz establishment.", bg='white',font=("Times New Roman",12))

welc_msg.pack(padx=10,pady=20)



nextbutton = tk.Button(root, text="Next >",font=("Arial",12))
nextbutton.pack(side="bottom",padx=10, pady=10)

root.mainloop()