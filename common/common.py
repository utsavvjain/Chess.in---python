import json
class UpdateDS :
    def __init__(self,of,ds) :
        self.of=of
        self.ds=ds
    def to_json(self) :
        return json.dumps(self.__dict__)
    def from_json(jsonString) :
        newDict=json.loads(jsonString)
        return UpdateDS(**newDict)
class Member :
    def __init__(self,member_id,password) :
        self.member_id=member_id
        self.password=password
    def to_json(self) :
        return json.dumps(self.__dict__)
    def from_json(jsonString) :
        newDict=json.loads(jsonString)
        return Member(**newDict)
class Invitation :
    def __init__(self,_from,to) :
        self._from=_from
        self.to=to
    def to_json(self) :
        return json.dumps(self.__dict__)
    def from_json(jsonString) :
        newDict=json.loads(jsonString)
        return Invitation(**newDict)
class Message :
    def __init__(self,to,msg) :         
        self.to=to
        self.msg=msg
    def to_json(self) :
        return json.dumps(self.__dict__)
    def from_json(jsonString) :
        newDict=json.loads(jsonString)
        return Message(**newDict)



