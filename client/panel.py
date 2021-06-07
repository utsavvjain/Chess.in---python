import tkinter
import tkinter.ttk
import tkinter.tix
from tmgrid import *
from chatwindow import *
from model import *
from notificationwindow import *
import sys
sys.path.append(".")
from common.common import *
class TMChessPanel(tkinter.Frame) :
    def __init__(self,master,client,callbackFn,inviteClicked,invitationHandler) :
        tkinter.Frame.__init__(self,master,height=386,width=200,highlightbackground="black",highlightthickness=1,bg="black")
        self.state=""
        self.calbackFn=callbackFn
        self.activeGridWindow=None
        self.invitationGridWindow=None
        self.chatboxWindow=None 
        self.notification_window=None 
        self.homeImg=tkinter.PhotoImage(file="image//home.png")
        self.chatImg=tkinter.PhotoImage(file="image//chat.png")
        self.invitationImg=tkinter.PhotoImage(file="image//invitation.png")
        self.activeUsersImg=tkinter.PhotoImage(file="image//activeusers.png")
        self.tip=tkinter.tix.Balloon(master)
        for sub in self.tip.subwidgets_all() : 
            sub.config(bg="white") 
        self.canvas=tkinter.Canvas(self,height=386,width=200,highlightbackground="black",highlightthickness=2,bg="#283747")
        self.canvas.grid(row=0,column=0)
        self.img=tkinter.PhotoImage(file="image//chessbg1.ppm")
        self.canvas.create_image(0,0,image=self.img,anchor="nw")
        self.canvas.create_text(100,15,text="Chess.in",fill="white",font=("Arial Rounded MT",18,"bold"))
        self.canvas.create_line(0,30,200,30,fill="white",width=5)               
        self.canvas.create_text(100,40,text="Notification Tray",fill="white",font=("Times New Roman",12,"bold"))
        self.homeButton=self.button=tkinter.Button(self,bg="grey",fg="white",border=0,width=30,font=("Verdana",12,"bold"),command=self.showHome,image=self.homeImg)
        self.tip.bind_widget(self.homeButton,balloonmsg="Main Feed")
        self.canvas.create_window(15,54,window=self.homeButton,anchor="nw") 
        self.availableUsersButton=self.button=tkinter.Button(self,bg="grey",fg="white",border=0,width=30,font=("Verdana",12,"bold"),command=self.showAvailableUsers,image=self.activeUsersImg)
        self.tip.bind_widget(self.availableUsersButton,balloonmsg="Active Users")
        self.canvas.create_window(65,54,window=self.availableUsersButton,anchor="nw") 
        self.invitationButton=self.button=tkinter.Button(self,text="IV",bg="grey",fg="white",border=0,width=30,font=("Verdana",12,"bold"),command=self.showInvitations,image=self.invitationImg)
        self.tip.bind_widget(self.invitationButton,balloonmsg="Invitations")
        self.canvas.create_window(115,54,window=self.invitationButton,anchor="nw") 
        self.chatButton=self.button=tkinter.Button(self,text="CB",bg="grey",fg="white",border=0,width=30,font=("Verdana",12,"bold"),command=self.showChatbox,image=self.chatImg)
        self.chatButton['state']="disabled" 
        self.tip.bind_widget(self.chatButton,balloonmsg="Chat box")
        self.canvas.create_window(165,54,window=self.chatButton,anchor="nw") 
        self.canvas.create_line(0,90,200,90,fill="white",width=5)               
        self.headText=self.canvas.create_text(100,110,text="Home",fill="white",font=("Arial Rounded MT",12,"bold"))       
        self.activeUsersDataModel=ActiveUsersDataModel()        
        self.activeUsersDataModel.editCommand=inviteClicked
        self.activeUsersGrid=TMGrid(self,self.activeUsersDataModel,180,180)
        self.chatWindow=ChatWindow(self,170,180,client,callbackFn)
        self.notificationWindowText=self.canvas.create_text(100,215,text="Notification Window",fill="white",font=("Cooper",14,"bold"))
        self.notificationWindow=NotificationWindow(self,70,180)
        self.notification_window=self.canvas.create_window(7,230,window=self.notificationWindow,anchor="nw")
        self.turnText=self.canvas.create_text(100,360,text="",fill="white",font=("Cooper",14,"bold"))
        self.checkText=self.canvas.create_text(100,135,text="",fill="red",font=("Cooper",14,"bold"))
        self.invitationDataModel=InvitationDataModel()
        self.invitationDataModel.editCommand=invitationHandler
        self.invitationGrid=TMGrid(self,self.invitationDataModel,180,180)
    def showAvailableUsers(self) :
        self.state="AvailableUsers"
        self.canvas.itemconfigure(self.headText,text="Active Users")
        if self.invitationGridWindow is not None : self.canvas.delete(self.invitationGridWindow)
        if self.chatboxWindow is not None : self.canvas.delete(self.chatboxWindow)
        self.eraseHomeScreen()
        self.activeGridWindow=self.canvas.create_window(7,120,window=self.activeUsersGrid,anchor="nw") 
        self.invitationGridWindow=None
        self.chatboxWindow=None 
        self.canvas.update()
    def showInvitations(self) :
        self.state="Invitations"
        self.invitationButton.configure(image=self.invitationImg)
        self.canvas.itemconfigure(self.headText,text="Invitations")
        if self.activeGridWindow is not None : self.canvas.delete(self.activeGridWindow)
        if self.chatboxWindow is not None : self.canvas.delete(self.chatboxWindow)
        self.invitationGridWindow=self.canvas.create_window(7,120,window=self.invitationGrid,anchor="nw") 
        self.eraseHomeScreen()
        self.activeGridWindow=None
        self.chatboxWindow=None 
        self.canvas.update()
    def showChatbox(self) :
        self.state="Chatbox"
        self.chatButton.configure(image=self.chatImg) 
        self.canvas.itemconfigure(self.headText,text="Chat Box")
        if self.activeGridWindow is not None : self.canvas.delete(self.activeGridWindow)
        if self.invitationGridWindow is not None : self.canvas.delete(self.invitationGridWindow)
        self.chatboxWindow=self.canvas.create_window(4,120,window=self.chatWindow,anchor="nw")   
        self.eraseHomeScreen()
        self.activeGridWindow=None
        self.invitationGridWindow=None
        self.canvas.update()
    def showHome(self) :
        self.state="Home"
        self.canvas.itemconfigure(self.headText,text="Home")
        if self.activeGridWindow is not None : self.canvas.delete(self.activeGridWindow)
        if self.invitationGridWindow is not None : self.canvas.delete(self.invitationGridWindow)
        if self.chatboxWindow is not None : self.canvas.delete(self.chatboxWindow)        
        self.notification_window=self.canvas.create_window(7,230,window=self.notificationWindow,anchor="nw")   
    def eraseHomeScreen(self) : 
        if self.notification_window is not None : self.canvas.delete(self.notification_window)
        self.notification_window=None
        self.canvas.update()
    def updateTurnText(self,msg) :
        self.canvas.itemconfigure(self.turnText,text=msg)
    def updateCheckText(self,msg,check=False) :
        self.canvas.itemconfigure(self.checkText,text=msg)