
from tkinter import*
import random

class Snake:
     def __init__(self,dimesionSetka_,size_,color_):
        self.dimesionSetka=dimesionSetka_
        self.size=size_
        self.color=color_
        self.sizeCell=self.size//self.dimesionSetka
        self.paint_=Paint(self.sizeCell)
         
     def KeyS(self,event):
        self.goal.GetRandomPoint()
        self.goal.PaintGoal()     
        self.setka.PaintCell(self.goal.oldpoint)
               
     def Go(self):

        self.windows=self.paint_.PaintForm()
        self.setka=Setka(self.dimesionSetka,self.size,self.paint_,self.color,self.sizeCell)
        self.setka.PaintSetka()
       
        
        self.zmeika=Zmeika( self.paint_)
        self.zmeika.CellsSnake.append(Point(0,0))
        self.zmeika.CellsSnake.append(Point(1,0))
        self.zmeika.CellsSnake.append(Point(2,0))
        self.goal=Goal( self.dimesionSetka,self.paint_)
        self.zmeika.PaintSnake()
        self.goal.PaintGoal()
        self.windows.bind("<s>", self.KeyS) 
        self.windows.mainloop()

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
    def __init__(self,sizecell_):        
        self.sizeCell=sizecell_

    def PaintForm(self):
        window_width = 1000
        window_length = 800
        self.windows= Tk()
        self.canvas = Canvas(self.windows,width = window_width,height = window_length)
        self.windows.title('Snake')
        self.canvas.pack()
        self.windows.update()
        return  self.windows

    def Invalidate(self):
        self.canvas.pack()
        self.windows.update()


    def GetRect(self,point_):# вынести в рисование
        r=Rect()
        r.X0=(point_.Column+2)*self.sizeCell
        r.Y0=(point_.Row+2)*self.sizeCell
        r.X1=r.X0+self.sizeCell
        r.Y1=r.Y0+self.sizeCell
        return r

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

    def __init__(self,dimesionSetka_,size_,paint_,color_,sizecell_):
        self.CellsSetka=[]
        self.Color=color_
        self.dimesionSetka=dimesionSetka_
        self.size=size_
        self.sizeCell=sizecell_
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
      def __init__(self,paint_,dimesionSnake_=3):
        
        self.CellsSnake=[]
        self.Color="White"
        self.dimesionSnake=dimesionSnake_
        self.paint=paint_

      def SetPoinsForSnake(self):
          p=5
      def PaintSnake(self):
           for point_ in self.CellsSnake:
               self.paint.PaintRectange(self.paint.GetRect(point_).X0,
                                    self.paint.GetRect(point_).Y0,
                                    self.paint.GetRect(point_).X1,
                                    self.paint.GetRect(point_).Y1,self.Color)

snake=Snake(20,500,"Gray")
snake.Go()
 



