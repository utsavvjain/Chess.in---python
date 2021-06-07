import tkinter
import tkinter.ttk
import sys
import time
from panel import *
from authentication import *
import tkinter.messagebox
sys.path.append(".")
from common.common import *
from move_validations import *
from network_common.wrappers import Request,Response,Wrapper
from network_client.client import NetworkClient
import tkinter.font
class TMChess(tkinter.tix.Tk) :
    isPeiceSelected=False
    oldPos=None
    def __init__(self,client) :
        self.client=client
        tkinter.tix.Tk.__init__(self)
        screenHeight=self.winfo_screenheight()
        screenWidth=self.winfo_screenwidth() 
        frameWidth=600
        frameHeight=400
        frameX=int(screenWidth/2)-int(frameWidth/2)   
        frameY=int(screenHeight/2)-int(frameHeight/2)   
        self.geometry(f"{frameWidth}x{frameHeight}+{frameX}+{frameY}") 
        self.peice=None
        self.playingWith=None
        self.myTurn=False  
        self.title("Authenticate")
        self.authenticate()         
        self.highlightRect=None
    def fetchMessage(self) :
        request=Request(self.username,"getmessage")
        response=client.send(request)
        message=Wrapper.from_json(response.result_object_json_string)
        for msg in message : 
            string=f"{self.playingWith} : {msg}"  
            self.panel.chatWindow.append(string) 
        if len(message)>0 : 
            self.panel.notificationWindow.append(f"{time.strftime('%H:%M')} -> New chat received")
            if self.panel.state!="Chatbox" :self.panel.chatButton.configure(image=self.chatReceivedImage) 
        self.fetchMessageJob=self.after(2000,self.fetchMessage)
    def fetchLastMove(self) :
        request=Request(self.playingWith,"getLastMove")
        response=client.send(request)
        lastMove=Wrapper.from_json(response.result_object_json_string)
        for move in lastMove : 
            string=f"{time.strftime('%H:%M')} -> {self.playingWith} moved {move}"  
            self.panel.notificationWindow.append(string) 
        self.fetchLastMoveJob=self.after(2000,self.fetchLastMove)
    def callbackFn(self,action,arguments) :
         if action=="sendmessage" : 
              message=Message(self.playingWith,arguments)
              request=Request(self.username,"sendmessage",message)
              response=client.send(request)
    def initGame(self) :
        self.title(self.username)
        self.requestSent=False
        self.canvas=tkinter.Canvas(master=self,width=384,height=384) 
        self.canvas.grid(row=0,column=0)
        self.chatReceivedImage=tkinter.PhotoImage(file="image//chatR.png")
        self.invitationReceivedImage=tkinter.PhotoImage(file="image//inviteR.png")
        self.panel=TMChessPanel(self,client,self.callbackFn,self.inviteClicked,self.invitationHandler)
        self.panel.grid(row=0,column=1)         
        self.loadPeices()
        self.invitations=[] 
        self.invitationSent=[]
        self.playing=False 
        self.board=self.createBoardDataStructure()
        self.updateBoard()
        self.fetchAvailableUser()
        self.fetchInvitations() 
        self.protocol("WM_DELETE_WINDOW",self.close) 
        self.sentImg=tkinter.PhotoImage(file="image//sent.png")
    def authenticate(self) :
        self.authenticationFrame=AuthenticationFrame(self,self.authenticationCallback)
        self.authenticationFrame.grid(row=0,column=0)         
    def authenticationCallback(self) :
        self.username=self.authenticationFrame.usernameEntry.get()
        password=self.authenticationFrame.passwordEntry.get()
        member=Member(self.username,password)
        request=Request(self.username,"authenticate",member)  
        response=self.client.send(request)
        if response.success==False :
            tkinter.messagebox.showinfo(title="Notification",message="Invalid username or password")      
            self.authenticationFrame.usernameEntry.focus()
            return
        self.authenticationFrame.grid_remove()
        self.initGame()
        self.panel.notificationWindow.append(f"{time.strftime('%H:%M')} -> Logged in successfully")
    def initalizeNewGame(self) :
        if self.peice=="White" :
            self.board[0][0]="br"
            self.board[0][1]="bkt"
            self.board[0][2]="bb"
            self.board[0][3]="bk"
            self.board[0][4]="bq"
            self.board[0][5]="bb"
            self.board[0][6]="bkt"
            self.board[0][7]="br"
            self.board[1][0]="bp"
            self.board[1][1]="bp"
            self.board[1][2]="bp"
            self.board[1][3]="bp"
            self.board[1][4]="bp"
            self.board[1][5]="bp"
            self.board[1][6]="bp"
            self.board[1][7]="bp"
            self.board[7][0]="wr"
            self.board[7][1]="wkt"
            self.board[7][2]="wb"
            self.board[7][3]="wk"
            self.board[7][4]="wq"
            self.board[7][5]="wb"
            self.board[7][6]="wkt"
            self.board[7][7]="wr"
            self.board[6][0]="wp"
            self.board[6][1]="wp"
            self.board[6][2]="wp"
            self.board[6][3]="wp"
            self.board[6][4]="wp"
            self.board[6][5]="wp"
            self.board[6][6]="wp"
            self.board[6][7]="wp"
        if self.peice=="Black" :
            self.board[0][0]="wr"
            self.board[0][1]="wkt"
            self.board[0][2]="wb"
            self.board[0][3]="wk"
            self.board[0][4]="wq"
            self.board[0][5]="wb"
            self.board[0][6]="wkt"
            self.board[0][7]="wr"
            self.board[1][0]="wp"
            self.board[1][1]="wp"
            self.board[1][2]="wp"
            self.board[1][3]="wp"
            self.board[1][4]="wp"
            self.board[1][5]="wp"
            self.board[1][6]="wp"
            self.board[1][7]="wp"
            self.board[7][0]="br"
            self.board[7][1]="bkt"
            self.board[7][2]="bb"
            self.board[7][3]="bk"
            self.board[7][4]="bq"
            self.board[7][5]="bb"
            self.board[7][6]="bkt"
            self.board[7][7]="br"
            self.board[6][0]="bp"
            self.board[6][1]="bp"
            self.board[6][2]="bp"
            self.board[6][3]="bp"
            self.board[6][4]="bp"
            self.board[6][5]="bp"
            self.board[6][6]="bp"
            self.board[6][7]="bp"
        request=Request(self.username,"updateBoardDS",UpdateDS(self.playingWith,self.board)) 
        response=self.client.send(request)
    def loadPeices(self) :
        self.peices={}
        self.peices["wr"]=tkinter.PhotoImage(file="image//wr.png")               
        self.peices["wkt"]=tkinter.PhotoImage(file="image//wkt.png")               
        self.peices["wb"]=tkinter.PhotoImage(file="image//wb.png")               
        self.peices["wk"]=tkinter.PhotoImage(file="image//wk.png")               
        self.peices["wq"]=tkinter.PhotoImage(file="image//wq.png")               
        self.peices["wp"]=tkinter.PhotoImage(file="image//wp.png")               
        self.peices["br"]=tkinter.PhotoImage(file="image//br.png")               
        self.peices["bkt"]=tkinter.PhotoImage(file="image//bkt.png")               
        self.peices["bb"]=tkinter.PhotoImage(file="image//bb.png")               
        self.peices["bk"]=tkinter.PhotoImage(file="image//bk.png")               
        self.peices["bq"]=tkinter.PhotoImage(file="image//bq.png")               
        self.peices["bp"]=tkinter.PhotoImage(file="image//bp.png")               
    def fetchInvitations(self) :       
        request=Request(self.username,"getInvitations")
        response=client.send(request)
        invitations=Wrapper.from_json(response.result_object_json_string)
        if invitations!=self.invitations and len(invitations)>0 : 
            self.panel.notificationWindow.append(f"{time.strftime('%H:%M')} -> New invite received")
            if self.panel.state!="Invitations" : self.panel.invitationButton.configure(image=self.invitationReceivedImage)
        self.invitations=invitations 
        self.panel.invitationDataModel.updateDS(self.invitations)
        self.panel.invitationGrid.update()
        self.after(2000,self.fetchInvitations)                  
    def close(self) :
        request=Request(self.username,"logout")        
        self.client.send(request)
        if self.playingWith!=None : 
            request=Request(self.username,"gameTerminate",Wrapper(self.playingWith))        
            self.client.send(request)
        self.destroy()
    def fetchAvailableUser(self) :
        request=Request(self.username,"getAvailableUser")
        response=client.send(request)
        availableUsers=Wrapper.from_json(response.result_object_json_string)
        if self.username in availableUsers: availableUsers.remove(self.username)
        self.panel.activeUsersDataModel.updateDS(availableUsers)
        self.panel.activeUsersGrid.update()
        self.after(2000,self.fetchAvailableUser)          
    def createBoardDataStructure(self) :
        board=list()
        for x in range(8) :
            board.append(list())
            for y in range(8) :
                board[x].append(None)
        return board
    def updateBoard(self) :
        ycor=0
        for x in range(8) :
            xcor=0
            for y in range(8) :
                if (x+y)%2==0 : self.canvas.create_rectangle(xcor,ycor,xcor+48,ycor+48,fill="#CCB7AE",width=0)
                else : self.canvas.create_rectangle(xcor,ycor,xcor+48,ycor+48,fill="#706677",width=0)
                if self.board[x][y]!=None : self.canvas.create_image(xcor,ycor,image=self.peices[self.board[x][y]],anchor="nw")
                xcor+=48
            ycor+=48
    def onChessBoardClicked(self,event) :
        if TMChess.isPeiceSelected :
            if self.highlightRect is not None : self.canvas.delete(self.highlightRect)
            self.highlightRect=None
            peice=self.board[TMChess.oldPos[0]][TMChess.oldPos[1]]
            newPos=(self.getBoardY(event.y),self.getBoardX(event.x))
            if peice=="bp" or peice== "wp" : 
                valid=Pawn.isValidMove(self.board,TMChess.oldPos,newPos,self.peice)
                if valid==False : 
                    TMChess.isPeiceSelected=False 
                    return  
            elif peice=="wr" or peice== "br" : 
                valid=Rook.isValidMove(self.board,TMChess.oldPos,newPos,self.peice)            
                if valid==False : 
                    TMChess.isPeiceSelected=False 
                    return  
            elif peice=="wkt" or peice== "bkt" : 
                valid=Knight.isValidMove(self.board,TMChess.oldPos,newPos,self.peice)            
                if valid==False :
                    TMChess.isPeiceSelected=False 
                    return  
            elif peice=="bb" or peice== "wb" : 
                valid=Bishop.isValidMove(self.board,TMChess.oldPos,newPos,self.peice)            
                if valid==False :
                    TMChess.isPeiceSelected=False 
                    return  
            elif peice=="bq" or peice== "wq" : 
                valid=Queen.isValidMove(self.board,TMChess.oldPos,newPos,self.peice)            
                if valid==False :
                    TMChess.isPeiceSelected=False 
                    return  
            elif peice=="bk" or peice== "wk" : 
                valid=King.isValidMove(self.board,TMChess.oldPos,newPos,self.peice)            
                if valid==False :
                    TMChess.isPeiceSelected=False 
                    return  
            self.playing=False 
            self.board[TMChess.oldPos[0]][TMChess.oldPos[1]]=None
            self.board[newPos[0]][newPos[1]]=peice            
            if King.isGettingCheck(self.board,self.peice)==True: 
                TMChess.isPeiceSelected=False 
                self.board=self.oldBoard
                TMChess.isPeiceSelected=False 
                self.panel.updateCheckText("ILLEGAL MOVE",King.isGettingCheck(self.board,self.peice))
                return
            else : self.panel.updateCheckText("")
            request=Request(self.username,"updateBoardDS",UpdateDS(self.playingWith,self.board)) 
            response=self.client.send(request)
            self.updateBoard() 
            if self.peice=="Black" : 
                if peice=="bp" : request=Request(self.username,"updateLastMove",Wrapper(f"pawn from {chr(97+TMChess.oldPos[1])}{TMChess.oldPos[0]+1} to {chr(97+newPos[1])}{newPos[0]+1}"))
                elif peice=="br" : request=Request(self.username,"updateLastMove",Wrapper(f"rook from {chr(97+TMChess.oldPos[1])}{TMChess.oldPos[0]+1} to {chr(97+newPos[1])}{newPos[0]+1}"))
                elif peice=="bkt" : request=Request(self.username,"updateLastMove",Wrapper(f"knight from {chr(97+TMChess.oldPos[1])}{TMChess.oldPos[0]+1} to {chr(97+newPos[1])}{newPos[0]+1}"))
                elif peice=="bb" : request=Request(self.username,"updateLastMove",Wrapper(f"bishop from {chr(97+TMChess.oldPos[1])}{TMChess.oldPos[0]+1} to {chr(97+newPos[1])}{newPos[0]+1}"))
                elif peice=="bk" : request=Request(self.username,"updateLastMove",Wrapper(f"king from {chr(97+TMChess.oldPos[1])}{TMChess.oldPos[0]+1} to {chr(97+newPos[1])}{newPos[0]+1}"))
                elif peice=="bq" : request=Request(self.username,"updateLastMove",Wrapper(f"queen from {chr(97+TMChess.oldPos[1])}{TMChess.oldPos[0]+1} to {chr(97+newPos[1])}{newPos[0]+1}"))
            elif self.peice=="White" : 
                if peice=="wp" : request=Request(self.username,"updateLastMove",Wrapper(f"pawn from {chr(97+TMChess.oldPos[1])}{7-TMChess.oldPos[0]+1} to {chr(97+newPos[1])}{7-newPos[0]+1}"))
                elif peice=="wr" : request=Request(self.username,"updateLastMove",Wrapper(f"rook from {chr(97+TMChess.oldPos[1])}{7-TMChess.oldPos[0]+1} to {chr(97+newPos[1])}{7-newPos[0]+1}"))
                elif peice=="wkt" : request=Request(self.username,"updateLastMove",Wrapper(f"knight from {chr(97+TMChess.oldPos[1])}{7-TMChess.oldPos[0]+1} to {chr(97+newPos[1])}{7-newPos[0]+1}"))
                elif peice=="wb" : request=Request(self.username,"updateLastMove",Wrapper(f"bishop from {chr(97+TMChess.oldPos[1])}{7-TMChess.oldPos[0]+1} to {chr(97+newPos[1])}{7-newPos[0]+1}"))
                elif peice=="wk" : request=Request(self.username,"updateLastMove",Wrapper(f"king from {chr(97+TMChess.oldPos[1])}{7-TMChess.oldPos[0]+1} to {chr(97+newPos[1])}{7-newPos[0]+1}"))
                elif peice=="wq" : request=Request(self.username,"updateLastMove",Wrapper(f"queen from {chr(97+TMChess.oldPos[1])}{7-TMChess.oldPos[0]+1} to {chr(97+newPos[1])}{7-newPos[0]+1}"))
            response=self.client.send(request)                         
            self.panel.updateTurnText(f"{self.playingWith}'s turn")
            TMChess.isPeiceSelected=False             
            return
        if self.board[self.getBoardY(event.y)][self.getBoardX(event.x)]==None : return
        if self.playing==False : return
        TMChess.oldPos=(self.getBoardY(event.y),self.getBoardX(event.x))             
        TMChess.isPeiceSelected=True
        self.oldBoard=self.board 
        if (self.peice=="Black" and self.board[TMChess.oldPos[0]][TMChess.oldPos[1]][0]=="b") or (self.peice=="White" and self.board[TMChess.oldPos[0]][TMChess.oldPos[1]][0]=="w") :
            self.highlightRect=self.canvas.create_rectangle(TMChess.oldPos[1]*48,TMChess.oldPos[0]*48,(TMChess.oldPos[1]+1)*48,(TMChess.oldPos[0]+1)*48,width=2,outline="black")
    def getBoardX(self,mouseX) :
        xc=0
        for x in range(8) :
            if mouseX>=xc and mouseX<=xc+47 : return x
            xc+=48
        return -1 
    def getBoardY(self,mouseY) :
        yc=0
        for y in range(8) :
            if mouseY>=yc and mouseY<=yc+47 : return y
            yc+=48
        return -1 
    def inviteClicked(self,rowIndex,columnIndex) :
        invitation=Invitation(self.username,self.panel.activeUsersDataModel.data[rowIndex])
        request=Request(self.username,"invite",invitation)
        response=self.client.send(request)
        self.panel.notificationWindow.append(f"{time.strftime('%H:%M')} -> Invitation sent to : {self.panel.activeUsersDataModel.data[rowIndex]}")
        self.panel.activeUsersDataModel.buttons[self.panel.activeUsersDataModel.data[rowIndex]]["state"]="disabled" 
        self.invitationSent.append(self.panel.activeUsersDataModel.data[rowIndex])
        self.panel.activeUsersDataModel.buttons[self.panel.activeUsersDataModel.data[rowIndex]].configure(image=self.sentImg)  
        self.invitationCheckJob=self.after(2000,self.isInviteAccepted)
    def isInviteAccepted(self) :
        for name in self.invitationSent :
            request=Request(self.username,"isInviteAccepted",Wrapper(name))
            response=self.client.send(request)        
            if response.success==True :
                self.playingWith=name
                self.playing=True
                self.panel.updateTurnText("your turn")
                self.peice="White" 
                self.initalizeNewGame()
                self.after_cancel(self.invitationCheckJob)
                self.fetchMessage()   
                self.fetchLastMove()
                self.panel.chatButton['state']="normal" 
                self.fetchDS() 
                self.updateBoard()  
                self.isPlayerConnected()
                self.isGameWon()
                self.canvas.bind("<Button-1>",self.onChessBoardClicked)
                self.panel.notificationWindow.append(f"{time.strftime('%H:%M')} -> {name} accepted invitation, starting new game")
                self.invitationSent.remove(name)
                request=Request(self.username,"withdrawInvite",Wrapper(self.invitationSent))
                response=self.client.send(request) 
                break
            if self.playingWith==None : self.after(2000,self.isInviteAccepted)                 
    def invitationHandler(self,rowIndex,columnIndex) :
         if columnIndex==2 :  
             name=self.panel.invitationDataModel.data[rowIndex]
             request=Request(self.username,"declineInvitation",Wrapper(name))             
             response=self.client.send(request)
             Wrapper(self.panel.invitationDataModel.removeData(name))
             self.panel.invitationGrid.update()
         if columnIndex==1 :
             request=Request(self.username,"acceptInvitation",Wrapper(self.panel.invitationDataModel.data[rowIndex]))
             response=self.client.send(request)
             self.panel.chatButton['state']="normal"
             self.playingWith=self.panel.invitationDataModel.data[rowIndex]
             self.playing=False
             self.panel.updateTurnText(f"{self.playingWith}'s turn")
             self.peice="Black"   
             self.initalizeNewGame()
             self.fetchMessage()
             self.fetchLastMove()
             self.fetchDS() 
             self.updateBoard()
             self.isPlayerConnected()
             self.isGameWon()
             self.canvas.bind("<Button-1>",self.onChessBoardClicked)
    def fetchDS(self) :
        request=Request(self.username,"getBoardDS")
        response=client.send(request)
        brd=Wrapper.from_json(response.result_object_json_string)
        diff=False
        for r in range(8):
            for c in range(8) :
                if self.board[r][c]!=brd[r][c] : 
                    diff=True
                    break    
        if self.board!=brd : 
            self.board=brd
            self.updateBoard()
            if self.peice=="Black" :
                if King.isGettingCheck(self.board,"Black")  :
                    if King.isCheckMate(self.board,"Black") : 
                        self.panel.updateCheckText("Check Mate")
                        self.gameLost()
                        return   
                    else : self.panel.updateCheckText("Check")
                else : self.panel.updateCheckText("")             
            if self.peice=="White" :
                if King.isGettingCheck(self.board,"White")  :
                    if King.isCheckMate(self.board,"White") :
                        self.panel.updateCheckText("Check Mate")
                        self.gameLost()   
                        return   
                    else : self.panel.updateCheckText("Check")
                else : self.panel.updateCheckText("") 
            self.playing=True 
            self.panel.updateTurnText("your turn")
        self.fetchDSJob=self.after(1000,self.fetchDS)                
    def isPlayerConnected(self) :
        request=Request(self.username,"isPlayerPlaying",Wrapper(self.playingWith))
        response=self.client.send(request)
        if response.success==False :
            self.board=self.createBoardDataStructure()
            self.updateBoard()
            self.panel.notificationWindow.append(f"{time.strftime('%H:%M')} -> {self.playingWith} left the game")
            self.playingWith=None
            self.after_cancel(self.fetchMessageJob)
            self.after_cancel(self.fetchDSJob)
            self.after_cancel(self.fetchLastMoveJob)     
            self.panel.chatButton['state']="disabled" 
            self.panel.updateTurnText("")
        else : self.isPlayerConnectedJob=self.after(2000,self.isPlayerConnected)
    def gameOver(self) : 
        self.board=self.createBoardDataStructure()
        self.updateBoard()
        self.panel.notificationWindow.append(f"{time.strftime('%H:%M')} -> Game finished")
        self.playingWith=None
        self.after_cancel(self.fetchMessageJob)
        self.after_cancel(self.fetchDSJob)
        self.after_cancel(self.fetchLastMoveJob)     
        self.panel.chatButton['state']="disabled" 
        self.after_cancel(self.isPlayerConnectedJob)
    def gameLost(self) : 
        request=Request(self.username,"lostGame",Wrapper(self.playingWith))        
        self.client.send(request)
        self.after(4000,self.gameOver)
        self.panel.updateTurnText("YOU LOST!!") 
    def isGameWon(self) :
        request=Request(self.username,"isGameWon",Wrapper(self.playingWith))
        response=self.client.send(request) 
        if response.success==True : 
            self.after(5000,self.gameOver)
            self.panel.updateTurnText("YOU WON!!") 
        else : self.after(2000,self.isGameWon)
client=NetworkClient()
sb=TMChess(client)
sb.mainloop()                                                                                                                                                                                                                                                                                                                                                                                                     