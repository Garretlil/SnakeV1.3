
from tkinter import*
import random
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
    def __init__(self):        
        pass

    def PaintForm(self):
        window_width = 1000
        window_length = 800
        ob= Tk()
        self.canvas = Canvas(ob,width = window_width,height = window_length)
        ob.title('Snake')
        self.canvas.pack()
        ob.update()
        return  ob
    def GetRect(self,point_,sizeCell):# вынести в рисование
        r=Rect()
        r.X0=(point_.Column+2)*sizeCell
        r.Y0=(point_.Row+2)*sizeCell
        r.X1=r.X0+sizeCell
        r.Y1=r.Y0+sizeCell
        return r

    def PaintRectange(self,X0,Y0,X1,Y1,Color):
        self.canvas.create_rectangle(X0,Y0,X1,Y1,fill=Color)

class Goal:
     def __init__(self):
         #self.CellsGoal=[]
         self.Color="Orange"
         self.Column=random.randint(0,10)
         self.Row=random.randint(0,10)
         
     def PaintGoal(self):
          paint_.PaintRectange(paint_.GetRect(goal,setka.sizeCell).X0,
                               paint_.GetRect(goal,setka.sizeCell).Y0,
                               paint_.GetRect(goal,setka.sizeCell).X1,
                               paint_.GetRect(goal,setka.sizeCell).Y1,self.Color)

class Setka:

    def __init__(self,dimesionSetka_,size_):
        self.CellsSetka=[]
        self.Color="Blue"
        self.dimesionSetka=dimesionSetka_
        self.size=size_
        self.sizeCell=self.size//self.dimesionSetka
        
        for i in range(self.dimesionSetka):
          for k in range(self.dimesionSetka):
             self.CellsSetka.append(Point(i,k))
     

    def FindPointOfColumnRow(self,Column_,Row_):
       return self.CellsSetka[Column_,Row_]

    def PaintSetka(self):
        for point_ in self.CellsSetka:  
             paint_.PaintRectange(paint_.GetRect(point_,self.sizeCell).X0,
                                  paint_.GetRect(point_,self.sizeCell).Y0,
                                  paint_.GetRect(point_,self.sizeCell).X1,
                                  paint_.GetRect(point_,self.sizeCell).Y1,self.Color)

class Snake:   
      def __init__(self,dimesionSnake_):
        
        self.CellsSnake=[]
        self.Color="White"
        self.dimesionSnake=dimesionSnake_

      def SetPoinsForSnake(self):
          p=5
      def PaintSnake(self):
           for point_ in self.CellsSnake:
               paint_.PaintRectange(paint_.GetRect(point_,setka.sizeCell).X0,
                                    paint_.GetRect(point_,setka.sizeCell).Y0,
                                    paint_.GetRect(point_,setka.sizeCell).X1,
                                    paint_.GetRect(point_,setka.sizeCell).Y1,self.Color)

paint_=Paint()
ob=paint_.PaintForm()
setka=Setka(10,500)
setka.PaintSetka()
SNAKE=Snake(5)
SNAKE.CellsSnake.append(Point(0,0))
SNAKE.CellsSnake.append(Point(1,0))
SNAKE.CellsSnake.append(Point(2,0))
goal=Goal()
SNAKE.PaintSnake()
goal.PaintGoal()
ob.mainloop()

