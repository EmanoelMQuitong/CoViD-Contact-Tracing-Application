import tkinter as tk

class Search_Entry():
    def __init__(self):
        root = tk.Tk()

        #Create a main frame
        root.geometry("200x200")
        root.title("Covid Contact Tracing Application")
        root.resizable(False,False)

        #Change Application Icon
        Change_Icon = 'COVID ICON.png' 
        new_icon =tk.PhotoImage(file=Change_Icon)
        root.iconphoto(True, new_icon)

        #Create Frame
        Main_frame = tk.Frame(root, bg='dark slate gray', relief='sunken', bd=2).pack(fill="both", expand=1)
        
        #Create Label
        Username = tk.Label(Main_frame, text="Username: ", fg='white',bg='dark slate gray', font=("helvetica",10)).place(x=65,y=50)
        Password = tk.Label(Main_frame, text="Password: ", fg='white',bg='dark slate gray', font=("helvetica",10)).place(x=65,y=125)
        
        #Create Variables
        self.User = tk.StringVar()
        self.Pass = tk.StringVar()
        self.User.set('******')
        self.Pass.set('******')

        #Create Entries
        username = tk.Entry(Main_frame, font=("helvetica",10), justify='center', textvariable=self.User, relief='sunken', bd=2).place(x=25,y=25)
        password = tk.Entry(Main_frame, font=("helvetica",10),justify='center', textvariable=self.Pass, relief='sunken', bd=2, show='*').place(x=25,y=100)


        #Create Enter Button
        enter = tk.Button(Main_frame, text='ENTER', font=('arial', 12), command=self.Enter). place(x=125, y=160)
        #Create Reset Button
        reset = tk.Button(Main_frame, text='RESET', font=('arial', 12), command= self.Reset). place(x=10, y=160)

        root.mainloop()

    def Enter(self):
        pass
    
    def Reset(self):
        self.User.set('******')
        self.Pass.set('******')


sample = Search_Entry()







