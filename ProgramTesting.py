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

