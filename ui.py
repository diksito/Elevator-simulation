from Tkinter import *
from turtle import *
import tkMessageBox

# elevator 1
elevator = Turtle()
elevator.hideturtle()

# elevator 2
secondElevator = Turtle()
secondElevator.hideturtle()
secondElevator.color('blue')

# elevator 3
thirdElevator = Turtle()
thirdElevator.hideturtle()

building = Turtle()
building.ht()

f = Turtle()
f.color('blue')
f.ht()

def drawBuilding(objectName,x,y):
	objectName.ht()
	objectName.clear()	
	x = x / 2
	y = y / 2
	objectName.speed('fastest')
	objectName.clear()
	objectName.setpos(-x,0)
	objectName.clear()
	objectName.goto(-x,-y)
	objectName.goto(x,-y)
	objectName.goto(x,y)
	objectName.goto(-x,y)
	objectName.goto(-x,0)

def drawFloor(objectName):
	objectName.clear()
	objectName.setpos(-120,-160)
	objectName.clear()
	objectName.begin_fill()
	objectName.goto(-40,-160)
	objectName.goto(-40,-150)
	objectName.goto(-120,-150)
	objectName.goto(-120,-160)
	objectName.end_fill()

def elevator():
    """ Display the Entry text value. """

    global entryWidget
    global entryWidget2
    global entryWidget3
    #if entryWidget.get().strip() == "":
        #tkMessageBox.showerror("Tkinter Entry Widget", "Enter a text value")
    #else:
        #tkMessageBox.showinfo("Tkinter Entry Widget", "Text value =" + entryWidget.get().strip())
        #elevator.circle(int(entryWidget.get()))
    if entryWidget.get().strip() != "" and entryWidget2.get().strip() != "" and entryWidget3.get().strip() != "":
        drawBuilding(building,240, 320)
        drawFloor(f)
    elif (entryWidget.get().strip() != "" and entryWidget2.get().strip() != "") or (entryWidget.get().strip() != "" and entryWidget3.get().strip() != "") or (entryWidget2.get().strip() != "" and entryWidget3.get().strip() != ""):
        drawBuilding(building,200, 280)
        drawFloor(f) 
    elif entryWidget.get().strip() != "" or entryWidget2.get().strip() != "" or entryWidget3.get().strip() != "":
        drawBuilding(building,100, 140)
        drawFloor(f)

        
if __name__ == "__main__":

    root = Tk()
    
    root.title("Elevator v1.0")
    root["padx"] = 100
    root["pady"] = 40
    root.maxsize(400, 180) # maximum size of the window
    

   # call Elevator 1
    # Create a text frame to hold the text Label and the Entry widget
    textFrame = Frame(root)
    
    #Create a Label in textFrame
    entryLabel = Label(textFrame)
    entryLabel["text"] = "Elevator 1:"
    entryLabel.pack(side='left')
    
    # Create an Entry Widget in textFrame
    entryWidget = Entry(textFrame)
    entryWidget["width"] = 10
    entryWidget.pack(side='left')



  # Create a Button
    button = Button(root, text="Call", command=elevator)
    button.pack(after=entryWidget)
    textFrame.pack()

    # call Elevator 2
    # Create a text frame to hold the text Label and the Entry widget
    textFrame2 = Frame(root)
    #Create a Label in textFrame
    entryLabel2 = Label(textFrame2)
    entryLabel2["text"] = "Elevator 2:"
    entryLabel2.pack(side='left')
    # Create an Entry Widget in textFrame
    entryWidget2 = Entry(textFrame2)
    entryWidget2["width"] = 10
    entryWidget2.pack(side='left')

    textFrame2.pack(after=textFrame)
    # Create button for calling Elevator 2s
    button2 = Button(root, text="Call", command=elevator)
    button2.pack(after=entryWidget2)

    # call Elevator 3
    # Create a text frame to hold the text Label and the Entry widget
    textFrame3 = Frame(root)
    #Create a Label in textFrame3
    entryLabel3 = Label(textFrame3)
    entryLabel3["text"] = "Elevator 3:"
    entryLabel3.pack(side='left')
    # Create an Entry Widget in textFrame3
    entryWidget3 = Entry(textFrame3)
    entryWidget3["width"] = 10
    entryWidget3.pack(side='left')

    textFrame3.pack(after=textFrame2)
    # Create button for calling Elevator 3
    button3 = Button(root, text="Call", command=elevator)
    button3.pack(after=entryWidget3)

    root.mainloop()
