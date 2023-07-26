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
        #Create Entries
        #Create Enter Button
        #Create Reset Button

        root.mainloop()

    def read_file(cf):
        try:
            with open(cf, 'r') as file:
                content = file.read()
                return content
        
        except FileNotFoundError:
            print(f'File not found: {cf}')
        except IOError:
            print(f'Error reading file: {cf}')

def next(self):
    print("Hellow world")


sample = Search_Entry()







