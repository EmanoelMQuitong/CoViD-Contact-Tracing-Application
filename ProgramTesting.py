import tkinter as tk

class CCT:

    def __init__(self):


        self.welcome = tk.Tk()
        
        
        self.welcome.geometry("500x500")
        self.welcome.title("Covid Contact Tracing Application")
        self.welcome.resizable(False,False)

        #Create a main frame
        self.Main_frame = tk.Frame(self.welcome, )
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
        nextbutton = tk.Button(self.textframe, text="Next >",font=("Arial",12),command=self.next2)
        nextbutton.place(x=430,y=450)
        #Back Button
        backbutton = tk.Button(self.textframe, text="< Back",font=("Arial",12))
        backbutton.place(x=10,y=450)

        
        self.welcome.mainloop()

    def next2(self):
        print(self.Name.get())
        print(self.Age.get())
        print(self.Status.get())
        print(self.Address.get())
        print(self.Room.get())

cct_app = CCT()

