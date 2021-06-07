import tkinter
import tkinter.ttk
import tkinter.font
class TMGrid(tkinter.Canvas) :
    def __init__(self,master,model,w,h) :
        tkinter.Canvas.__init__(self,master,width=w,height=h,highlightbackground="#080808",highlightthickness=1)
        self.width=w
        self.heigth=h
        self.model=model
        self.customEvents={}
        self.customEvents["<RowSelectionChanged>"]=None 
        self.images={} 
        self.selectedRowIndex=-1
        self.update()
        self.bind("<Button-1>",self.gridClicked)
        self.bind("<Key>",self.gridKeyHandler)
    def canvasWidgetClickedHandler(self,row,column) :
        if self.model.editCommand!=None : 
            self.model.editCommand(row,column)   
    def gridKeyHandler(self,event) :
        rows=self.model.getRowCount()
        if event.keysym!="Up" and event.keysym!="Down" : return
        if event.keysym=="Up" : 
            rowIndex=self.selectedRowIndex-1
            if rowIndex==-1 : rowIndex=rows-1
        if event.keysym=="Down" : 
            rowIndex=self.selectedRowIndex+1
            if rowIndex>=rows : rowIndex=0
        oldRowIndex=self.selectedRowIndex
        newRowIndex=rowIndex
        if self.selectedRowIndex!=-1 :
            rectX1=self.x1+1
            rectX2=self.x2-1
            rectY1=self.y1+((self.selectedRowIndex+1)*self.rowHeight)+5      
            rectY2=rectY1+self.rowHeight-5
            self.create_rectangle(rectX1,rectY1,rectX2,rectY2,fill="#303030",width=0)
            columns=self.model.getColumnCount()
            x=self.x1+1
            for i in range(columns-1) :
                x+=self.model.getColumnWidth(i)
                self.create_line(x,rectY1,x,rectY2,fill="white") 
                self.create_line(x+1,rectY1,x+1,rectY2,fill="#ADADAD")
            x=self.x1+1
            y=self.y1+((self.selectedRowIndex+1)*self.rowHeight)+1
            dataFont=tkinter.font.Font(family="verdana",size=8)
            for c in range(columns) :
                cellContent=self.model.getValueAt(self.selectedRowIndex,c)
                cellContentType=self.model.getCellType(self.selectedRowIndex,c)
                if cellContentType=="int" :
                    textX=self.model.getColumnWidth(c)-dataFont.measure(text=cellContent)-5
                    textY=self.rowHeight/2-dataFont.metrics('linespace')/2
                    self.create_text(x+textX,y+textY,font=dataFont,text=cellContent,anchor="nw",fill="white")
                elif cellContentType=="str" :
                    textY=self.rowHeight/2-dataFont.metrics('linespace')/2
                    self.create_text(x+5,y+textY,font=dataFont,text=cellContent,anchor="nw",fill="white")
                elif cellContentType=="PhotoImage" :
                    if cellContent not in self.images :
                        img=tkinter.PhotoImage(file=cellContent)
                        self.images[cellContent]=img
                    else : 
                        img=self.images[cellContent]
                    imageWidth=img.width()
                    imageHeight=img.height()
                    cellHeight=self.rowHeight
                    cellWidth=self.model.getColumnWidth(c)                      
                    imageX=int(cellWidth/2)-int(imageWidth/2)
                    imageY=int(cellHeight/2)-int(imageHeight/2)    
                    self.create_image(x+imageX,y+imageY,image=img,anchor="nw")    
                x+=self.model.getColumnWidth(c)
        #higlight the newly selected row
        self.selectedRowIndex=rowIndex
        rectX1=self.x1+1
        rectX2=self.x2-1
        rectY1=self.y1+((rowIndex+1)*self.rowHeight)+5
        rectY2=rectY1+self.rowHeight-5
        self.create_rectangle(rectX1,rectY1,rectX2,rectY2,fill="#90B3CE",width=0)
        columns=self.model.getColumnCount()
        x=self.x1+1
        for i in range(columns-1) :
            x+=self.model.getColumnWidth(i)
            self.create_line(x,rectY1,x,rectY2,fill="white") 
            self.create_line(x+1,rectY1,x+1,rectY2,fill="#ADADAD")
        x=self.x1+1
        y=self.y1+((self.selectedRowIndex+1)*self.rowHeight)+1
        dataFont=tkinter.font.Font(family="verdana",size=8)
        for c in range(columns) :
            cellContent=self.model.getValueAt(self.selectedRowIndex,c)
            cellContentType=self.model.getCellType(self.selectedRowIndex,c)
            if cellContentType=="int" :
                textX=self.model.getColumnWidth(c)-dataFont.measure(text=cellContent)-5
                textY=self.rowHeight/2-dataFont.metrics('linespace')/2
                self.create_text(x+textX,y+textY,font=dataFont,text=cellContent,anchor="nw",fill="white")
            elif cellContentType=="str" :
                textY=self.rowHeight/2-dataFont.metrics('linespace')/2
                self.create_text(x+5,y+textY,font=dataFont,text=cellContent,anchor="nw",fill="black")
            elif cellContentType=="PhotoImage" :
                if cellContent not in self.images :
                    img=tkinter.PhotoImage(file=cellContent)
                    self.images[cellContent]=img
                else : 
                    img=self.images[cellContent]
                imageWidth=img.width()
                imageHeight=img.height()
                cellHeight=self.rowHeight
                cellWidth=self.model.getColumnWidth(c)                      
                imageX=int(cellWidth/2)-int(imageWidth/2)
                imageY=int(cellHeight/2)-int(imageHeight/2)    
                self.create_image(x+imageX,y+imageY,image=img,anchor="nw")    
            x+=self.model.getColumnWidth(c)
        callback=self.customEvents["<RowSelectionChanged>"]
        if callback!=None : callback(oldRowIndex,newRowIndex)            
    def bind(self,event,callback)  :
        if event  in self.customEvents : 
            self.customEvents[event]=callback
        else : super().bind(event,callback)         
    def gridClicked(self,event) :
        self.focus_set()
        x=event.x
        y=event.y
        if not self.inGrid(x,y) : return
        rowIndex=self.getRowClicked(x,y)        
        if rowIndex==-1 : return
        if self.selectedRowIndex==rowIndex : return
        oldRowIndex=self.selectedRowIndex
        newRowIndex=rowIndex
        if self.selectedRowIndex!=-1 :
            rectX1=self.x1+1
            rectX2=self.x2-1
            rectY1=self.y1+((self.selectedRowIndex+1)*self.rowHeight)+5      
            rectY2=rectY1+self.rowHeight-5
            self.create_rectangle(rectX1,rectY1,rectX2,rectY2,fill="#303030",width=0)
            columns=self.model.getColumnCount()
            x=self.x1+1
            for i in range(columns-1) :
                x+=self.model.getColumnWidth(i)
                self.create_line(x,rectY1,x,rectY2,fill="white")
                self.create_line(x+1,rectY1,x+1,rectY2,fill="#ADADAD")
            x=self.x1+1
            y=self.y1+((self.selectedRowIndex+1)*self.rowHeight)+1
            dataFont=tkinter.font.Font(family="verdana",size=8)
            for c in range(columns) :
                cellContent=self.model.getValueAt(self.selectedRowIndex,c)
                cellContentType=self.model.getCellType(self.selectedRowIndex,c)
                if cellContentType=="int" :
                    textX=self.model.getColumnWidth(c)-dataFont.measure(text=cellContent)-5
                    textY=self.rowHeight/2-dataFont.metrics('linespace')/2
                    self.create_text(x+textX,y+textY,font=dataFont,text=cellContent,anchor="nw",fill="white")
                elif cellContentType=="str" :
                    textY=self.rowHeight/2-dataFont.metrics('linespace')/2
                    self.create_text(x+5,y+textY,font=dataFont,text=cellContent,anchor="nw",fill="white")
                elif cellContentType=="PhotoImage" :
                    if cellContent not in self.images :
                        img=tkinter.PhotoImage(file=cellContent)
                        self.images[cellContent]=img
                    else : 
                        img=self.images[cellContent]
                    imageWidth=img.width()
                    imageHeight=img.height()
                    cellHeight=self.rowHeight
                    cellWidth=self.model.getColumnWidth(c)                      
                    imageX=int(cellWidth/2)-int(imageWidth/2)
                    imageY=int(cellHeight/2)-int(imageHeight/2)    
                    self.create_image(x+imageX,y+imageY,image=img,anchor="nw")     
                x+=self.model.getColumnWidth(c)
        #higlight the newly selected row
        self.selectedRowIndex=rowIndex
        rectX1=self.x1+1
        rectX2=self.x2-1
        rectY1=self.y1+((rowIndex+1)*self.rowHeight)+5
        rectY2=rectY1+self.rowHeight-5
        self.create_rectangle(rectX1,rectY1,rectX2,rectY2,fill="#90B3CE",width=0)
        columns=self.model.getColumnCount()
        x=self.x1+1
        for i in range(columns-1) :
            x+=self.model.getColumnWidth(i)
            self.create_line(x,rectY1,x,rectY2,fill="white") 
            self.create_line(x+1,rectY1,x+1,rectY2,fill="#ADADAD")
        x=self.x1+1
        y=self.y1+((self.selectedRowIndex+1)*self.rowHeight)+1
        dataFont=tkinter.font.Font(family="verdana",size=8)
        for c in range(columns) :
            cellContent=self.model.getValueAt(self.selectedRowIndex,c)
            cellContentType=self.model.getCellType(self.selectedRowIndex,c)
            if cellContentType=="int" :
                textX=self.model.getColumnWidth(c)-dataFont.measure(text=cellContent)-5
                textY=self.rowHeight/2-dataFont.metrics('linespace')/2
                self.create_text(x+textX,y+textY,font=dataFont,text=cellContent,anchor="nw",fill="white")
            elif cellContentType=="str" :
                textY=self.rowHeight/2-dataFont.metrics('linespace')/2
                self.create_text(x+5,y+textY,font=dataFont,text=cellContent,anchor="nw",fill="white")
            elif cellContentType=="PhotoImage" :
                if cellContent not in self.images :
                    img=tkinter.PhotoImage(file=cellContent)
                    self.images[cellContent]=img
                else : 
                    img=self.images[cellContent]
                imageWidth=img.width()
                imageHeight=img.height()
                cellHeight=self.rowHeight
                cellWidth=self.model.getColumnWidth(c)                      
                imageX=int(cellWidth/2)-int(imageWidth/2)
                imageY=int(cellHeight/2)-int(imageHeight/2)    
                self.create_image(x+imageX,y+imageY,image=img,anchor="nw")     
            x+=self.model.getColumnWidth(c)
        callback=self.customEvents["<RowSelectionChanged>"]
        if callback!=None : callback(oldRowIndex,newRowIndex)    
    def getRowClicked(self,x,y) :
        row=int((y-self.y1)/self.rowHeight)-1
        if row>=self.model.getRowCount() : return -1
        else :
            return row
    def inGrid(self,x,y) :
        return self.x1<=x<=self.x2 and self.y1<=y<=self.y2  
    def update(self) :
        self.delete('all')
        x1=0
        y1=0
        x2=x1+self.width
        y2=y1+self.heigth
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.create_rectangle(x1,y1,x2,y2,fill="#303030",width=1)        
        left=x1+1
        right=x2-1
        top=y1+1
        rowHeight=30
        self.rowHeight=rowHeight         
        self.create_rectangle(left,top,right,top+rowHeight,fill="black")
        top+=rowHeight
        rows=self.model.getRowCount()            
        for i in range(rows+1) :
            y=top+i*rowHeight
            self.create_line(left,y,right,y,fill="white")
            self.create_line(left,y+1,right,y+1,fill="#adadad")
        columns=self.model.getColumnCount()
        top=y1+1
        bottom=y2-1
        x=left
        for i in range(columns-1) :
            x+=self.model.getColumnWidth(i)
            self.create_line(x,top,x,bottom,fill="white") 
            self.create_line(x+1,top,x+1,bottom,fill="#ADADAD") 
        titleFont=tkinter.font.Font(family="verdana",size=9,weight="bold")
        x=left
        for i in range(columns) :
            self.create_text(x+5,top+15,font=titleFont,fill="white",anchor="nw",text=self.model.getColumnTitle(i))
            x+=self.model.getColumnWidth(i)  
        dataFont=tkinter.font.Font(family="verdana",size=8)
        x=left
        y=y1+1+rowHeight
        for r in range(rows) :
            x=left
            for c in range(columns) :
                cellContent=self.model.getValueAt(r,c)
                cellContentType=self.model.getCellType(r,c)
                if cellContentType=="int" :
                    textX=self.model.getColumnWidth(c)-dataFont.measure(text=cellContent)-5
                    textY=rowHeight/2-dataFont.metrics('linespace')/2
                    self.create_text(x+textX,y+textY,font=dataFont,text=cellContent,anchor="nw")
                elif cellContentType=="str" :
                    textY=rowHeight/2-dataFont.metrics('linespace')/2
                    self.create_text(x+5,y+textY,font=dataFont,text=cellContent,anchor="nw",fill="white")
                elif cellContentType=="PhotoImage" :
                    if cellContent not in self.images :
                        img=tkinter.PhotoImage(file=cellContent)
                        self.images[cellContent]=img
                    else : 
                        img=self.images[cellContent]
                    imageWidth=img.width()
                    imageHeight=img.height()
                    cellHeight=rowHeight
                    cellWidth=self.model.getColumnWidth(c)                     
                    if (r-1)==rowIndex : cellWidth=self.x2-x  
                    imageX=int(cellWidth/2)-int(imageWidth/2)
                    imageY=int(cellHeight/2)-int(imageHeight/2)    
                    self.create_image(x+imageX,y+imageY,image=img,anchor="nw")     
                elif cellContentType=="Button" :
                    cellContent.configure(command=lambda x=r,y=c : self.canvasWidgetClickedHandler(x,y))
                    cellContent.command=lambda x=r,y=c : self.canvasWidgetClickedHandler(x,y)
                    buttonWidth=20
                    buttonHeight=20
                    cellHeight=rowHeight
                    cellWidth=self.model.getColumnWidth(c)                      
                    buttonX=int(cellWidth/2)-int(buttonWidth/2)
                    buttonY=int(cellHeight/2)-int(buttonHeight/2)                      
                    button1_window=self.create_window(x+buttonX,y+buttonY,window=cellContent,anchor="nw") 
                x+=self.model.getColumnWidth(c)
            y+=rowHeight                   

