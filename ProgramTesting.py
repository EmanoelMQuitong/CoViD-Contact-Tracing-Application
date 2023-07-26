import tkinter as tk
from tkinter import PhotoImage

class CCT:

    def __init__(self):

        #Create a new Window
        self.SI = tk.Tk()
        self.SI.geometry("1000x500")
        self.SI.title("Covid Contact Tracing Application")
        self.SI.resizable(False,False)

        #Create a main frame
        self.Main_frame = tk.Frame(self.SI, bg='lemon chiffon', relief = "sunken", bd=5 )
        self.Main_frame.pack(fill="both", expand=1)

        #Create Frames
        self.blank = tk.Frame(self.Main_frame,bg='white', width=100, height=50  )
        self.blank.pack(fill="both", expand=1)

        

        #Text Frame 1 Title
        self.TextTitle = tk.Frame(self.Main_frame, relief='raise', bd=3,width=986, height=50).place(x=2,y=2)

        #Main Title
        main_title = tk.Label(self.Main_frame, text='Please confirm the following information...', font=('times new roman bold', 20)).place(x=3,y=5)

        #Text frame 1
        self.textframe = tk.Frame(self.blank, relief='groove',bd=3, width=495, height=500 )
        self.textframe.place(x=0,y=0)
        
        #Text Frame 2
        self.textframe1 = tk.Frame(self.blank, relief='groove', bd=3, width=500, height=450  )
        self.textframe1.place(x=492,y=0)

        #Personal Information Title
        PI_title= tk.Label(self.textframe, text='Personal Information:', font=('times new roman bold', 16),wraplength=400, justify="center", fg='black').place(x=5,y=50)
        border1 = tk.Frame(self.textframe, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=75)
        border2 = tk.Frame(self.textframe, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=50)
        
        #Personal Information Labels
        s_name = tk.Label(self.textframe, text='Name:', font=('times new roman', 12)).place(x=5,y=80)
        s_age = tk.Label(self.textframe, text='Age:', font=('times new roman', 12)).place(x=5,y=108)
        s_status = tk.Label(self.textframe, text='Status:', font=('times new roman', 12)).place(x=5,y=136)
        s_room = tk.Label(self.textframe, text='Room:', font=('times new roman', 12)).place(x=5,y=162)
        s_address = tk.Label(self.textframe, text='Address:', font=('times new roman', 12)).place(x=5,y=190)
        

        #Personal Information Entries

        #Health Declaration Title
        HDF_title= tk.Label(self.textframe, text='Health Conditions:', font=('times new roman bold', 16),wraplength=400, justify="center", fg='black').place(x=5,y=250)

        #Border
        border3 = tk.Frame(self.textframe, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=275)
        border4 = tk.Frame(self.textframe, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=250)

        #Health Declaration Labels
        s_V1 = tk.Label(self.textframe, text='Vaccination:', font=('times new roman', 12)).place(x=5,y=290)
        s_S1= tk.Label(self.textframe, text='Symptoms:', font=('times new roman', 12)).place(x=5,y=330)
        s_E1 = tk.Label(self.textframe, text='Covid Exposure:', font=('times new roman', 12)).place(x=5,y=370)
        s_CC1 = tk.Label(self.textframe, text='Covid Contact:', font=('times new roman', 12)).place(x=5,y=410)
        s_CT1 = tk.Label(self.textframe, text='Covid Tests:', font=('times new roman', 12)).place(x=5,y=450)

        #Health Declaration Entries
        #Border
        border4 = tk.Frame(self.textframe, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=480)

        #Contact Person Title
        PI_title= tk.Label(self.textframe1, text='Contact Person Details:', font=('times new roman bold', 16),wraplength=400, justify="center", fg='black').place(x=5,y=50)
        border1 = tk.Frame(self.textframe1, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=75)
        border2 = tk.Frame(self.textframe1, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=50)

        #Contact Person Labels
        s_CP_name = tk.Label(self.textframe1, text='Name:', font=('times new roman', 12)).place(x=5,y=80)
        s_CP_Relationship = tk.Label(self.textframe1, text='Relationship:', font=('times new roman', 12)).place(x=5,y=120)
        s_CP_CN = tk.Label(self.textframe1, text='Contact Number:', font=('times new roman', 12)).place(x=5,y=160)
        s_CP_Address = tk.Label(self.textframe1, text='Address:', font=('times new roman', 12)).place(x=5,y=200)

        #Contact Person Entries

        #Border
        border5 = tk.Frame(self.textframe1, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=250)

        #Insert Image
        Photo = "COVID_img.png"  
        image = PhotoImage(file=Photo)

        poster = tk.Label(self.textframe1, image=image).place(x=100, y=260)

        #Button Frame 1
        self.buttonframe = tk.Frame(self.blank,relief='groove', bd=3, width=500, height=50  )
        self.buttonframe.place(x=492,y=450)

        #Page 4 Back Button
        pg3_back = tk.Button(self.buttonframe, text="< Back",font=("arial underline",12),command=self.back_to_page3)
        pg3_back.place(x=5,y=3)

        #Page 4 Confirm Button
        pg3_next = tk.Button(self.buttonframe, text="Confirm",font=("arial underline",12),command=self.next_to_page5)
        pg3_next.place(x=415,y=3)


        self.SI.mainloop()

    def back_to_page3(self):
        print("HI")

    def next_to_page5(self):
        print("Hellow")

    def setvariables(self):
        pass

cct_app = CCT()

