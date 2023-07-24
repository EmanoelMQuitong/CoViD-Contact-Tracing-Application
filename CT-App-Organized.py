import tkinter as tk
from tkinter import messagebox
class CCT:

    def __init__(self):
        self.root = tk.Tk()

        #Create a main frame
        self.root.geometry("500x500")
        self.root.title("Covid Contact Tracing Application")

        self.Main_frame = tk.Frame(self.root, )

        self.Main_frame.pack(fill="both", expand=1)

        #Create a label as title
        self.label = tk.Label(self.Main_frame, text="Welcome! This is company XYZ contact tracing app. To proceed, please kindly read the information below. Click the check box below and press next.", justify="left",wraplength= "500", font=("Helvetica",8))
        self.label.pack(side='top', fill= "both")

        #Create Second Frame    
        self.sec_frame = tk.Frame(self.Main_frame)
        self.sec_frame.pack(side="top", fill="both",)

        #Create a canvas
        self.my_canvas = tk.Canvas(self.Main_frame)
        self.my_canvas.pack(side='left',fill="both", expand=1)

        #Create a Scroll bar
        self.scroll = tk.Scrollbar(self.Main_frame, orient="vertical", command=self.my_canvas.yview)
        self.scroll.pack(side="right", fill="y")

        #Configure the canvas
        self.my_canvas.configure(yscrollcommand=self.scroll)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        #Create a second frame
        self.welc_msg_frame = tk.Frame(self.my_canvas) 
        self.welc_msg_frame.pack( padx=10,pady=10)

        #Add the new frame  to a window in the canvas
        self.my_canvas.create_window((0,0), window=self.welc_msg_frame, anchor="nw")

        #Insert text on a second frame
        self.cf = 'ConsentForm.txt'
        self.welc_msg = tk.Label(self.welc_msg_frame, relief='sunken',borderwidth=3, justify="left",wraplength= "450", text= self.read_file('ConsentForm.txt'), bg='white',font=("Times New Roman",8))
        self.welc_msg.pack(padx=10)

        #Create IntVar function
        self.check_agree = tk.IntVar()

        #Create Agreement checkbox button
        self.agree=tk.Checkbutton(self.root, text=" I have read and understood the information above. I hereby agree and give consent to use my personal information by the stated purposes only. ", justify="left",wraplength= "400", font=("Arial", 8, "underline"), variable=self.check_agree)
        self.agree.pack(side='left',padx=10, pady=10, expand=1, fill="both")

        #Add next button
        self.nextbutton = tk.Button(self.root, text="Next >",font=("Arial",12), command=self.move_to_next1)
        self.nextbutton.pack(side='top', padx=10, pady=10,fill="both")

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title="Are you sure?", message="Do you really want to quit?"):
            self.root.destroy()

    def read_file(self, cf):
        try:
            with open(cf, 'r') as file:
                content = file.read()
                return content
        
        except FileNotFoundError:
            print(f'File not found: {cf}')
        except IOError:
            print(f'Error reading file: {cf}')

    def move_to_next1(self):
        if self.check_agree.get()==0:
            messagebox.showinfo(title="To Proceed", message="Please click the check box before you proceed.")
        else:
            self.PI = tk.Toplevel(self.root)
            self.PI.geometry("500x500")
            self.PI.title("Personal Information")


            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.PI.mainloop()






cct_app = CCT()

