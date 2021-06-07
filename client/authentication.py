import tkinter
import tkinter.ttk
class AuthenticationFrame(tkinter.Frame) :
    def __init__(self,master,callback) :
        tkinter.Frame.__init__(self,master,height=400,width=600,highlightbackground="black",highlightthickness=1,bg="black")
        self.canvas=tkinter.Canvas(self,height=400,width=600)
        self.img=tkinter.PhotoImage(file="image//chessbg.ppm")
        self.canvas.create_image(0,0,anchor="nw",image=self.img) 
        self.canvas.create_text(30,20,text="Chess.in",fill="White",font=("Verdana",25,"bold"),anchor="nw") 	
        entryFont=tkinter.font.Font(family="Comic Sans MS",size=14,weight="bold")
        self.canvas.create_text(80,150,text="Username",fill="White",font=entryFont,anchor="nw")
        self.usernameEntry=tkinter.Entry(self,width=20,border=2,font=("Verdana",12))
        self.canvas.create_window(180,155,anchor="nw",window=self.usernameEntry)  
        self.canvas.create_text(80,200,text="Password",fill="White",font=entryFont,anchor="nw") 
        self.passwordEntry=tkinter.Entry(self,width=20,border=2,font=("Verdana",12),show="*")
        self.canvas.create_window(180,205,anchor="nw",window=self.passwordEntry)   
        self.button=tkinter.Button(self,text="Login",bg="grey",fg="white",border=0,width=10,font=("Verdana",12,"bold"),command=callback)
        self.canvas.create_window(270,250,anchor="nw",window=self.button )  
        self.canvas.grid(row=0,column=0)
        self.canvas.pack(fill=tkinter.BOTH,expand=1) 
