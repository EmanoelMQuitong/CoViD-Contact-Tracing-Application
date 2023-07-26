import tkinter as tk

class CCT:

    def __init__(self):


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
        HDF = tk.Label(self.TextTitle, text="HEALTH DECLARATION:",  font=("arial bold ",16)).place(x=140,y=30)

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

    def setvariables(self):
        pass
cct_app = CCT()

