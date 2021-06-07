import tkinter
import tkinter.ttk
import tkinter.font
import sys
sys.path.append(".")
from common.common import *
class NotificationWindow(tkinter.Frame) :
    def __init__(self,master,height,width) :
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
        hbar.config(command=self.canvas.xview)
        self.canvas.config(yscrollcommand=vbar.set,xscrollcommand=hbar.set) 
        self.canvas.pack(fill=tkinter.BOTH,expand=1)
        self.dataFont=tkinter.font.Font(family="Verdana",size=10,weight="bold")
        self.Y=0
        self.X=0
    def append(self,data) :
        self.canvas.create_text(7,self.Y+10,text=data,font=self.dataFont,anchor="nw",fill="white")
        self.Y+=self.dataFont.metrics('linespace')+10
        x=self.dataFont.measure(text=data)
        if x>self.X : self.X=x
        self.canvas.config(scrollregion=(0,0,self.X+15,self.Y+5))	
        self.canvas.yview_moveto('1.0')
        self.canvas.xview_moveto('0.0')