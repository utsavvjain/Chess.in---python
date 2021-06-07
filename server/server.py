import sys
sys.path.append(".")
from network_server.server import NetworkServer
from network_common.wrappers import Request,Response,Wrapper
from threading import Thread
from common.common import *	
from data_layer.member_data_layer import MemberDataLayer
class ClientRepr :
    def __init__(self,username) :
        self.username=username
        self.invitations={}
        self.message=[]
        self.lastMove=[]
        self.board=self.createBoardDataStructure()
        self.playing=False
        self.won=False
    def getInvitations(self) :
        return self.invitations.keys()
    def addInvitation(self,username) :
        self.invitations.append(username) 
    def removeInvitation(self,username) :
        self.invitations.remove(username)     
    def createBoardDataStructure(self) :
        board=list()
        for x in range(8) :
            board.append(list())
            for y in range(8) :
                board[x].append(None)
        return board
class Server :
    _this=None
    _initalized=False
    _dataStructure=[]
    _members=dict()
    _activeUser=set()
    _playingUser=set()  
    _clientReprDict={}    
    def __new__(cls) :
        if Server._this==None : Server._this=super().__new__(cls)
        return Server._this
    def __init__(self) : 
        if Server._initalized==True : return 
        Server.populateDataStructures()
        Server._initalized=True
    def populateDataStructures() :
        registeredUsers=MemberDataLayer.getMembers()
        for member in registeredUsers : 
            Server._members[member.member_id]=member            
    def authenticate(username,password) :   
        if username in Server._members :
            if password==Server._members[username].password : return True
        return False
    def logout(username) :
        Server._activeUser.remove(username)
        if username in Server._playingUser  : Server._playingUser.remove(username)
        if username in Server._clientReprDict : Server._clientReprDict.pop(username)
    def requestHandler(request) :            
        username=request.manager.lower()
        if request.action=="authenticate" :
            member=Member.from_json(request.json_string)
            if Server.authenticate(member.member_id,member.password) :
                Server._activeUser.add(username)
                Server._clientReprDict[username]=ClientRepr(username)
                return Response(success=True)   
            else : return Response(success=False)
        elif request.action=="logout" :            
            Server.logout(username)                   
            return Response(success=True)
        elif request.action=="getAvailableUser" :
            if username not in Server._clientReprDict : return Response(success=False,result_object=Wrapper([]))
            availableUser=list(Server._activeUser-Server._playingUser)
            return Response(success=True,result_object=Wrapper(availableUser))
        elif request.action=="invite" :
            invitation=Invitation.from_json(request.json_string)
            Server._clientReprDict[invitation.to].invitations[username]=0
            return Response(success=True)
        elif request.action=="getInvitations" :
            if username not in Server._clientReprDict : return Response(success=False,result_object=Wrapper([]))
            invitations=[]
            for name in Server._clientReprDict[username].invitations.keys() :
                if  Server._clientReprDict[username].invitations[name]==0 :
                    invitations.append(name)            
            return Response(success=True,result_object=Wrapper(invitations))    
        elif request.action=="declineInvitation" :
            Server._clientReprDict[username].invitations[Wrapper.from_json(request.json_string)]=-1
            return Response(success=True)    
        elif request.action=="acceptInvitation" :
            name=Wrapper.from_json(request.json_string)
            Server._clientReprDict[username].invitations[name]=1
            Server._playingUser.add(username)
            Server._playingUser.add(name)
            return Response(success=True)  
        elif request.action=="isInviteAccepted" :
            name=Wrapper.from_json(request.json_string)
            if name in Server._clientReprDict : 
                    if username in Server._clientReprDict :
                        if name in Server._clientReprDict and username in Server._clientReprDict[name].invitations and Server._clientReprDict[name].invitations[username] ==1 :
                            return Response(success=True)
            return Response(success=False) 
        elif request.action=="sendmessage" :
            message=Message.from_json(request.json_string)
            Server._clientReprDict[message.to].message.append(message.msg)
            return Response(success=True)
        elif request.action=="getmessage" :
            if username not in Server._clientReprDict : return Response(success=False,result_object=Wrapper([]))
            message=Server._clientReprDict[username].message
            Server._clientReprDict[username].message=[]  
            return Response(success=True,result_object=Wrapper(message))
        elif request.action=="updateBoardDS" :
            updateDS=UpdateDS.from_json(request.json_string)
            Server._clientReprDict[username].board=updateDS.ds
            Server._clientReprDict[updateDS.of].board=updateDS.ds[::-1] 
            return Response(success=True)
        elif request.action=="getBoardDS"  :
            if username not in Server._clientReprDict : return Response(success=False,result_object=Wrapper([]))
            board=Server._clientReprDict[username].board
            return Response(success=True,result_object=Wrapper(board))  
        elif request.action=="updateLastMove" :
            lastMove=Wrapper.from_json(request.json_string)
            Server._clientReprDict[username].lastMove.append(lastMove)      
            return Response(success=True)
        elif request.action=="getLastMove" :
            if username not in Server._clientReprDict : return Response(success=False,result_object=Wrapper([]))
            lastMove=Server._clientReprDict[username].lastMove
            Server._clientReprDict[username].lastMove=[]  
            return Response(success=True,result_object=Wrapper(lastMove))
        elif request.action=="withdrawInvite" :
            invitationSent=Wrapper.from_json(request.json_string)
            for invitee in invitationSent :
                if invitee in Server._clientReprDict : Server._clientReprDict[invitee].invitations[username]=-1
            return Response(success=True) 
        elif request.action=="isPlayerPlaying" :
            if Wrapper.from_json(request.json_string) in Server._activeUser :
                return Response(success=True)
            else : return Response(success=False)
        elif request.action=="gameTerminate" : 
            name=Wrapper.from_json(request.json_string)
            if name in Server._playingUser : Server._playingUser.remove(name)
            if name in Server._clientReprDict : Server._clientReprDict.pop(name)
            return Response(success=True)
        elif request.action=="isGameWon" : 
            if username in Server._clientReprDict : 
                if Server._clientReprDict[username].won==True :
                    return Response(success=True)
            return Response(success=False) 
        elif request.action=="lostGame" :
            name=Wrapper.from_json(request.json_string)
            if name in Server._clientReprDict : 
                Server._clientReprDict[name].won=True 
                return Response(success=True)
            return Response(success=False) 
server=Server()
network_server=NetworkServer(Server.requestHandler)
network_server.start()

