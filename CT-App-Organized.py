import tkinter as tk
from tkinter import messagebox

class CCT:

    def __init__(self):


        self.welcome = tk.Tk()
        
        #Create a main frame
        self.welcome.geometry("500x500")
        self.welcome.title("Covid Contact Tracing Application")
        self.welcome.resizable(False,False)


        self.Main_frame = tk.Frame(self.welcome)

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
        self.agree=tk.Checkbutton(self.welcome, text=" I have read and understood the information above. I hereby agree and give consent to use my personal information by the stated purposes only. ", justify="left",wraplength= "400", font=("Arial", 8, "underline"), variable=self.check_agree)
        self.agree.pack(side='left',padx=10, pady=10, expand=1, fill="both")

        #Add next button
        self.nextbutton = tk.Button(self.welcome, text="Next >",font=("Arial",12), command=self.move_to_next1)
        self.nextbutton.pack(side='top', padx=10, pady=10,fill="both")

        self.welcome.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.welcome.mainloop()

    #a function that asks the user when close window is clicked
    def on_closing(self):
        if messagebox.askyesno(title="Are you sure?", message="Do you really want to quit?"):
            self.welcome.destroy()

    #open a file then read all of its contents
    def read_file(self, cf):
        try:
            with open(cf, 'r') as file:
                content = file.read()
                return content
        
        except FileNotFoundError:
            print(f'File not found: {cf}')
        except IOError:
            print(f'Error reading file: {cf}')


    
        

    #Command to move to next window when "next >" is clicked
    def move_to_next1(self):
        if self.check_agree.get()==0:
            messagebox.showinfo(title="To Proceed", message="Please click the check box before you proceed.")
        else:
            #Hide the welcome window
            self.welcome.withdraw()
            
            #Create new window
            self.PI = tk.Toplevel(self.welcome, bg='lemon chiffon', relief = "sunken", bd=5)
            self.PI.geometry("500x500")
            self.PI.title("Covid Contact Tracing Application")
            self.PI.resizable(False,False)

            #Create a main frame
            self.Main_frame = tk.Frame(self.PI, )
            self.Main_frame.pack(fill="both", expand=1)

            #Create Franes
            self.blank = tk.Frame(self.Main_frame,bg='white', width=100, height=50  )
            self.blank.pack(fill="both", expand=1)

            self.textframe = tk.Frame(self.blank )
            self.textframe.pack(side='top', fill="both", expand=1)
            
            #Create a label as title
            Headline = tk.Label(self.textframe, text="Personal Information",  font=("arial bold",30))
            Headline.place(x=50,y=1)

            #String Variables
            self.Name=tk.StringVar()
            self.Age=tk.StringVar()
            self.Status=tk.StringVar()
            self.Address=tk.StringVar()
            self.Room=tk.StringVar()

            #Labels
            NAME = tk.Label(self.textframe, text="Name: ",  font=("arial ",12)).place(x=20,y=75)
            e1 = tk.Label(self.textframe, text="*Example: Juan Dela Cruz", font=("arial ",8)).place(x=90,y=100)
            r1 = tk.Label(self.textframe, text="*Required",  fg='red',font=("arial ",8)).place(x=400,y=100)

            AGE = tk.Label(self.textframe, text="Age: ",  font=("arial ",12)).place(x=20,y=150)
            e2 = tk.Label(self.textframe, text="*Please state your age. ",  font=("arial ",8)).place(x=90,y=175)
            r2 = tk.Label(self.textframe, text="*Required",  fg='red',font=("arial ",8)).place(x=400,y=175)

            STATUS = tk.Label(self.textframe, text="Status: ",  font=("arial ",12)).place(x=20,y=225)
            e2 = tk.Label(self.textframe, text="*Are you SINGLE, or MARRIED? ",  font=("arial ",8)).place(x=90,y=250)
            r2 = tk.Label(self.textframe, text="*Required",  fg='red',font=("arial ",8)).place(x=400,y=250)
            
            ADDRESS = tk.Label(self.textframe, text="Address: ",  font=("arial ",12)).place(x=20,y=300)
            e2 = tk.Label(self.textframe, text="*House No./Block/Sitio/Village/Barangay/Province or City. ",  font=("arial ",8)).place(x=90,y=325)
            r2 = tk.Label(self.textframe, text="*Required",  fg='red',font=("arial ",8)).place(x=400,y=325)

            ROOM = tk.Label(self.textframe, text="Room: ",  font=("arial ",12)).place(x=20,y=375)
            e2 = tk.Label(self.textframe, text="*Which room in the establishment you are heading?",  font=("arial ",8)).place(x=90,y=400)
            r2 = tk.Label(self.textframe, text="*Required",  fg='red',font=("arial ",8)).place(x=400,y=400)

            #Entries   
            entry_Name=tk.Entry(self.textframe, textvariable=self.Name, width=40, bd=2, font=("arial", 12)).place(x=90, y=75)
            entry_Age=tk.Entry(self.textframe, textvariable=self.Age, width=40, bd=2, font=("arial", 12)).place(x=90, y=150)
            entry_Status=tk.Entry(self.textframe, textvariable=self.Status, width=40, bd=2, font=("arial", 12)).place(x=90, y=225)
            entry_Address=tk.Entry(self.textframe, textvariable=self.Address, width=40, bd=2, font=("arial", 12)).place(x=90, y=300)
            entry_Room=tk.Entry(self.textframe, textvariable=self.Room, width=40, bd=2, font=("arial", 12)).place(x=90, y=375)
            
            
            #Next Button
            nextbutton = tk.Button(self.textframe, text="Next >",font=("Arial",12),command =self.move_to_next2)
            nextbutton.place(x=430,y=450)

            self.PI.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.PI.mainloop()

    def move_to_next2(self):
            print(self.Name.get())
            print(self.Age.get())
            print(self.Status.get())
            print(self.Address.get())
            print(self.Room.get())  
            





cct_app = CCT()

