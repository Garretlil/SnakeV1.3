from tkinter import*
import random
from enum import Enum
import time
from functools import lru_cache

class Directions(Enum):
    Up = 1
    Down = 3
    Left = 4
    Right = 6

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
        self.currentdirection=0

class Snake:
     def __init__(self,options_):
        self.options=options_  
        self.options.sizeCell=options_.size//options_.dimesionSetka
        self.paint_=Paint(self.options)
        self.setka=Setka(self.paint_,self.options)
        self.setka.PaintSetka()             
        self.zmeika=Zmeika( self.paint_,self.options)
        self.zmeika.PaintZmeika()
        self.goal=Goal( self.options.dimesionSetka,self.paint_)
        self.goal.PaintGoal()
        self.paint_.BindKey("<"+Directions.Right.name+">",self.Keys) 
        self.paint_.BindKey("<"+Directions.Left.name+">",self.Keys) 
        self.paint_.BindKey("<"+Directions.Down.name+">",self.Keys) 
        self.paint_.BindKey("<"+Directions.Up.name+">",self.Keys) 
        self.paint_.PaintForm()
     def findDirection(self,event):
         for each in Directions:## вынести в функцию
            if event.keysym==each.name:
                return each
         
     def Keys(self,event):
        #проверка на разворот
        direction=self.findDirection(event)
        if direction.value%2!=options.currentdirection.value%2:                                            ##РАЗКОММЕНТИРОВАТЬ!!!
           self.MoveCicle(direction)
     def MoveCicle(self,direction):
             CellsZmeikaOld=self.zmeika.MoveNext(direction)#return self.CellsZmeikaOld
             self.setka.PaintCells(CellsZmeikaOld)
             self.zmeika.PaintZmeika()
             if CellsZmeikaOld[2].Column==self.goal.Col and  CellsZmeikaOld[2].Row==self.goal.Row:                                            #проверка на поедание яблока
                self.goal.GetRandomPoint()
                self.goal.PaintGoal()
             self.paint_.canvasupdate()
             time.sleep(0.05)
             #доделать
             self.MoveCicle(direction)       #self.paint_.mainwindow.after(500,
#self.goal.GetRandomPoint()
#self.goal.PaintGoal()     
#self.setka.PaintCell(self.goal.oldpoint)   
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
        self.mainwindow= Tk()
        self.canvas = Canvas(self.mainwindow,width = self.options.witdthform,height = self.options.heightform)
    def canvasupdate(self):
        self.canvas.update()
   

    def GetRect(self,point_):# вынести в рисование
        r=Rect()
        r.X0=(point_.Column+2)*self.options.sizeCell
        r.Y0=(point_.Row+2)*self.options.sizeCell
        r.X1=r.X0+self.options.sizeCell
        r.Y1=r.Y0+self.options.sizeCell
        return r

    def BindKey(self,keyvalue,func):
        self.mainwindow.bind(keyvalue, func) 

    def PaintForm(self):
        self.mainwindow.title(self.options.titleform)
        self.canvas.pack()
        self.mainwindow.mainloop()

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

    def PaintCells(self,points_):
        for point_ in points_:  
             self.PaintCell(point_)

    def PaintSetka(self):
        for point_ in self.CellsSetka:  
             self.paint.PaintRectange(self.paint.GetRect(point_).X0,
                                  self.paint.GetRect(point_).Y0,
                                  self.paint.GetRect(point_).X1,
                                  self.paint.GetRect(point_).Y1,self.Color)

class Zmeika:   
      def coping(self):
          self.CellsZmeikaOld=[]
          for i in self.CellsZmeika:
              self.CellsZmeikaOld.append(i)
          return self.CellsZmeikaOld

      def __init__(self,paint_,options_):
        
        self.CellsZmeika=[]
        self.CellsZmeikaOld=[]
        self.Color=options_.colorzmeika
        self.dimesionSnake=options_.dimesionZmeika
        self.paint=paint_
        # начальное положение
        self.CellsZmeika.append(Point(0,0))
        self.CellsZmeika.append(Point(1,0))
        self.CellsZmeika.append(Point(2,0))

      def MoveNext(self,direction_):
          self.direction=direction_
          self.CellsZmeikaOld=[]
          options.currentdirection=direction_
          
          for i in self.CellsZmeika:
              self.CellsZmeikaOld.append(i)#копируем старую модель змейки
          self.CellsZmeika=[]#создаем хранилище для новой модели змейки
          self.count=len(self.CellsZmeikaOld)#  длина змейки
          self.previousCell=self.CellsZmeikaOld[self.count-1]# голова змейки
          


          if self.direction==Directions.Down: 
              if self.previousCell.Row==options.dimesionSetka -1:
                 self.CellsZmeika.append(Point(self.previousCell.Column,
                                               0))   
              else:
                   self.CellsZmeika.append(Point(self.previousCell.Column,
                                               self.previousCell.Row+1))# смещаем голову змейки 
              for i in range(self.count-2,-1,-1):
                  point_=(Point(self.previousCell.Column,
                                self.previousCell.Row))
                  self.CellsZmeika.append(point_)
                  self.previousCell=self.CellsZmeikaOld[i]

          if self.direction==Directions.Left:              
              if self.previousCell.Column==0:
                 self.CellsZmeika.append(Point(options.dimesionSetka-1,
                                               self.previousCell.Row)) 
              else:
                  self.CellsZmeika.append(Point(self.previousCell.Column-1,
                                            self.previousCell.Row))
              for i in range(self.count-2,-1,-1):
                  point_=(Point(self.previousCell.Column,
                                self.previousCell.Row))
                  self.CellsZmeika.append(point_)
                  self.previousCell=self.CellsZmeikaOld[i]
          if self.direction==Directions.Right:    
              if self.previousCell.Column==options.dimesionSetka-1:
                 self.CellsZmeika.append(Point(0,
                                               self.previousCell.Row))# смещаем голову змейки 
              else:
                  self.CellsZmeika.append(Point(self.previousCell.Column+1,
                                            self.previousCell.Row))
              for i in range(self.count-2,-1,-1):
                  point_=(Point(self.previousCell.Column,
                                self.previousCell.Row))
                  self.CellsZmeika.append(point_)
                  self.previousCell=self.CellsZmeikaOld[i]

          if self.direction==Directions.Up:
              if self.previousCell.Row==0:
                 self.CellsZmeika.append(Point(self.previousCell.Column,
                                            options.dimesionSetka -1))# смещаем голову змейки    
              else:
                  self.CellsZmeika.append(Point(self.previousCell.Column,
                                            self.previousCell.Row-1))
              for i in range(self.count-2,-1,-1):
                  point_=(Point(self.previousCell.Column,
                                self.previousCell.Row))
                  self.CellsZmeika.append(point_)
                  self.previousCell=self.CellsZmeikaOld[i]
          
          self.CellsZmeika.reverse()
          return self.CellsZmeikaOld
           

      def PaintZmeika(self):
           for point_ in self.CellsZmeika:
               self.paint.PaintRectange(self.paint.GetRect(point_).X0,
                                    self.paint.GetRect(point_).Y0,
                                    self.paint.GetRect(point_).X1,
                                    self.paint.GetRect(point_).Y1,self.Color)

options=Options()
options.dimesionSetka=30
options.size=450
options.colorsetka="Gray"
options.colorzmeika="Red"
options.dimesionZmeika=3
options.witdthform=600
options.heightform=600
options.titleform="TestSnake"
options.currentdirection=Directions.Right
snake=Snake(options)

 
