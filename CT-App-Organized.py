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
        if self.Name.get()=='' or self.Age.get()=='' or self.Status.get()=='' or self.Address.get()=='' or self.Room.get()=='':
            messagebox.showinfo(title="INVALID!", message="Please fill all the entry boxes.")
        else:
            #Hide the 2nd window
            self.PI.withdraw()  
            
            #Create 3rd window
                    
            self.HI = tk.Tk()
            
            
            self.HI.geometry("1000x500")
            self.HI.title("Covid Contact Tracing Application")
            self.HI.resizable(False,False)

            #Create a main frame
            self.Main_frame = tk.Frame(self.HI, bg='lemon chiffon', relief = "sunken", bd=5 )
            self.Main_frame.pack(fill="both", expand=1)

            #Create Frames
            self.blank = tk.Frame(self.Main_frame,bg='white', width=100, height=50  )
            self.blank.pack(fill="both", expand=1)

            #Text frame 1
            self.textframe = tk.Frame(self.blank, relief='groove',bd=3, width=495, height=500 )
            self.textframe.place(x=0,y=0)
            
            #Text Frame 2
            self.textframe1 = tk.Frame(self.blank, relief='groove', bd=3, width=500, height=450  )
            self.textframe1.place(x=492,y=0)

            #Text Frame 1 Title
            self.TextTitle = tk.Frame(self.textframe, relief='raise', bd=3,width=450, height=50).place(x=20,y=10)

            #Set Variables
            V1 = tk.StringVar()
            V1.set('Not yet')
            S1 = tk.StringVar()
            S1.set('Yes')
            E1 = tk.StringVar()
            E1.set('Yes')
            CC1 = tk.StringVar()
            CC1.set('Yes')
            CT1 = tk.StringVar()
            CT1.set('No')

            #Title 
            HDF = tk.Label(self.textframe, text="HEALTH DECLARATION:",  font=("arial bold ",16)).place(x=140,y=20)

            #Questions and Radiiobuttons
            Vaccination = tk.Label(self.textframe, text="1.	Have you been vaccinated for COVID-19? ",  font=("arial ",10)).place(x=20,y=75)
            r1 = tk.Label(self.textframe, text="*Required",  fg='red',font=("arial ",8)).place(x=400,y=75)
            
            V1_1 = tk.Radiobutton(self.textframe, text='Not yet', variable=V1, value='Not yet').place(x=50,y=100)
            V1_2 = tk.Radiobutton(self.textframe, text='1st Dose', variable=V1, value='1st Dose').place(x=50,y=125)
            V1_3 = tk.Radiobutton(self.textframe, text='2nd Dose', variable=V1, value='2nd Dose(Complete Vaccination)').place(x=200,y=100)
            V1_4 = tk.Radiobutton(self.textframe, text='1st Booster Shot', variable=V1, value='1st Booster Shot').place(x=200,y=125)
            V1_5 = tk.Radiobutton(self.textframe, text='2nd Booster Shot', variable=V1, value='2nd Booster Shot').place(x=300,y=100)


            Symptoms = tk.Label(self.textframe, text="2.	Are you experiencing any symptoms in the past 7 days such as body pains, headache, sore throat, fever, diarrhea, cough, colds, shortness of breath, loss of taste, or loss of smell?",justify="left", wraplength=450, font=("arial ",8)).place(x=20,y=150)
            
            S1_1 = tk.Radiobutton(self.textframe, text='Yes', variable=S1, value='Yes').place(x=50,y=200)
            S1_2 = tk.Radiobutton(self.textframe, text='No', variable=S1, value='No').place(x=200,y=200)
            

            Exposure = tk.Label(self.textframe, text="3.	Have you had exposure to a probable or confirmed case in the last 14 days?",  justify='left',wraplength=450,font=("arial ",10)).place(x=20,y=250)
            
            E1_1 = tk.Radiobutton(self.textframe, text='Yes', variable=E1, value='Yes').place(x=50,y=290)
            E1_2 = tk.Radiobutton(self.textframe, text='No', variable=E1, value='No').place(x=200,y=290)
            E1_3 = tk.Radiobutton(self.textframe, text='Uncertain', variable=E1, value='Uncertain').place(x=350,y=290)

            CovidContact = tk.Label(self.textframe, text="4.	Have you had contact with somebody with body pains, headache, sore throat, fever, diarrhea, cough, colds, shortness of breath, loss of taste, or loss of smell in the past 7 days?", justify='left',wraplength=450,font=("arial ",8)).place(x=20,y=325)

            CC1_1 = tk.Radiobutton(self.textframe, text='Yes', variable=CC1, value='Yes').place(x=50,y=370)
            CC1_2 = tk.Radiobutton(self.textframe, text='No', variable=CC1, value='No').place(x=200,y=370)
            CC1_3 = tk.Radiobutton(self.textframe, text='Uncertain', variable=CC1, value='Uncertain').place(x=350,y=370)

            CovidTest = tk.Label(self.textframe, text="5.	Have you been tested for COVID-19 in the last 14 days?",  font=("arial ",10)).place(x=20,y=400)

            CT1_1 = tk.Radiobutton(self.textframe, text='No', variable=CT1, value='No').place(x=50,y=425)
            CT1_2 = tk.Radiobutton(self.textframe, text='Yes-Positive', variable=CT1, value='Yes-Positive').place(x=200,y=425)
            CT1_3 = tk.Radiobutton(self.textframe, text='Yes-Negative', variable=CT1, value='Yes-Negative').place(x=50,y=450)
            CT1_4 = tk.Radiobutton(self.textframe, text='Yes-Pending', variable=CT1, value='Yes-Pending').place(x=200,y=450)   




            #Contact Person Details

            #Contact Person Title Frame
            self.TextTitle1 = tk.Frame(self.textframe1, relief='raise', bd=3,width=450, height=50).place(x=20,y=10)

            #Contact Person Title
            PCD = tk.Label(self.textframe1, text="CONTACT PERSON DETAILS:", font=("arial bold ", 16)).place(x=100, y=20)
        
        
            #Contact Person Variables
            self.CP_Name = tk.StringVar()
            self.CP_Relationship= tk.StringVar()
            self.CP_CN = tk.StringVar()
            self.CP_EA = tk.StringVar()

            #Contact Person Entries
            Name=tk.Entry(self.textframe1, textvariable=self.CP_Name, width=40, bd=2, font=("arial", 12)).place(x=90, y=75)
            Relationship=tk.Entry(self.textframe1, textvariable=self.CP_Relationship, width=40, bd=2, font=("arial", 12)).place(x=90, y=175)
            CN=tk.Entry(self.textframe1, textvariable=self.CP_CN, width=40, bd=2, font=("arial", 12)).place(x=90, y=270)
            EA=tk.Entry(self.textframe1, textvariable=self.CP_EA, width=40, bd=2, font=("arial", 12)).place(x=90, y=370)


            #Contact Person Labels
            NAME = tk.Label(self.textframe1, text="Name: ",  font=("arial ",12)).place(x=20,y=75)
            e1 = tk.Label(self.textframe1, text="*Example: Juan Dela Cruz", font=("arial ",8)).place(x=90,y=100)
            r1 = tk.Label(self.textframe1, text="*Required",  fg='red',font=("arial ",8)).place(x=400,y=100)

            RELATION = tk.Label(self.textframe1, text="Relation: ",  font=("arial ",12)).place(x=20,y=175)
            e2 = tk.Label(self.textframe1, text="*Family/Father/Mother/Brother/Sister",  font=("arial ",8)).place(x=90,y=200)
            r2 = tk.Label(self.textframe1, text="*Required",  fg='red',font=("arial ",8)).place(x=400,y=200)

            CONTACT_NUMBER = tk.Label(self.textframe1,justify='left',wraplength=100, text="Contact Number: ",  font=("arial ",12)).place(x=20,y=250)
            e2 = tk.Label(self.textframe1, text="*63+ 9** *** **** ",  font=("arial ",8)).place(x=90,y=300)
            r2 = tk.Label(self.textframe1, text="*Required",  fg='red',font=("arial ",8)).place(x=400,y=300)
                
            EMAIL_ADDRESS = tk.Label(self.textframe1,justify='left',wraplength=100, text="Email Address: ",  font=("arial ",12)).place(x=20,y=350)
            e2 = tk.Label(self.textframe1, text="*JuanDelaCruz@hotmail.com ",  font=("arial ",8)).place(x=90,y=400)
            r2 = tk.Label(self.textframe1, text="*Required",  fg='red',font=("arial ",8)).place(x=400,y=400)


            #Button Frame 1
            self.buttonframe = tk.Frame(self.blank,relief='groove', bd=3, width=500, height=50  )
            self.buttonframe.place(x=492,y=450)

            #Page 3 Back Button
            pg3_back = tk.Button(self.buttonframe, text="< Back",font=("arial underline",12),command=self.back_to_page2)
            pg3_back.place(x=5,y=5)

            #Page 3 Next Button
            pg3_next = tk.Button(self.buttonframe, text="Next >",font=("arial underline",12),command=self.next_to_page4)
            pg3_next.place(x=430,y=5)


            
            

            
            self.HI.mainloop()

    def back_to_page2(self):
            print("HI")

    def next_to_page4(self):
            print("Hellow")





cct_app = CCT()

