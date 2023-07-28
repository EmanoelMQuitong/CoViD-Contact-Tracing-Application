import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

from Data_Entry import Data_Entry
from Search_Entry import Search_Entry


pos = -1
class Main():
    def __init__(self):
        self.main = tk.Tk()

        self.main.geometry("400x300")
        self.main.title("Covid Contact Tracing Applicaiton")
        self.main.resizable(False,False)

        #Change Application Icon
        Change_Icon = 'COVID ICON.png' 
        new_icon =tk.PhotoImage(file=Change_Icon)
        self.main.iconphoto(True, new_icon)

        #Create Frame
        sub = tk.Frame(self.main, bg='dark slate gray', relief='sunken', bd=2).pack(fill="both", expand=1)

        #Create Label
        Choose = tk.Label(self.main, text="Choose function: ", fg='white',bg='dark slate gray', font=("helvetica",20)).place(x=75,y=50)
        
        #Create Frame
        blank_frame = tk.Frame(sub,bg='steel blue',width=300, height=175, relief='sunken', bd=5).place(x=50,y=100)

        #Create Enter Button
        enter = tk.Button(blank_frame, text='Data Entry',width=25, relief='raised', bd=5,font=('arial', 12), command=self.Data_entry). place(x=85, y=125)
        #Create Reset Button
        reset = tk.Button(blank_frame, text='Search Entry',width=25, relief='raised', bd=5, font=('arial', 12), command= self.Search_entry). place(x=85, y=175)

        #Create Quit Button
        reset = tk.Button(blank_frame, text='Quit',width=25, relief='raised', bd=5, font=('arial', 12), command= self.exit). place(x=85, y=225)



        self.main.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.main.mainloop()
    
    def exit(self):
        self.on_closing()

    def Data_entry(self):
        enter = Data_Entry()
        

    def Search_entry(self):
        Search = Search_Entry()
        

    def on_closing(self):
        if messagebox.askyesno(title="Are you sure?", message="Do you really want to quit?"):
            self.main.destroy()
    
        

sampl = Main()