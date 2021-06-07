import tkinter
import tkinter.ttk
class ActiveUsersDataModel :
    def __init__(self) :
        self.data=[]
        self.images={}
        self.buttons={}
    def updateDS(self,ds) :
        self.data=ds         
    def getRowCount(self) :
        return len(self.data)
    def getColumnCount(self) :
        return 2
    def getColumnTitle(self,columnIndex) :
        if columnIndex==0 : return "Name"
        if columnIndex==1 : return "Invite"
    def getColumnWidth(self,columnIndex) :
        if columnIndex==0 : return 120
        if columnIndex==1: return 50
    def getValueAt(self,rowIndex,columnIndex) :
        if columnIndex==0 : return self.data[rowIndex]
        else :
            cellContent="image//invite.png"    
            if cellContent not in self.images :
                img=tkinter.PhotoImage(file=cellContent)
                self.images[cellContent]=img
            else :
                img=self.images[cellContent]
            if self.data[rowIndex] not in self.buttons :
                button=tkinter.Button(width=20,height=18,image=img,anchor=tkinter.NW,bg="grey",fg="white") 
                self.buttons[self.data[rowIndex]]=button
            else :
                button=self.buttons[self.data[rowIndex]]  
            return button 
    def getCellType(self,rowIndex,columnIndex) :
        if columnIndex==0: return "str"
        return "Button" 
    def getCellCommand(self,rowIndex,columnIndex) :
        if columnIndex==4 : return self.editCommand
    def addData(self,d) :
        self.data.append(d)
    def removeData(self,d) :
        if d in self.buttons :   
            self.buttons.pop(d)  
class InvitationDataModel :
    def __init__(self) :
        self.data=["Utsav","Rohan","Mohan","Shyam"]
        self.images={}
        self.acceptButtons=[]
        self.rejectButtons=[]
    def getRowCount(self) :
        return len(self.data)
    def updateDS(self,ds) :
        self.data=ds
    def getColumnCount(self) :
        return 3
    def getColumnTitle(self,columnIndex) :
        if columnIndex==0 : return "Name"
        if columnIndex==1 : return  "Accept"
        if columnIndex==2 : return "Reject" 
    def getColumnWidth(self,columnIndex) :
        if columnIndex==0 : return 80
        if columnIndex==1: return 50
        if columnIndex==2: return 50
    def getValueAt(self,rowIndex,columnIndex) :
        if columnIndex==0 : return self.data[rowIndex]
        if columnIndex==1 : 
            cellContent="image//accept.png"    
            if cellContent not in self.images :
                img=tkinter.PhotoImage(file=cellContent)
                self.images[cellContent]=img
            else :
                img=self.images[cellContent]
            button=tkinter.Button(width=20,height=18,image=img,anchor=tkinter.NW,bg="grey",fg="white") 
            self.acceptButtons.append(button)
            return button
        else :
            cellContent="image//reject.png"    
            if cellContent not in self.images :
                img=tkinter.PhotoImage(file=cellContent)
                self.images[cellContent]=img
            else :
                img=self.images[cellContent]
            button=tkinter.Button(width=20,height=18,image=img,anchor=tkinter.NW,bg="grey",fg="white") 
            self.rejectButtons.append(button)
            return button
    def getCellType(self,rowIndex,columnIndex) :
        if columnIndex==0: return "str"
        else : return "Button" 
    def getCellCommand(self,rowIndex,columnIndex) :
        if columnIndex==4 : return self.editCommand
        return None
    def addData(self,d) :
        self.data.append(d)
    def removeData(self,d) :
        self.data.remove(d)
