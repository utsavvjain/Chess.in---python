import tkinter
import tkinter.ttk
import tkinter.font
import sys
sys.path.append(".")
from common.common import *
class CustomEntry(tkinter.Entry) :
    def __init__(self,master,placeholder,*args,**kwargs) :
        super().__init__(master,*args,**kwargs)
        self.placeholder=placeholder
        self.insert("0",self.placeholder)
        self.bind("<FocusIn>",self.clearPlaceHolder)
        self.bind("<FocusOut>",self.addPlaceHolder)
    def clearPlaceHolder(self,e) :
        self.delete(0,'end')
    def addPlaceHolder(self,e) :
        if not self.get() : self.insert("0",self.placeholder)
class ChatWindow(tkinter.Frame) :
    def __init__(self,master,height,width,client,callbackFn) :
        h=height
        w=width
        tkinter.Frame.__init__(self,master,height=h,width=w)
        self.canvas=tkinter.Canvas(self,bg="black",height=h,width=w)
        vbar=tkinter.Scrollbar(self,orient=tkinter.VERTICAL)
        vbar.pack(side=tkinter.RIGHT,fill=tkinter.Y) 
        vbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=vbar.set) 
        hbar=tkinter.Scrollbar(self,orient=tkinter.HORIZONTAL)
        hbar.pack(side=tkinter.BOTTOM,fill=tkinter.X)
        self.e=CustomEntry(self,placeholder="Type your message here",width=10,bg="black",fg="white")
        self.e.pack(side=tkinter.BOTTOM,fill=tkinter.X)
        self.e.bind('<Return>',self.callback)
        hbar.config(command=self.canvas.xview)
        self.canvas.config(yscrollcommand=vbar.set,xscrollcommand=hbar.set) 
        self.canvas.pack(fill=tkinter.BOTH,expand=1)
        self.dataFont=tkinter.font.Font(family="Verdana",size=10)
        self.Y=0
        self.X=0
        self.callbackFn=callbackFn
    def callback(self,event) :
        string=f"you : {self.e.get()}"
        if len(self.e.get())==0 : return  
        self.append(string)
        self.callbackFn("sendmessage",self.e.get())     
        self.e.delete(0,"end")
        self.canvas.focus_set()
    def append(self,data) :
        self.canvas.create_text(10,self.Y+10,text=data,font=self.dataFont,anchor="nw",fill="white")
        self.Y+=self.dataFont.metrics('linespace')+10
        x=self.dataFont.measure(text=data)
        if x>self.X : self.X=x
        self.canvas.config(scrollregion=(0,0,self.X+15,self.Y+5))	
        self.canvas.yview_moveto('1.0')
