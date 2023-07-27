import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox

pos=-1
class cutie:

    def __init__(self):
        self.SE = tk.Tk()
            
        self.SE.geometry("1000x500")
        self.SE.title("Covid Contact Tracing Application")
        self.SE.resizable(False,False)

        #Create a main frame
        self.Main_frame = tk.Frame(self.SE, bg='lemon chiffon', relief = "sunken", bd=5 )
        self.Main_frame.pack(fill="both", expand=1)

        #Create Frames
        self.blank = tk.Frame(self.Main_frame,bg='white', width=100, height=50  )
        self.blank.pack(fill="both", expand=1)

        #Text Frame 1 Title
        self.TextTitle = tk.Frame(self.Main_frame, relief='raise', bd=3,width=986, height=50).place(x=2,y=2)

        #Search Text
        main_title = tk.Label(self.Main_frame, text='Search Here: ', font=('times new roman bold', 20)).place(x=3,y=5)

        #Search Button
        SB = tk.Button(self.Main_frame, text="Search",font=('times new roman bold', 16), command=self.search).place(x=890,y=5)

        #Search Variable
        self.SV = tk.StringVar()
        self.SV.set('Please enter name...')
            
        #Search Entry
        search_entry = tk.Entry(self.Main_frame, width =50,relief='sunken',textvariable=self.SV, bd=3,font=('times new roman bold', 20)).place(x=175,y=5)

            
        #Text frame 1
        self.textframe = tk.Frame(self.blank, relief='groove',bd=3, width=495, height=500 )
        self.textframe.place(x=0,y=0)
            
        #Text Frame 2
        self.textframe1 = tk.Frame(self.blank, relief='groove', bd=3, width=500, height=450  )
        self.textframe1.place(x=492,y=0)

        #Personal Information Title
        PI_title= tk.Label(self.textframe, text='Personal Information:', font=('time    s new roman bold', 16),wraplength=400, justify="center", fg='black').place(x=5,y=50)
        border1 = tk.Frame(self.textframe, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=75)
        border2 = tk.Frame(self.textframe, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=50)
            
        #Personal Information Labels
        s_name = tk.Label(self.textframe, text='Name:', font=('times new roman', 12)).place(x=5,y=80)
        s_age = tk.Label(self.textframe, text='Age:', font=('times new roman', 12)).place(x=5,y=108)
        s_status = tk.Label(self.textframe, text='Status:', font=('times new roman', 12)).place(x=5,y=136)
        s_room = tk.Label(self.textframe, text='Room:', font=('times new roman', 12)).place(x=5,y=162)
        s_address = tk.Label(self.textframe, text='Address:', font=('times new roman', 12)).place(x=5,y=190)
            
        #Variables
        self.SC_name =tk.StringVar()
        self.SC_name.set('*')

        #Personal Information Entries
        s_name = tk.Label(self.textframe, text=self.SC_name.get(), font=('times new roman', 12)).place(x=100,y=80)
        s_birthday = tk.Label(self.textframe, text='*', font=('times new roman', 12)).place(x=100,y=108)
        s_status = tk.Label(self.textframe, text='*', font=('times new roman', 12)).place(x=100,y=136)
        s_room = tk.Label(self.textframe, text='*', font=('times new roman', 12)).place(x=100,y=162)
        s_address = tk.Label(self.textframe, text='*',wraplength=300,justify='left', font=('times new roman', 11)).place(x=100,y=190)

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
        s_V1 = tk.Label(self.textframe, text='*', font=('times new roman', 12)).place(x=150,y=290)
        s_S1= tk.Label(self.textframe, text='*', font=('times new roman', 12)).place(x=150,y=330)
        s_E1 = tk.Label(self.textframe, text='*', font=('times new roman', 12)).place(x=150,y=370)
        s_CC1 = tk.Label(self.textframe, text='*', font=('times new roman', 12)).place(x=150,y=410)
        s_CT1 = tk.Label(self.textframe, text='*', font=('times new roman', 12)).place(x=150,y=450)

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
        s_CP_name = tk.Label(self.textframe1, text='*', font=('times new roman', 12)).place(x=150,y=80)
        s_CP_Relationship = tk.Label(self.textframe1, text='*', font=('times new roman', 12)).place(x=150,y=120)
        s_CP_CN = tk.Label(self.textframe1,text='*', font=('times new roman', 12)).place(x=150,y=160)
        s_CP_Address = tk.Label(self.textframe1,text='*', font=('times new roman', 12)).place(x=150,y=200)


        #Border
        border5 = tk.Frame(self.textframe1, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=250)

        #Insert Image
        Photo = "COVID_img.png"  
        image = PhotoImage(file=Photo)

        poster = tk.Label(self.textframe1, image=image).place(x=100, y=260)

        #Button Frame 1
        self.buttonframe = tk.Frame(self.blank,relief='groove', bd=3, width=500, height=50  )
        self.buttonframe.place(x=492,y=450)

        #Reset Button
        pg3_back = tk.Button(self.buttonframe, text="Reset",font=("arial underline",12),command=self.Reset1)
        pg3_back.place(x=5,y=3)

        #Finish Button
        pg3_next = tk.Button(self.buttonframe, text="Finish",font=("arial underline",12),command=self.Finish)
        pg3_next.place(x=415,y=3)

        self.SE.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.SE.mainloop()

    def Reset1(self):
        print("Reset")

    def Finish(self):
        pass

    #Read and Modify the Text from the Text file
    def change(self):
        file_path = "Stored Informations.txt"
        file =open(file_path, "r")
        lines = file.readlines()
        modified = []

        # Process the lines outside the 'with' block if needed
        for line in lines:
            modified.append(line.strip())  # Use strip() to remove newline characters
        self. modified = modified
        
        return modified

    #Search for the position of the Entered Name
    def search_name(self):
        i = 0
        while i< len(self.modified):
            if self.modified[i] == str(self.SV.get()):
                globals()['pos'] = i
                return pos
            i = i+1

        return messagebox.showerror("INVALID!", "Entered name was not found!")

    def search(self):
        print("Search")
        print(self.SC_name.set(self.change()[self.search_name()]))
        
        self.SE2 = tk.Toplevel(self.SE)
        self.SE2.geometry("1000x500")
        self.SE2.title("Covid Contact Tracing Application")
        self.SE2.resizable(False,False)

        #Create a main frame
        self.Main_frame = tk.Frame(self.SE2, bg='lemon chiffon', relief = "sunken", bd=5 )
        self.Main_frame.pack(fill="both", expand=1)

        #Create Frames
        self.blank1 = tk.Frame(self.Main_frame,bg='white', width=100, height=50  )
        self.blank1.pack(fill="both", expand=1)

        #Text Frame 1 Title
        self.TextTitle = tk.Frame(self.Main_frame, relief='raise', bd=3,width=986, height=50).place(x=2,y=2)

        #Search Text
        main_title = tk.Label(self.Main_frame, text='Search Here: ', font=('times new roman bold', 20)).place(x=3,y=5)

        #Search Button
        SB = tk.Button(self.Main_frame, text="Search",font=('times new roman bold', 16), command=self.search).place(x=890,y=5)

        #Search Variable
        self.SV = tk.StringVar()
        self.SV.set('Please enter name...')
            
        #Search Entry
        search_entry = tk.Entry(self.Main_frame, width =50,relief='sunken',textvariable=self.SV, bd=3,font=('times new roman bold', 20)).place(x=175,y=5)

            
        #Text frame 1
        self.textframe3 = tk.Frame(self.blank1, relief='groove',bd=3, width=495, height=500 )
        self.textframe3.place(x=0,y=0)
            
        #Text Frame 2
        self.textframe4 = tk.Frame(self.blank1, relief='groove', bd=3, width=500, height=450  )
        self.textframe4.place(x=492,y=0)

        #Personal Information Title
        PI_title= tk.Label(self.textframe3, text='Personal Information:', font=('time    s new roman bold', 16),wraplength=400, justify="center", fg='black').place(x=5,y=50)
        border1 = tk.Frame(self.textframe3, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=75)
        border2 = tk.Frame(self.textframe3, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=50)
            
        #Personal Information Labels
        s_name = tk.Label(self.textframe3, text='Name:', font=('times new roman', 12)).place(x=5,y=80)
        s_age = tk.Label(self.textframe3, text='Age:', font=('times new roman', 12)).place(x=5,y=108)
        s_status = tk.Label(self.textframe3, text='Status:', font=('times new roman', 12)).place(x=5,y=136)
        s_room = tk.Label(self.textframe3, text='Room:', font=('times new roman', 12)).place(x=5,y=162)
        s_address = tk.Label(self.textframe3, text='Address:', font=('times new roman', 12)).place(x=5,y=190)
            
        #Variables
        self.SC_name.set(self.change()[self.search_name()])

        #Personal Information Entries
        s_name = tk.Label(self.textframe3, text=self.SC_name.get(), font=('times new roman', 12)).place(x=100,y=80)
        s_birthday = tk.Label(self.textframe3, text='*', font=('times new roman', 12)).place(x=100,y=108)
        s_status = tk.Label(self.textframe3, text='*', font=('times new roman', 12)).place(x=100,y=136)
        s_room = tk.Label(self.textframe3, text='*', font=('times new roman', 12)).place(x=100,y=162)
        s_address = tk.Label(self.textframe3, text='*',wraplength=300,justify='left', font=('times new roman', 11)).place(x=100,y=190)

            #Health Declaration Title
        HDF_title= tk.Label(self.textframe3, text='Health Conditions:', font=('times new roman bold', 16),wraplength=400, justify="center", fg='black').place(x=5,y=250)

        #Border
        border3 = tk.Frame(self.textframe3, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=275)
        border4 = tk.Frame(self.textframe3, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=250)

        #Health Declaration Labels
        s_V1 = tk.Label(self.textframe3, text='Vaccination:', font=('times new roman', 12)).place(x=5,y=290)
        s_S1= tk.Label(self.textframe3, text='Symptoms:', font=('times new roman', 12)).place(x=5,y=330)
        s_E1 = tk.Label(self.textframe3, text='Covid Exposure:', font=('times new roman', 12)).place(x=5,y=370)
        s_CC1 = tk.Label(self.textframe3, text='Covid Contact:', font=('times new roman', 12)).place(x=5,y=410)
        s_CT1 = tk.Label(self.textframe3, text='Covid Tests:', font=('times new roman', 12)).place(x=5,y=450)

        #Health Declaration Entries
        s_V1 = tk.Label(self.textframe3, text='*', font=('times new roman', 12)).place(x=150,y=290)
        s_S1= tk.Label(self.textframe3, text='*', font=('times new roman', 12)).place(x=150,y=330)
        s_E1 = tk.Label(self.textframe3, text='*', font=('times new roman', 12)).place(x=150,y=370)
        s_CC1 = tk.Label(self.textframe3, text='*', font=('times new roman', 12)).place(x=150,y=410)
        s_CT1 = tk.Label(self.textframe3, text='*', font=('times new roman', 12)).place(x=150,y=450)

        #Border
        border4 = tk.Frame(self.textframe3, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=480)

        #Contact Person Title
        PI_title= tk.Label(self.textframe31, text='Contact Person Details:', font=('times new roman bold', 16),wraplength=400, justify="center", fg='black').place(x=5,y=50)
        border1 = tk.Frame(self.textframe31, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=75)
        border2 = tk.Frame(self.textframe31, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=50)

        #Contact Person Labels
        s_CP_name = tk.Label(self.textframe4, text='Name:', font=('times new roman', 12)).place(x=5,y=80)
        s_CP_Relationship = tk.Label(self.textframe4, text='Relationship:', font=('times new roman', 12)).place(x=5,y=120)
        s_CP_CN = tk.Label(self.textframe4, text='Contact Number:', font=('times new roman', 12)).place(x=5,y=160)
        s_CP_Address = tk.Label(self.textframe4, text='Address:', font=('times new roman', 12)).place(x=5,y=200)

        #Contact Person Entries
        s_CP_name = tk.Label(self.textframe4, text='*', font=('times new roman', 12)).place(x=150,y=80)
        s_CP_Relationship = tk.Label(self.textframe4, text='*', font=('times new roman', 12)).place(x=150,y=120)
        s_CP_CN = tk.Label(self.textframe4,text='*', font=('times new roman', 12)).place(x=150,y=160)
        s_CP_Address = tk.Label(self.textframe4,text='*', font=('times new roman', 12)).place(x=150,y=200)


        #Border
        border5 = tk.Frame(self.textframe4, bg='dark slate gray',relief='raised',bd=2, width=600,height=5).place(x=0,y=250)

        #Insert Image
        Photo = "COVID_img.png"  
        image = PhotoImage(file=Photo)

        poster = tk.Label(self.textframe4, image=image).place(x=100, y=260)

        #Button Frame 1
        self.buttonframe = tk.Frame(self.blank,relief='groove', bd=3, width=500, height=50  )
        self.buttonframe.place(x=492,y=450)

        #Reset Button
        pg3_back = tk.Button(self.buttonframe, text="Reset",font=("arial underline",12),command=self.Reset1)
        pg3_back.place(x=5,y=3)

        #Finish Button
        pg3_next = tk.Button(self.buttonframe, text="Finish",font=("arial underline",12),command=self.Finish)
        pg3_next.place(x=415,y=3)

        self.SE2.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.SE2.mainloop()

        self.SE2 = tk.Toplevel(self.SE)

    def on_closing(self):
        if messagebox.askyesno(title="Are you sure?", message="Do you really want to quit?"):
            self.SE.destroy()
samp = cutie()