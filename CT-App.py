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

root.geometry("500x500")
root.title("Covid Contact Tracing Application")

label = tk.Label(root, text="Welcome!", font=("Times New Roman",20))
label.pack(padx=10,pady=10)

welc_msg_frame = tk.Frame(width="200",height="300",bg="white") 
welc_msg_frame.pack(padx=10,pady=10)

cf = 'ConsentForm.txt'
welc_msg = tk.Label(welc_msg_frame, justify="left",wraplength= "400", text= read_file(cf), bg='white',font=("Times New Roman",12))

welc_msg.pack(padx=10,pady=20)



nextbutton = tk.Button(root, text="Next >",font=("Arial",12))
nextbutton.pack(side="bottom",padx=10, pady=10)

root.mainloop()

print(read_cf)