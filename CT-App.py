import tkinter as tk

def read_file(cf):
    try:
        with open(cf, 'r') as file:
            content = file.read()
            return content
    
    except FileNotFoundError:
        print(f'File not found: {cf}')
    except IOError:
        print(f'Error reading file: {cf}')




root = tk.Tk()

#Create a main frame
root.geometry("500x500")
root.title("Covid Contact Tracing Application")

Main_frame = tk.Frame(root)
Main_frame.pack(fill="both", expand=1)

#Create a label as title
label = tk.Label(Main_frame, text="Welcome!", font=("Times New Roman",20))
label.pack(side='top', padx=10,pady=10)

#Create Second Frame
sec_frame = tk.Frame(Main_frame)
sec_frame.pack(side="top", fill="both",)

#Create a canvas
my_canvas = tk.Canvas(Main_frame)
my_canvas.pack(side='left',fill="both", expand=1)

#Create a Scroll bar
scroll = tk.Scrollbar(Main_frame, orient="vertical", command=my_canvas.yview)
scroll.pack(side="right", fill="y")

#Configure the canvas
my_canvas.configure(yscrollcommand=scroll)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

#Create a second frame
welc_msg_frame = tk.Frame(my_canvas) 
welc_msg_frame.pack( padx=10,pady=10)

#Add the new frame  to a window in the canvas
my_canvas.create_window((0,0), window=welc_msg_frame, anchor="nw")

#Insert text on a second frame
cf = 'ConsentForm.txt'
welc_msg = tk.Label(welc_msg_frame, justify="left",wraplength= "450", text= read_file(cf), bg='white',font=("Times New Roman",8))
welc_msg.pack(padx=10,pady=20)

#Add next button
nextbutton = tk.Button(root, text="Next >",font=("Arial",12))
nextbutton.pack(side='right', padx=10, pady=10)

root.mainloop()

