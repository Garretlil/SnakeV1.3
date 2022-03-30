
from tkinter import*
import random

class Options:
     def __init__(self):
        self.dimesionSetka=0
        self.dimesionZmeika=0
        self.size=0
        self.sizeCell=0
        self.witdthform=0
        self.heightform=0
        self.colorsetka=0
        self.colorzmeika=0
        self.colorgoal=0
        self.titleform=0

class Snake:
     def __init__(self,options_):
        self.options=options_  
        self.options.sizeCell=options_.size//options_.dimesionSetka
        self.paint_=Paint(self.options)
        self.setka=Setka(self.paint_,self.options)
        self.setka.PaintSetka()             
        self.zmeika=Zmeika( self.paint_,self.options)
        self.zmeika.PaintSnake()
        self.goal=Goal( self.options.dimesionSetka,self.paint_)
        self.goal.PaintGoal()
        self.paint_.Key("<d>",self.KeyS) 
        self.paint_.PaintForm()
         
     def KeyS(self,event):
        self.goal.GetRandomPoint()
        self.goal.PaintGoal()     
        self.setka.PaintCell(self.goal.oldpoint)   
 

class Point:
     def __init__(self,Column_,Row_):
         self.Column=Column_
         self.Row=Row_  

class Rect:
     def __init__(self):
         self.X0=0
         self.Y0=0 
         self.X1=0
         self.Y1=0

class Paint:
    def __init__(self,options_):   
        self.options=options_     
        self.windows= Tk()
        self.canvas = Canvas(self.windows,width = self.options.witdthform,height = self.options.heightform)
   

    def GetRect(self,point_):# вынести в рисование
        r=Rect()
        r.X0=(point_.Column+2)*self.options.sizeCell
        r.Y0=(point_.Row+2)*self.options.sizeCell
        r.X1=r.X0+self.options.sizeCell
        r.Y1=r.Y0+self.options.sizeCell
        return r

    def Key(self,keyvalue,func):
        self.windows.bind(keyvalue, func) 

    def PaintForm(self):
        self.windows.title(self.options.titleform)
        self.canvas.pack()
        self.windows.mainloop()

    def PaintRectange(self,X0,Y0,X1,Y1,Color):
        self.canvas.create_rectangle(X0,Y0,X1,Y1,fill=Color)

class Goal:
     def __init__(self,dimesionsetka,paint_):
         self.CellsGoal=[]
         self.dimesionSetka=dimesionsetka-1
         self.Col=0
         self.Row=0
         self.GetRandomPoint()
         self.Color="Orange" 
         self.paint=paint_


     def GetRandomPoint(self):
         self.OldCol=self.Col
         self.OldRow=self.Row
         self.oldpoint=Point(self.OldCol,self.OldRow)

         self.Col=random.randint(0,self.dimesionSetka)
         self.Row=random.randint(0,self.dimesionSetka)
         self.CellsGoal.clear()
         newpoint_=Point(self.Col,self.Row)
         self.CellsGoal.append(newpoint_)
         return newpoint_
         
     def PaintGoal(self):
          for point_ in self.CellsGoal:
               self.paint.PaintRectange(self.paint.GetRect(point_).X0,
                                    self.paint.GetRect(point_).Y0,
                                    self.paint.GetRect(point_).X1,
                                    self.paint.GetRect(point_).Y1,self.Color)

class Setka:

    def __init__(self,paint_,options_):
        self.CellsSetka=[]
        self.Color=options_.colorsetka
        self.dimesionSetka=options_.dimesionSetka
        self.size=options_.size
        self.sizeCell=options_.sizeCell
        self.paint=paint_
        
        for i in range(self.dimesionSetka):
          for k in range(self.dimesionSetka):
             self.CellsSetka.append(Point(i,k))
     

    def FindPointOfColumnRow(self,Column_,Row_):
       return self.CellsSetka[Column_,Row_]

    def PaintCell(self,point_):  
             self.paint.PaintRectange(self.paint.GetRect(point_).X0,
                                  self.paint.GetRect(point_).Y0,
                                  self.paint.GetRect(point_).X1,
                                  self.paint.GetRect(point_).Y1,self.Color)

    def PaintSetka(self):
        for point_ in self.CellsSetka:  
             self.paint.PaintRectange(self.paint.GetRect(point_).X0,
                                  self.paint.GetRect(point_).Y0,
                                  self.paint.GetRect(point_).X1,
                                  self.paint.GetRect(point_).Y1,self.Color)

class Zmeika:   
      def __init__(self,paint_,options_):
        
        self.CellsZmeika=[]
        self.Color=options_.colorzmeika
        self.dimesionSnake=options_.dimesionZmeika
        self.paint=paint_
        self.CellsZmeika.append(Point(0,0))
        self.CellsZmeika.append(Point(1,0))
        self.CellsZmeika.append(Point(2,0))

      def SetPoinsForSnake(self):
          p=5
      def PaintSnake(self):
           for point_ in self.CellsZmeika:
               self.paint.PaintRectange(self.paint.GetRect(point_).X0,
                                    self.paint.GetRect(point_).Y0,
                                    self.paint.GetRect(point_).X1,
                                    self.paint.GetRect(point_).Y1,self.Color)

options=Options()
options.dimesionSetka=50
options.size=300
options.colorsetka="Gray"
options.colorzmeika="Red"
options.dimesionZmeika=5
options.witdthform=600
options.heightform=600
options.titleform="TestSnake"
snake=Snake(options)
 
 



