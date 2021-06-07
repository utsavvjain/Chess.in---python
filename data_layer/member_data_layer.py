import json
import os.path
class Member :
    def __init__(self,member_id,password) :
        self.member_id=member_id
        self.password=password
    def to_json(self) :
        return json.dumps(self.__dict__)
    def from_json(jsonString) :
        newDict=json.loads(jsonString)
        return Member(**newDict)
class MemberDataLayer :
    if os.path.exists("users.txt")==False: 
        print("File users.txt missing read documentation")
        exit() 
    with open("users.txt") as f:
        members=json.load(f)
    _member=[]
    for key,value in members.items() : _member.append(Member(key,value))   
#    _member=[Member("amit","amit"),Member("rohan","rohan"),Member("sohan","sohan"),Member("akash","akash"),Member("mohan","mohan")]	
    def getMembers() :
        return MemberDataLayer._member