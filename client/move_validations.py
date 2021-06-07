import copy
class King :
    def isValidMove(board,currPos,newPos,player) :
        currY=currPos[0]
        currX=currPos[1]     
        newY=newPos[0]
        newX=newPos[1]
        peice=board[currY][currX]
        if peice=="bk" and player=="White"  :return False
        if peice=="wk" and player=="Black"  :return False
        if abs(currY-newY)>1 or abs(currX-newX)>1 : return False
        if peice=="bk" :
            if board[newY][newX] is not None and board[newY][newX][0]=="b" : return False
            return True 
        if peice=="wk" :
            if board[newY][newX] is not None and board[newY][newX][0]=="w" : return False
            return True 
    def isGettingCheck(board,player) :
        whitePiecesPos={}
        blackPiecesPos={}
        i=0
        while i<len(board) :
            j=0
            while j<len(board[i]) :
                if board[i][j] is not None :
                    peice=board[i][j]
                    if peice[0]=='w' : whitePiecesPos[(i,j)]=peice
                    else : blackPiecesPos[(i,j)]=peice      
                j+=1
            i+=1 
        isGettingCheck=False 
        if player=="White" :          
            for key,val in whitePiecesPos.items():
                if val=="wk" : 
                    whiteKingY,whiteKingX=key  
                    break            
            isObstacle=False
            #########vertical moves#################
            for y in range(whiteKingY-1,-1,-1) :
                if board[y][whiteKingX] is not None :
                    if board[y][whiteKingX][0]=="w" : 
                        isObstacle=True 
                        break
                    if board[y][whiteKingX] in ("bkt","bp","bk","bb") :
                        if y==whiteKingY-1 and board[y][whiteKingX]=="bk":
                            isGettingCheck=True      
                            break  
                        isObstacle=True 
                        break
                    if  board[y][whiteKingX] in ("bq","br")  : 
                        isGettingCheck=True      
                        break  
            if isGettingCheck : return isGettingCheck   
            for y in range(whiteKingY+1,8,1) :
                if board[y][whiteKingX] is not None :
                    if board[y][whiteKingX][0]=="w" : 
                        isObstacle=True 
                        break
                    if board[y][whiteKingX] in ("bkt","bp","bk","bb") :
                        if y==whiteKingY+1 and board[y][whiteKingX]=="bk":
                            isGettingCheck=True      
                            break  
                        isObstacle=True 
                        break
                    if  board[y][whiteKingX] in ("bq","br")  : 
                        isGettingCheck=True      
                        break  
            if isGettingCheck : return isGettingCheck
            ############horizontal moves################
            for x in range(whiteKingX-1,-1,-1) :
                if board[whiteKingY][x] is not None :
                    if board[whiteKingY][x][0]=="w" : 
                        isObstacle=True 
                        break
                    if board[whiteKingY][x] in ("bkt","bp","bk","bb") :                    
                        if x==whiteKingX-1 and board[whiteKingY][x]=="bk":
                            isGettingCheck=True      
                            break  
                        isObstacle=True 
                        break
                    if board[whiteKingY][x] in ("bq","br")  : 
                        isGettingCheck=True      
                        break  
            if isGettingCheck : return isGettingCheck
            for x in range(whiteKingX+1,8,1) :
                if board[whiteKingY][x] is not None :
                    if board[whiteKingY][x][0]=="w" : 
                        isObstacle=True 
                        break
                    if board[whiteKingY][x] in ("bkt","bp","bk","bb") :
                        if x==whiteKingX+1 and board[whiteKingY][x]=="bk":
                            isGettingCheck=True      
                            break  
                        isObstacle=True 
                        break
                    if board[whiteKingY][x] in ("bq","br")  : 
                        isGettingCheck=True      
                        break  
            if isGettingCheck : return isGettingCheck
            ##################diagonal moves#########################
            yCor=whiteKingY+1
            for x in range(whiteKingX+1,8,1) :
                if yCor==8 : break 
                if board[yCor][x] is None : 
                    yCor+=1
                    continue 
                if board[yCor][x][0]=="w" :
                    isObstacle=True 
                    break
                if board[yCor][x] in ("br","bk","bp","bkt") :
                    if x==whiteKingX+1 and yCor==whiteKingY+1 and board[yCor][x]=="bp":
                        isGettingCheck=True      
                        break   
                    if x==whiteKingX+1 and yCor==whiteKingY+1 and board[yCor][x]=="bk":
                        isGettingCheck=True      
                        break   
                    isObstacle=True 
                    break  
                if board[yCor][x] in ("bq","bb") :                       
                    isGettingCheck=True      
                    break  
                yCor=+1
            if isGettingCheck : return isGettingCheck
            yCor=whiteKingY+1
            for x in range(whiteKingX-1,-1,-1) :
                if yCor==8 : break 
                if board[yCor][x] is None : 
                    yCor+=1
                    continue 
                if board[yCor][x][0]=="w" :
                    isObstacle=True 
                    break
                if board[yCor][x] in ("br","bk","bp","bkt") :
                    if x==whiteKingX-1 and yCor==whiteKingY+1 and board[yCor][x]=="bp":
                        isGettingCheck=True      
                        break   
                    isObstacle=True 
                    break
                    if x==whiteKingX-1 and y==whiteKingY+1 and board[yCor][x]=="bk":
                        isGettingCheck=True      
                        break   
                    isObstacle=True 
                    break
                if board[yCor][x] in ("bq","bb") :                       
                    isGettingCheck=True      
                    break  
                yCor=+1
            if isGettingCheck : return isGettingCheck
            xCor=whiteKingX+1 
            for y in range(whiteKingY-1,-1,-1) :
                if xCor==8 : break 
                if board[y][xCor] is None : 
                   xCor+=1
                   continue 
                if board[y][xCor][0]=="w" :
                    isObstacle=True 
                    break
                if board[y][xCor] in ("br","bk","bp","bkt") :
                    if xCor==whiteKingX+1 and y==whiteKingY-1 and board[y][xCor]=="bk":
                        isGettingCheck=True      
                        break   
                    isObstacle=True 
                    break
                if board[y][xCor] in ("bq","bb") :                       
                    isGettingCheck=True      
                    break              
                xCor+=1   
            if isGettingCheck : return isGettingCheck
            xCor=whiteKingX-1 
            for y in range(whiteKingY-1,-1,-1) :
                if xCor==-1 : break
                if board[y][xCor] is None : 
                    xCor-=1
                    continue 
                if board[y][xCor][0]=="w" :
                    isObstacle=True 
                    break
                if board[y][xCor] in ("br","bk","bp","bkt") :
                    if xCor==whiteKingX-1 and y==whiteKingY-1 and board[y][xCor]=="bk":
                        isGettingCheck=True      
                        break   
                    isObstacle=True 
                    break
                if board[y][xCor] in ("bq","bb") :                       
                    isGettingCheck=True      
                    break              
                xCor-=1 
            if isGettingCheck : return isGettingCheck
            ######################knight position####################
            knightsPos=[(whiteKingY-1,whiteKingX+2),(whiteKingY-1,whiteKingX-2),(whiteKingY+1,whiteKingX+2),(whiteKingY+1,whiteKingX-2),(whiteKingY+2,whiteKingX+1),(whiteKingY+2,whiteKingX-1),(whiteKingY-2,whiteKingX+1),(whiteKingY-2,whiteKingX-1)]
            for pos in knightsPos :
                y,x=pos
                if 0<=y<=7 and 0<=x<=7 : 
                    if board[y][x] is not None and board[y][x]=="bkt" :
                         isGettingCheck=True      
                         break                                       
        if player=="Black" : 
            for key,val in blackPiecesPos.items():                    
                if val=="bk" : 
                    blackKingY,blackKingX=key  
                    break            
            isObstacle=False
            #########vertical moves#################
            for y in range(blackKingY-1,-1,-1) :
                if board[y][blackKingX] is not None :
                    if board[y][blackKingX][0]=="b" : 
                        isObstacle=True 
                        break
                    if board[y][blackKingX] in ("wkt","wp","wk","wb") :
                        if y==blackKingY-1 and board[y][blackKingX]=="wk"  :
                            isGettingCheck=True      
                            break  
                        isObstacle=True 
                        break
                    if  board[y][blackKingX] in ("wq","wr")  : 
                        isGettingCheck=True      
                        break  
            if isGettingCheck : return isGettingCheck
            for y in range(blackKingY+1,8,1) :
                if board[y][blackKingX] is not None :
                    if board[y][blackKingX][0]=="b" : 
                        isObstacle=True 
                        break
                    if board[y][blackKingX] in ("wkt","wp","wk","wb") :
                        if y==blackKingY+1 and board[y][blackKingX]=="wk"  :
                            isGettingCheck=True      
                            break  
                        isObstacle=True 
                        break
                    if  board[y][blackKingX] in ("wq","wr")  : 
                        isGettingCheck=True      
                        break
            if isGettingCheck : return isGettingCheck  
            ############horizontal moves################
            for x in range(blackKingX-1,-1,-1) :
                if board[blackKingY][x] is not None :
                    if board[blackKingY][x][0]=="b" : 
                        isObstacle=True 
                        break
                    if board[blackKingY][x] in ("wkt","wp","wk","wb") :                    
                        if x==blackKingX-1 and board[blackKingY][x]=="wk"  :
                            isGettingCheck=True      
                            break  
                        isObstacle=True 
                        break
                    if board[blackKingY][x] in ("wq","wr")  : 
                        isGettingCheck=True      
                        break  
            if isGettingCheck : return isGettingCheck
            for x in range(blackKingX+1,8,1) :
                if board[blackKingY][x] is not None :
                    if board[blackKingY][x][0]=="b" : 
                        isObstacle=True 
                        break
                    if board[blackKingY][x] in ("wkt","wp","wk","wb") :
                        if x==blackKingX+1 and board[blackKingY][x]=="wk"  :
                            isGettingCheck=True      
                            break  
                        isObstacle=True 
                        break
                    if board[blackKingY][x] in ("wq","wr")  : 
                        isGettingCheck=True      
                        break  
            if isGettingCheck : return isGettingCheck
            ##################diagonal moves#########################
            yCor=blackKingY+1
            for x in range(blackKingX+1,8,1) :
                if yCor==8 : break 
                if board[yCor][x] is None : 
                    yCor+=1
                    continue 
                if board[yCor][x][0]=="b" :
                    isObstacle=True 
                    break
                if board[yCor][x] in ("wr","wk","wp","wkt") :
                    if x==blackKingX+1 and y==blackKingY+1 and board[yCor][x]=="wp":
                        isGettingCheck=True      
                        break   
                    if x==blackKingX+1 and y==blackKingY+1 and board[yCor][x]=="wk":
                        isGettingCheck=True      
                        break   
                    isObstacle=True 
                    break  
                if board[yCor][x] in ("wq","wb") :                       
                    isGettingCheck=True      
                    break  
                yCor=+1
            if isGettingCheck : return isGettingCheck
            yCor=blackKingY+1
            for x in range(blackKingX-1,-1,-1) :
                if yCor==8 : break 
                if board[yCor][x] is None : 
                    yCor+=1
                    continue 
                if board[yCor][x][0]=="b" :
                    isObstacle=True 
                    break
                if board[yCor][x] in ("wr","wk","wp","wkt") :
                    if x==blackKingX+1 and y==blackKingY+1 and board[yCor][x]=="wp":
                        isGettingCheck=True      
                        break   
                    if x==blackKingX+1 and y==blackKingY+1 and board[yCor][x]=="wk":
                        isGettingCheck=True      
                        break   
                    isObstacle=True 
                    break
                if board[yCor][x] in ("wq","wb") :                       
                    isGettingCheck=True      
                    break  
                yCor=+1
            if isGettingCheck : return isGettingCheck
            xCor=blackKingX+1 
            for y in range(blackKingY-1,-1,-1) :
                if xCor==8 : break 
                if board[y][xCor] is None : 
                   xCor+=1
                   continue 
                if board[y][xCor][0]=="b" :
                    isObstacle=True 
                    break
                if board[y][xCor] in ("wr","wk","wp","wkt") :
                    if xCor==blackKingX+1 and y==blackKingY-1 and board[y][xCor]=="wk":
                        isGettingCheck=True      
                        break   
                    isObstacle=True 
                    break
                if board[y][xCor] in ("wq","wb") :                       
                    isGettingCheck=True      
                    break              
                xCor+=1   
            if isGettingCheck : return isGettingCheck
            xCor=blackKingX-1 
            for y in range(blackKingY-1,-1,-1) :
                if xCor==-1 : break
                if board[y][xCor] is None : 
                    xCor-=1
                    continue 
                if board[y][xCor][0]=="b" :
                    isObstacle=True 
                    break
                if board[y][xCor] in ("wr","wk","wp","wkt") :
                    if xCor==blackKingX-1 and y==blackKingY-1 and board[y][xCor]=="wk":
                        isGettingCheck=True      
                        break   
                    isObstacle=True 
                    break
                if board[y][xCor] in ("wq","wb") :                       
                    isGettingCheck=True      
                    break              
                xCor-=1 
            if isGettingCheck : return isGettingCheck
            ######################knight position####################
            knightsPos=[(blackKingY-1,blackKingX+2),(blackKingY-1,blackKingX-2),(blackKingY+1,blackKingX+2),(blackKingY+1,blackKingX-2),(blackKingY+2,blackKingX+1),(blackKingY+2,blackKingX-1),(blackKingY-2,blackKingX+1),(blackKingY-2,blackKingX-1)]
            for pos in knightsPos :
                y,x=pos
                if 0<=y<=7 and 0<=x<=7 : 
                    if board[y][x] is not None and board[y][x]=="wkt" :
                         isGettingCheck=True      
                         break                                       
        return isGettingCheck
    def isCheckMate(board,player) :
        whitePiecesPos={}
        blackPiecesPos={}
        i=0
        while i<len(board) :
            j=0
            while j<len(board[i]) :
                if board[i][j] is not None :
                    peice=board[i][j]
                    if peice[0]=='w' : whitePiecesPos[(i,j)]=peice
                    else : blackPiecesPos[(i,j)]=peice      
                j+=1
            i+=1 
        newBoard=copy.deepcopy(board)
        #generate moves for black and check if check still exists if exists then mate
        isCheckMate=True
        if player=="Black" :
            for oldPos,value in blackPiecesPos.items() :
            #############Checks for PAWN############# 
                if value=="bp" :
                    newPos=(oldPos[0]+1,oldPos[1])
                    if 0<=newPos[0]<=7 and 0<=newPos[1]<=7 :
                        if(Pawn.isValidMove(newBoard,oldPos,newPos,"Black",True)) :
                            newBoard[oldPos[0]][oldPos[1]]=None
                            newBoard[newPos[0]][newPos[1]]="bp"
                            if(King.isGettingCheck(newBoard,"Black")==False) :
                                isCheckMate=False
                                break
                            newBoard=copy.deepcopy(board)
                    newPos=(oldPos[0]+1,oldPos[1]+1)
                    if 0<=newPos[0]<=7 and 0<=newPos[1]<=7 :
                        if(Pawn.isValidMove(newBoard,oldPos,newPos,"Black",True)) :
                            newBoard[oldPos[0]][oldPos[1]]=None
                            newBoard[newPos[0]][newPos[1]]="bp"   
                            if(King.isGettingCheck(newBoard,"Black")==False) :
                                isCheckMate=False
                                break
                            newBoard=copy.deepcopy(board)
                    newPos=(oldPos[0]+1,oldPos[1]-1)
                    if 0<=newPos[0]<=7 and 0<=newPos[1]<=7 :
                        if(Pawn.isValidMove(newBoard,oldPos,newPos,"Black",True)) :
                            newBoard[oldPos[0]][oldPos[1]]=None
                            newBoard[newPos[0]][newPos[1]]="bp"   
                            if(King.isGettingCheck(newBoard,"Black")==False) :
                                isCheckMate=False
                                break
                            newBoard=copy.deepcopy(board)
            #############Checks for Rook############# 
                if value=="br" : 
                    for y in range(oldPos[0]-1,-1,-1) :
                        newPos=(y,oldPos[1])
                        if Rook.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="br"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    for y in range(oldPos[0]+1,8,1) :
                        newPos=(y,oldPos[1])
                        if Rook.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="br"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    for x in range(oldPos[1]-1,-1,-1) :
                        newPos=(oldPos[0],x)
                        if Rook.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="br"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    for x in range(oldPos[1]+1,8,1) :
                        newPos=(oldPos[0],x)
                        if Rook.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="br"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
            #############Checks for Bishop############# 
                if value=="bb" : 
                    xCor=oldPos[1]+1  
                    for y in range(oldPos[0]-1,-1,-1) :
                        if xCor==8 : break
                        newPos=(y,xCor)
                        if Bishop.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="bb"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False                               
                                break
                             newBoard=copy.deepcopy(board)
                        xCor+=1
                    if isCheckMate==False : break
                    xCor=oldPos[1]-1  
                    for y in range(oldPos[0]-1,-1,-1) :
                        if xCor==-1 : break
                        newPos=(y,xCor)
                        if Bishop.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="bb"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor-=1
                    if isCheckMate==False : break
                    xCor=oldPos[1]-1  
                    for y in range(oldPos[0]+1,8,1) :
                        if xCor==-1 : break
                        newPos=(y,xCor)
                        if Bishop.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="bb"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor-=1
                    if isCheckMate==False : break
                    xCor=oldPos[1]+1  
                    for y in range(oldPos[0]+1,8,1) :
                        if xCor==8 : break
                        newPos=(y,xCor)
                        if Bishop.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="bb"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor+=1
                    if isCheckMate==False : break
            #############Checks for Queen############# 
                if value=="bq" : 
                    for y in range(oldPos[0]-1,-1,-1) :
                        newPos=(y,oldPos[1])
                        if Queen.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="bq"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    for y in range(oldPos[0]+1,8,1) :
                        newPos=(y,oldPos[1])                        
                        if Queen.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="bq"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    for x in range(oldPos[1]-1,-1,-1) :
                        newPos=(oldPos[0],x)                         
                        if Queen.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="bq"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    for x in range(oldPos[1]+1,8,1) :
                        newPos=(oldPos[0],x)
                        if Queen.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="bq"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    xCor=oldPos[1]+1  
                    for y in range(oldPos[0]-1,-1,-1) :
                        if xCor==8 : break
                        newPos=(y,xCor)
                        if Queen.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="bq"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor+=1
                    if isCheckMate==False : break
                    xCor=oldPos[1]-1  
                    for y in range(oldPos[0]-1,-1,-1) :
                        if xCor==-1 : break
                        newPos=(y,xCor)
                        if Queen.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="bq"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor-=1
                    if isCheckMate==False : break
                    xCor=oldPos[1]-1  
                    for y in range(oldPos[0]+1,8,1) :
                        if xCor==-1 : break
                        newPos=(y,xCor)
                        if Queen.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="bq"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor-=1
                    if isCheckMate==False : break
                    xCor=oldPos[1]+1  
                    for y in range(oldPos[0]+1,8,1) :
                        if xCor==8 : break
                        newPos=(y,xCor)
                        if Queen.isValidMove(board,oldPos,newPos,"Black") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="bq"
                             if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor+=1
                    if isCheckMate==False : break
            #############Checks for Knight############# 
                if value=="bkt" : 
                    knightsPos=[(oldPos[0]-1,oldPos[1]+2),(oldPos[0]-1,oldPos[1]-2),(oldPos[0]+1,oldPos[1]+2),(oldPos[0]+1,oldPos[1]-2),(oldPos[0]+2,oldPos[1]+1),(oldPos[0]+2,oldPos[1]-1),(oldPos[0]-2,oldPos[1]+1),(oldPos[0]-2,oldPos[1]-1)]
                    for newPos in knightsPos :
                        if not (0<=newPos[0]<=7 and 0<=newPos[1]<=7)  : continue
                        if Knight.isValidMove(board,oldPos,newPos,"Black") :
                            newBoard[oldPos[0]][oldPos[1]]=None
                            newBoard[newPos[0]][newPos[1]]="bkt"
                            if King.isGettingCheck(newBoard,"Black")==False :
                               isCheckMate=False
                               break
                        newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
            #############Checks for King############# 
                if value=="bk" :
                    kingPos=[(oldPos[0],oldPos[1]+1),(oldPos[0],oldPos[1]-1),(oldPos[0]-1,oldPos[1]),(oldPos[0]+1,oldPos[1]),(oldPos[0]+1,oldPos[1]+1),(oldPos[0]-1,oldPos[1]-1),(oldPos[0]-1,oldPos[1]+1),(oldPos[0]+1,oldPos[1]-1)]
                    for newPos in kingPos :
                        if not (0<=newPos[0]<=7 and 0<=newPos[1]<=7) : continue
                        if King.isValidMove(board,oldPos,newPos,"Black") :
                            newBoard[oldPos[0]][oldPos[1]]=None
                            newBoard[newPos[0]][newPos[1]]="bk"
                            if King.isGettingCheck(newBoard,"Black")==False :
                                isCheckMate=False
                                break
                        newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
        elif player=="White" :
            for oldPos,value in whitePiecesPos.items() :
            #############Checks for PAWN############# 
                if value=="wp" :
                    newPos=(oldPos[0]+1,oldPos[1])
                    if 0<=newPos[0]<=7 and 0<=newPos[1]<=7 :
                        if(Pawn.isValidMove(newBoard,oldPos,newPos,"White",True)) :
                            newBoard[oldPos[0]][oldPos[1]]=None
                            newBoard[newPos[0]][newPos[1]]="wp"
                            if(King.isGettingCheck(newBoard,"White")==False) :
                                isCheckMate=False
                                break
                            newBoard=copy.deepcopy(board)
                    newPos=(oldPos[0]+1,oldPos[1]+1)
                    if 0<=newPos[0]<=7 and 0<=newPos[1]<=7 :
                        if(Pawn.isValidMove(newBoard,oldPos,newPos,"White",True)) :
                            newBoard[oldPos[0]][oldPos[1]]=None
                            newBoard[newPos[0]][newPos[1]]="wp"   
                            if(King.isGettingCheck(newBoard,"White")==False) :
                                isCheckMate=False
                                break
                            newBoard=copy.deepcopy(board)
                    newPos=(oldPos[0]+1,oldPos[1]-1)
                    if 0<=newPos[0]<=7 and 0<=newPos[1]<=7 :
                        if(Pawn.isValidMove(newBoard,oldPos,newPos,"White",True)) :
                            newBoard[oldPos[0]][oldPos[1]]=None
                            newBoard[newPos[0]][newPos[1]]="wp"   
                            if(King.isGettingCheck(newBoard,"White")==False) :
                                isCheckMate=False
                                break
                            newBoard=copy.deepcopy(board)
            #############Checks for Rook############# 
                if value=="wr" : 
                    for y in range(oldPos[0]-1,-1,-1) :
                        newPos=(y,oldPos[1])
                        if Rook.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wr"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    for y in range(oldPos[0]+1,8,1) :
                        newPos=(y,oldPos[1])
                        if Rook.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wr"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    for x in range(oldPos[1]-1,-1,-1) :
                        newPos=(oldPos[0],x)
                        if Rook.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wr"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    for x in range(oldPos[1]+1,8,1) :
                        newPos=(oldPos[0],x)
                        if Rook.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wr"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
            #############Checks for Bishop############# 
                if value=="wb" : 
                    xCor=oldPos[1]+1  
                    for y in range(oldPos[0]-1,-1,-1) :
                        if xCor==8 : break
                        newPos=(y,xCor)
                        if Bishop.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wb"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False                               
                                break
                             newBoard=copy.deepcopy(board)
                        xCor+=1
                    if isCheckMate==False : break
                    xCor=oldPos[1]-1  
                    for y in range(oldPos[0]-1,-1,-1) :
                        if xCor==-1 : break
                        newPos=(y,xCor)
                        if Bishop.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wb"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor-=1
                    if isCheckMate==False : break
                    xCor=oldPos[1]-1  
                    for y in range(oldPos[0]+1,8,1) :
                        if xCor==-1 : break
                        newPos=(y,xCor)
                        if Bishop.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wb"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor-=1
                    if isCheckMate==False : break
                    xCor=oldPos[1]+1  
                    for y in range(oldPos[0]+1,8,1) :
                        if xCor==8 : break
                        newPos=(y,xCor)
                        if Bishop.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wb"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor+=1
                    if isCheckMate==False : break
            #############Checks for Queen############# 
                if value=="wq" : 
                    for y in range(oldPos[0]-1,-1,-1) :
                        newPos=(y,oldPos[1])
                        if Queen.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wq"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    for y in range(oldPos[0]+1,8,1) :
                        newPos=(y,oldPos[1])                        
                        if Queen.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wq"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    for x in range(oldPos[1]-1,-1,-1) :
                        newPos=(oldPos[0],x)                         
                        if Queen.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wq"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    for x in range(oldPos[1]+1,8,1) :
                        newPos=(oldPos[0],x)
                        if Queen.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wq"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                    xCor=oldPos[1]+1  
                    for y in range(oldPos[0]-1,-1,-1) :
                        if xCor==8 : break
                        newPos=(y,xCor)
                        if Queen.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wq"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor+=1
                    if isCheckMate==False : break
                    xCor=oldPos[1]-1  
                    for y in range(oldPos[0]-1,-1,-1) :
                        if xCor==-1 : break
                        newPos=(y,xCor)
                        if Queen.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wq"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor-=1
                    if isCheckMate==False : break
                    xCor=oldPos[1]-1  
                    for y in range(oldPos[0]+1,8,1) :
                        if xCor==-1 : break
                        newPos=(y,xCor)
                        if Queen.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wq"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor-=1
                    if isCheckMate==False : break
                    xCor=oldPos[1]+1  
                    for y in range(oldPos[0]+1,8,1) :
                        if xCor==8 : break
                        newPos=(y,xCor)
                        if Queen.isValidMove(board,oldPos,newPos,"White") :
                             newBoard[oldPos[0]][oldPos[1]]=None
                             newBoard[newPos[0]][newPos[1]]="wq"
                             if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                             newBoard=copy.deepcopy(board)
                        xCor+=1
                    if isCheckMate==False : break
            #############Checks for Knight############# 
                if value=="wkt" : 
                    knightsPos=[(oldPos[0]-1,oldPos[1]+2),(oldPos[0]-1,oldPos[1]-2),(oldPos[0]+1,oldPos[1]+2),(oldPos[0]+1,oldPos[1]-2),(oldPos[0]+2,oldPos[1]+1),(oldPos[0]+2,oldPos[1]-1),(oldPos[0]-2,oldPos[1]+1),(oldPos[0]-2,oldPos[1]-1)]
                    for newPos in knightsPos :
                        if not (0<=newPos[0]<=7 and 0<=newPos[1]<=7) : continue
                        if Knight.isValidMove(board,oldPos,newPos,"White") :
                            newBoard[oldPos[0]][oldPos[1]]=None
                            newBoard[newPos[0]][newPos[1]]="wkt"
                            if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                        newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
                ##############checks for king################ 
                if value=="wk" :
                    kingPos=[(oldPos[0],oldPos[1]+1),(oldPos[0],oldPos[1]-1),(oldPos[0]-1,oldPos[1]),(oldPos[0]+1,oldPos[1]),(oldPos[0]+1,oldPos[1]+1),(oldPos[0]-1,oldPos[1]-1),(oldPos[0]-1,oldPos[1]+1),(oldPos[0]+1,oldPos[1]-1)]
                    for newPos in kingPos :
                        if not (0<=newPos[0]<=7 and 0<=newPos[1]<=7) : continue
                        if King.isValidMove(board,oldPos,newPos,"White") :
                            newBoard[oldPos[0]][oldPos[1]]=None
                            newBoard[newPos[0]][newPos[1]]="wk"
                            if King.isGettingCheck(newBoard,"White")==False :
                                isCheckMate=False
                                break
                        newBoard=copy.deepcopy(board)
                    if isCheckMate==False : break
        return isCheckMate
     
class Queen :
    def isValidMove(board,currPos,newPos,player) :
        currY=currPos[0]
        currX=currPos[1]     
        newY=newPos[0]
        newX=newPos[1]
        peice=board[currY][currX]
        if peice=="bq" and player=="White"  :return False
        if peice=="wq" and player=="Black"  :return False
        if (abs(currY-newY)==1 and abs(newX-currX)==2) or (abs(currY-newY)==2 and (abs(newX-currX))==1) : return False
        elif abs(newX-currX)==0 or abs(newY-currY)==0 :
            if peice=="bq" :
                if board[newY][newX]!=None and board[newY][newX][0]=="b" : return False
                if newY<currY :
                    obstacle=False
                    for i in range(currY-1,newY,-1) :
                        if board[i][currX]!=None :  
                            obstacle=True
                            break   
                    return not obstacle                       
                if newY>currY : 
                    obstacle=False
                    for i in range(currY+1,newY) :
                        if board[i][currX]!=None :  
                            obstacle=True
                            break   
                    return not obstacle                          
                if newX>currX :
                    obstacle=False
                    for i in range(currX+1,newX) :
                        if board[currY][i]!=None :  
                            obstacle=True
                            break   
                    return not obstacle                          
                if newX<currX :
                    obstacle=False
                    for i in range(currX-1,newX,-1) :
                        if board[currY][i]!=None :  
                            obstacle=True
                            break   
                    return not obstacle                          
            if peice=="wq" :   
                if board[newY][newX]!=None and board[newY][newX][0]=="w" : return False
                if newY>currY :
                    obstacle=False
                    for i in range(currY+1,newY) :
                        if board[i][currX]!=None :  
                            obstacle=True
                            break   
                    return not obstacle                       
                if newY<currY : 
                    obstacle=False
                    for i in range(currY-1,newY,-1) :
                        if board[i][currX]!=None :  
                            obstacle=True
                            break   
                    return not obstacle                          
                if newX>currX :
                    obstacle=False
                    for i in range(currX+1,newX) :
                        if board[currY][i]!=None :  
                            obstacle=True
                            break   
                    return not obstacle                          
                if newX<currX :
                    obstacle=False
                    for i in range(currX-1,newX,-1) :
                        if board[currY][i]!=None :  
                            obstacle=True
                            break   
                    return not obstacle                          
        elif abs(newX-currX)==abs(currY-newY) :
            if peice=="bq" :
                if board[newY][newX]!=None and board[newY][newX][0]=="b" : return False  
                if newX<currX and newY<currY:
                    obstacle=False
                    j=currY-1
                    for i in range(currX-1,newX,-1) :
                        if board[j][i]!=None :  
                            obstacle=True
                            break   
                        j-=1
                    return not obstacle                        
                elif newX>currX and newY>currY : 
                    obstacle=False
                    j=currY+1
                    for i in range(currX+1,newX) :
                        if board[j][i]!=None : 
                            obstacle=True
                            break   
                        j+=1
                    return not obstacle                                             
                elif newX>currX and newY<currY : 
                    obstacle=False
                    j=currY-1
                    for i in range(currX+1,newX) :
                        if board[j][i]!=None : 
                            obstacle=True
                            break   
                        j-=1
                    return not obstacle                        
                elif newX<currX and newY>currY : 
                    obstacle=False
                    j=currY+1
                    for i in range(currX-1,newX,-1) :
                        if board[j][i]!=None : 
                            obstacle=True
                            break   
                        j+=1
                    return not obstacle                        
            if peice=="wq" : 
                if board[newY][newX]!=None and board[newY][newX][0]=="w" : return False
                if newX>currX and newY>currY : 
                    obstacle=False
                    j=currY+1            
                    for i in range(currX+1,newX) :
                        if board[j][i]!=None : 
                            obstacle=True
                            break   
                        j+=1
                    return not obstacle                        
                if newX<currX and newY>currY : 
                    obstacle=False
                    j=currY+1            
                    for i in range(currX-1,newX,-1) :
                        if board[j][i]!=None : 
                            obstacle=True
                            break   
                        j+=1
                    return not obstacle                        
                if newX<currX and newY<currY : 
                    obstacle=False
                    j=currY-1            
                    for i in range(currX-1,newX,-1) :
                        if board[j][i]!=None : 
                            obstacle=True
                            break   
                        j-=1
                    return not obstacle                        
                if newX>currX and newY<currY : 
                    obstacle=False
                    j=currY-1            
                    for i in range(currX+1,newX) :
                        if board[j][i]!=None : 
                            obstacle=True
                            break   
                        j-=1
                    return not obstacle                                 
        else : return False        
class Rook :
    def isValidMove(board,currPos,newPos,player) :
        currY=currPos[0]
        currX=currPos[1]     
        newY=newPos[0]
        newX=newPos[1]
        peice=board[currY][currX]
        if peice=="br" and player=="White"  :return False
        if peice=="wr" and player=="Black"  :return False
        if abs(newX-currX)!=0 and abs(newY-currY)!=0 : 
            return False
        if peice=="br" :   
            if board[newY][newX]!=None and board[newY][newX][0]=="b" : return False
            if newY<currY :
                obstacle=False
                for i in range(currY-1,newY,-1) :
                    if board[i][currX]!=None :  
                        obstacle=True
                        break   
                return not obstacle                       
            if newY>currY : 
                obstacle=False
                for i in range(currY+1,newY) :
                    if board[i][currX]!=None :  
                        obstacle=True
                        break   
                return not obstacle                          
            if newX>currX :
                obstacle=False
                for i in range(currX+1,newX) :
                    if board[currY][i]!=None :  
                        obstacle=True
                        break   
                return not obstacle                          
            if newX<currX :
                obstacle=False
                for i in range(currX-1,newX,-1) :
                    if board[currY][i]!=None :  
                        obstacle=True
                        break   
                return not obstacle                          
        if peice=="wr" :   
            if board[newY][newX]!=None and board[newY][newX][0]=="w" : return False
            if newY>currY :
                obstacle=False
                for i in range(currY+1,newY) :
                    if board[i][currX]!=None :  
                        obstacle=True
                        break   
                return not obstacle                       
            if newY<currY : 
                obstacle=False
                for i in range(currY-1,newY,-1) :
                    if board[i][currX]!=None :  
                        obstacle=True
                        break   
                return not obstacle                          
            if newX>currX :
                obstacle=False
                for i in range(currX+1,newX) :
                    if board[currY][i]!=None :  
                        obstacle=True
                        break   
                return not obstacle                          
            if newX<currX :
                obstacle=False
                for i in range(currX-1,newX,-1) :
                    if board[currY][i]!=None :  
                        obstacle=True
                        break   
                return not obstacle                                    
class Bishop :
    def isValidMove(board,currPos,newPos,player) :
        currY=currPos[0]
        currX=currPos[1]     
        newY=newPos[0]
        newX=newPos[1]
        peice=board[currY][currX]
        if peice=="bb" and player=="White"  :return False
        if peice=="wb" and player=="Black"  :return False
        if abs(newX-currX)!=abs(currY-newY) :
            return False 
        if peice=="bb" :
            if board[newY][newX]!=None and board[newY][newX][0]=="b" : return False  
            if newX<currX and newY<currY:
                obstacle=False
                j=currY-1
                for i in range(currX-1,newX,-1) :
                    if board[j][i]!=None :  
                        obstacle=True
                        break   
                    j-=1
                return not obstacle                        
            elif newX>currX and newY>currY : 
                obstacle=False
                j=currY+1
                for i in range(currX+1,newX) :
                    if board[j][i]!=None : 
                        obstacle=True
                        break   
                    j+=1
                return not obstacle                                             
            elif newX>currX and newY<currY : 
                obstacle=False
                j=currY-1
                for i in range(currX+1,newX) :
                    if board[j][i]!=None : 
                        obstacle=True
                        break   
                    j-=1
                return not obstacle                        
            elif newX<currX and newY>currY : 
                obstacle=False
                j=currY+1
                for i in range(currX-1,newX,-1) :
                    if board[j][i]!=None : 
                        obstacle=True
                        break   
                    j+=1
                return not obstacle                        
        if peice=="wb" : 
            if board[newY][newX]!=None and board[newY][newX][0]=="w" : return False
            if newX>currX and newY>currY : 
                obstacle=False
                j=currY+1            
                for i in range(currX+1,newX) :
                    if board[j][i]!=None : 
                        obstacle=True
                        break   
                    j+=1
                return not obstacle                        
            if newX<currX and newY>currY : 
                obstacle=False
                j=currY+1            
                for i in range(currX-1,newX,-1) :
                    if board[j][i]!=None : 
                        obstacle=True
                        break   
                    j+=1
                return not obstacle                        
            if newX<currX and newY<currY : 
                obstacle=False
                j=currY-1            
                for i in range(currX-1,newX,-1) :
                    if board[j][i]!=None : 
                        obstacle=True
                        break   
                    j-=1
                return not obstacle                        
            if newX>currX and newY<currY : 
                obstacle=False
                j=currY-1            
                for i in range(currX+1,newX) :
                    if board[j][i]!=None : 
                        obstacle=True
                        break   
                    j-=1
                return not obstacle                                                                     
class Knight :
    def isValidMove(board,currPos,newPos,player) :
        currY=currPos[0]
        currX=currPos[1]     
        newY=newPos[0]
        newX=newPos[1]
        peice=board[currY][currX]
        if peice=="bkt" and player=="White"  :return False
        if peice=="wkt" and player=="Black"  :return False
        if board[currY][currY]=="bkt" :
            if (abs(currY-newY)==1 and abs(newX-currX)==2) or (abs(currY-newY)==2 and (abs(newX-currX))==1) :
                if board[newY][newX] is not None and board[newY][newX][0]=="b" : return False
                return True
            else :return False 
        else :
            if (abs(currY-newY)==1 and abs(newX-currX)==2) or (abs(currY-newY)==2 and (abs(newX-currX))==1) :
                if board[newY][newX] is not None and board[newY][newX][0]=="w" : return False
                return True
            else :return False 
class Pawn :
    def isValidMove(board,currPos,newPos,player,flag=False) :
        currY=currPos[0]
        currX=currPos[1]     
        newY=newPos[0]
        newX=newPos[1]
        peice=board[currY][currX]
        if peice=="bp" and player=="White"  :return False
        if peice=="wp" and player=="Black"  :return False
        if player=="Black" :
            if peice=="bp" and board[newY][newX]==None:
                if (currY-newY) == 1 and (newX==currX): return True
                return False
            if peice=="bp" and board[newY][newX][0]=="w":
                if abs(currX-newX)==1 and (currY-newY)==1 : return True
            if peice=="bp" : return False                          
            if peice=="wp" and board[newY][newX]==None:
                if (newY-currY) == 1 and (newX==currX): return True
                return False
            if peice=="wp" and board[newY][newX][0]=="b":
                if abs(currX-newX)==1 and (newY-currY)==1 : return True
            if peice=="wp" : return False                          
        if player=="White" :
            if peice=="bp" and board[newY][newX]==None:
                if (newY-currY) == 1 and (newX==currX): return True
                return False
            if peice=="bp" and board[newY][newX][0]=="w":
                if abs(newX-currX)==1 and (newY-currY)==1 : return True
            if peice=="bp" : return False                          
            if peice=="wp" and board[newY][newX]==None:
                if (currY-newY) == 1 and (newX==currX): return True
                return False
            if peice=="wp" and board[newY][newX][0]=="b":
                if abs(newX-currX)==1 and (currY-newY)==1 : return True
            if peice=="wp" : return False                          