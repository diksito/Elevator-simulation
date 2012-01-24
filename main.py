from Tkinter import *
from threading import *
import thread
from time import sleep
from math import sin, cos

window = Tk()
window.title("Elevator v: 0.01")
canvas = Canvas(window, width = 400, height = 300)
canvas.pack()

class Elevator() :
    def __init__(self,
                 bname = "default",
                 direction = 'up',
                 fill = 'red',
                 ssize = 1,
                 cx0 = 10,
                 cy0 = 250,
                 cx1 = 60,
                 cy1 = 300,
                 moving = False):
        self.fill = fill
        self.name = bname
        self.size = ssize
        self.i = 0
        self.deltax = 0
        if(direction == 'up'):
            self.deltay = -3
        else:
            self.deltay = 3
        self.cx0 = cx0
        self.cy0 = cy0
        self.cx1 = cx1
        self.cy1 = cy1
        self.moving = moving
        self.destfloor = 10
        self.setsize()
        
        canvas.create_rectangle(self.x0,self.y0,
                           self.x1,self.y1,
                           fill= self.fill,
                           tag = self.name)

        self.t = Thread(None, Elevator.run, None, [self])
        self.t.start()   
    def setsize(self):
        self.x0 = self.cx0 * self.size 
        self.y0 = self.cy0 * self.size 
        self.x1 = self.cx1 * self.size
        self.y1 = self.cy1 * self.size
    def currentFloor(self):
        currentFloor = 11-abs(self.y1/30)
        return currentFloor
    def run(self):
      while self.moving:
        if self.x1 >= 400:
            self.deltax = -self.deltax
        if self.x0 < 0:
            self.deltax = -self.deltax
        if self.y1 > 300:
            self.deltay = -self.deltay
        if self.y0 < 0:
            self.deltay = -self.deltay
        self.x0 += self.deltax
        self.x1 += self.deltax
        self.y0 += self.deltay
        self.y1 += self.deltay

        canvas.scale(self.name, 1, 1, cos(self.i), cos(self.i))    
        canvas.move(self.name, self.deltax, self.deltay)
        sleep(0.30)

        if(self.destfloor == self.currentFloor()):
            self.moving = False
            print self.name + ' stopped'
    def goToFloor(self, floor):
        if(self.moving == False):
            self.moving = True
            self.destfloor = floor
            self.run()
            
class Building():
    def __init__(self):
        self.elevators = [ Elevator('first', 'up', 'red',1),
                           Elevator('second', 'up', 'green',1,70,150,120,200 ),
                           Elevator('third', 'up', 'blue',1,130,200,180,250) ]       
    def elevatorcall(self):
        print "\ncalling elevator to floor {0} ".format(int(entryWidget.get()))
        for e in self.elevators:
            if (not(e.moving) and entryWidget.get().strip() != ""):
                print e.name + ' is moving...'
                f = int(entryWidget.get())
                entryWidget.delete(0,None)
                e.goToFloor(f)

b = Building()

def buttonPressed():
    thread.start_new_thread(b.elevatorcall,())

#### Create input field ####
textFrame = Frame(window)
# Create a Label in textFrame #
entryLabel = Label(textFrame)
entryLabel["text"] = "Floor:"
entryLabel.pack(side='left')    
# Create an Entry Widget in textFrame #
entryWidget = Entry(textFrame,textvariable='15')
entryWidget["width"] = 10
entryWidget.pack(side='left')
# Create a Button #
button = Button(window, text="Call", command=buttonPressed)
button.pack(after=entryWidget)
textFrame.pack()
window.mainloop()
