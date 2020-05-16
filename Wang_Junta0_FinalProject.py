"""
Purpose: Use turtle to create a 2D game
Author: Juntao Wang
Date: December 9, 2017
CS 111-02, Fall 2017
"""
import turtle
import math
import random
import time

def getData(filename):
    """read and store map data

    Parameter
        filename: text file name
        
    Return Value
        Map lists

    """
    wholeMap = []                                       # list for vertical values
    data = open(filename, "r")

    for line in data:
        lineData = line.split(',')
        intList = []                                    # list for horizontal values
        for i in lineData:
            intList.append(int(i))
        wholeMap.append(intList)                        # create a two dimensional data set
    data.close()
    return wholeMap

    # This function is derived from the List homework

def getData2(filename2):
    """read and store item data

    Parameter
        filename: text file name
        
    Return Value
        list of items

    """
    dataList = []
    data = open(filename2, "r")
    
    for line in data:
        lineData = line.strip()
        dataList.append(lineData)
    data.close()
    return dataList

    # This function is derived from the string manipulation homework

def getData3(filename3):
    """read and print user manual

    Parameter
        filename: text file name
        
    Return Value
        None

    """
    data = open(filename3, "r")

    for line in data:
        print(line.strip())                             # print each line of the text
    data.close()
    
    # This function is derived from textbook p.258

def drawSquare(color):
    """draw a square

    Parameter
        color: fill color

    Return Value
        None
        
    """
    tortoise.width(1)
    tortoise.fillcolor(color)
    tortoise.begin_fill()
    tortoise.down()
    for i in range(4):
        tortoise.forward(1)
        tortoise.left(90)
    tortoise.end_fill()
    tortoise.up()

    # This function is derived from group lab 1

def drawTriangle(pos,heading,color):
    """draw a equilateral triangle

    Parameter
        pos: coordinate to start
        heading: direction to start
        color: fill color

    Return Value
        None
        
    """
    tortoise.goto(pos)                                  # pos should be a tuple
    tortoise.setheading(heading)
    tortoise.fillcolor(color)
    tortoise.begin_fill()
    tortoise.down()
    for i in range(3):
        tortoise.forward(2)
        tortoise.left(120)
    tortoise.end_fill()
    tortoise.up()

def drawCircle(pos,heading,color,radius):
    """draw a circle

    Parameter
        pos: coordinate to start
        heading: direction to start
        color: fill color

    Return Value
        None
        
    """
    tortoise.goto(pos)
    tortoise.setheading(heading)
    tortoise.fillcolor(color)
    tortoise.begin_fill()
    tortoise.down()
    tortoise.circle(radius)
    tortoise.end_fill()
    tortoise.up()

    # This function is derived from group lab 3
    
def drawMap():
    """draw empty blocks

    Parameter
        None

    Return Value
        None
        
    """
    tortoise.goto(20.25,-1)
    tortoise.setheading(90)
    tortoise.width(18)                                  # bold black line
    tortoise.down()
    tortoise.forward(22)
    tortoise.up()

    # split screen with a black line
    
    tortoise.width(1)
    for i in range(21):                                 # draw vertical lines
        tortoise.up()
        tortoise.goto(i,0)
        tortoise.setheading(90)
        tortoise.down()
        tortoise.forward(20)
    for j in range(21):                                 # draw horizontal lines
        tortoise.up()
        tortoise.goto(0,j)
        tortoise.setheading(0)
        tortoise.down()
        tortoise.forward(20)

    # draw empty blocks
    
    tortoise.up()
    tortoise.goto(0,0)                                  # start point
    tortoise.setheading(0)
    drawSquare('purple')
    tortoise.goto(19,19)                                # exit
    tortoise.setheading(0)
    drawSquare('green')

    # draw start point and exit

def drawGamepad():
    """draw a gamepad with five buttons

    Parameter
        None

    Return Value
        None
        
    """
    tortoise.width(3)
    drawTriangle((25,2),60,'orange')                    # up
    drawTriangle((25,8),240,'orange')                   # down
    drawTriangle((22+math.sqrt(3),4),90,'orange')       # left
    drawTriangle((28-math.sqrt(3),4),30,'orange')       # right
    drawCircle((25,4.2),0,'red',0.8)                    # search

def drawMiniwindow():
    """draw a window for status

    Parameter
        None

    Return Value
        None
        
    """
    tortoise.goto(21.5,10)
    tortoise.setheading(0)
    tortoise.down()
    tortoise.forward(7.5)
    tortoise.left(90)
    tortoise.forward(9)
    tortoise.left(90)
    tortoise.forward(7.5)
    tortoise.left(90)
    tortoise.forward(9)
    tortoise.up()

    # draw a rectangle above the gamepad

    # this function is basically a drawSquare function

def drawStatus():
    """draw initial status

    Parameter
        None

    Return Value
        None
        
    """
    itemUpdater.hideturtle()
    searchUpdater.hideturtle()
    itemUpdater.up()
    searchUpdater.up()

    # hide turtles
    
    tortoise.goto(25.25,17.6)
    tortoise.write("Player Status", False,
                   "center",("Arial",20,"bold"))

    # draw title for status window
    
    tortoise.goto(22,16.5)
    tortoise.write("Name:", False, "left",
                   ("Arial",14,"normal"))

    # draw subtitle "Name"
    
    tortoise.goto(22,14.25)
    tortoise.write("Search Times Left:", False,
                   "left", ("Arial",14,"normal"))

    # draw subtitle "Search Times Left"
    
    tortoise.goto(22,12)
    tortoise.write("Items Got:", False, "left",
                   ("Arial",14,"normal"))

    # draw subtitle "Items Got"
    
    searchUpdater.goto(25.25,12.8)
    searchUpdater.write("100", False, "center",
                        ("Arial",20,"bold"))

    # draw initial search times as 100
    
    itemUpdater.goto(25.25,10.7)
    itemUpdater.write("0", False, "center",
                      ("Arial",20,"bold"))

    # draw initial item number as 0

def checkLocation():
    """check index of current block

    Parameter
        None

    Return Value
        index of the block
        
    """
    reverse = [19,18,17,16,
               15,14,13,12,
               11,10,9,8,7,
               6,5,4,3,2,1,0]                           # reversed index or coordinate
    x, y = tortoise.pos()                               # get real coordinate
    x = int(x)                                          # coordinate of bottom left cornor
    y = int(y)
    for i in range(len(reverse)):                       # transfer coordinate to index
        if reverse[i] == y:
            return x,i
     
def getItem():
    """randomly pick an item

    Parameter
        None

    Return Value
        Name of the item
        
    """
    pickUp = random.choice(items)
    if pickUp == 'The Hobbit':                          # return to the start point
        tortoise.up()
        tortoise.goto(0.5,0.5)
        tortoise.setheading(90)
        print("Welcome back!")
        print("The auction just started.")
        return pickUp
    return pickUp
  
def moveUp():
    """move turtle up one block

    Parameter
        None

    Return Value
        None
        
    """
    tortoise.up()
    tortoise.setheading(90)
    tortoise.forward(1)
    
def moveDown():
    """move turtle down one block

    Parameter
        None

    Return Value
        None
        
    """
    tortoise.up()
    tortoise.setheading(270)
    tortoise.forward(1)

def moveLeft():
    """move turtle left one block

    Parameter
        None

    Return Value
        None
        
    """
    tortoise.up()
    tortoise.setheading(180)
    tortoise.forward(1)

def moveRight():
    """move turtle right one block

    Parameter
        None

    Return Value
        None
        
    """
    tortoise.up()
    tortoise.setheading(0)
    tortoise.forward(1)

def drawLocal(x,y):
    """color the current block

    Parameter
        x: index value
        y: index value

    Return Value
        None
        
    """
    if data[y][x] == 1:                                 # use index values to find map value
        cHeading = tortoise.heading()                   # save current heading
        X,Y = tortoise.pos()                            # save current coordinate values
        tortoise.goto(int(X),int(Y))                    # go to the bottom left corner
        tortoise.setheading(0)
        drawSquare('blue')
        tortoise.goto(X,Y)                              # go back to saved coordinate
        tortoise.setheading(cHeading)                   # set heading to saved heading
        data[y][x] = 5                                  # change map value to avoid repetition

    # check map value and draw blue square if the value is 1
        
    elif data[y][x] == 2:
        cHeading = tortoise.heading()
        X,Y = tortoise.pos()
        tortoise.goto(int(X),int(Y))
        tortoise.setheading(0)
        drawSquare('yellow')
        tortoise.goto(X,Y)
        tortoise.setheading(cHeading)
        data[y][x] = 6

    # check map value and draw yellow square if the value is 2
        
def drawUp():
    """color the block above

    Parameter
        None

    Return Value
        None
        
    """
    moveUp()
    x, y = checkLocation()
    drawLocal(x,y)
    moveDown()

    # move up, fill color, and come back
    
def drawDown():
    """color the block below

    Parameter
        None

    Return Value
        None
        
    """
    moveDown()
    x, y = checkLocation()
    drawLocal(x,y)
    moveUp()

    # move down, fill color, and come back
    
def drawLeft():
    """color the block to the left

    Parameter
        None

    Return Value
        None
        
    """
    moveLeft()
    x, y = checkLocation()
    drawLocal(x,y)
    moveRight()

    # move left, fill color, and come back
    
def drawRight():
    """color the block to the right

    Parameter
        None

    Return Value
        None
        
    """
    moveRight()
    x, y = checkLocation()
    drawLocal(x,y)
    moveLeft()

    # move right, fill color, and come back
    
def search():
    """color surrounding blocks

    Parameter
        None

    Return Value
        None
        
    """
    cHeading = tortoise.heading()                       # save current heading
    x, y = checkLocation()                              # check current index values
    if x == 0 and y == 19:                              # at start point
        drawUp()
        drawRight()
    elif x == 0 and y == 0:                             # at top left cornor
        drawDown()
        drawRight()
    elif x == 19 and y == 0:                            # at bottom right cornor
        drawUp()
        drawLeft()
    elif x == 0 and 0 < y < 19:                         # at left boundary
        drawUp()
        drawDown()
        drawRight()
    elif x == 19 and 0 < y < 19:                        # at right boundary 
        drawUp()
        drawDown()
        drawLeft()
    elif y == 19 and 0 < x < 19:                        # at bottom boundary
        drawUp()
        drawLeft()
        drawRight()
    elif y == 0 and 0 < x < 19:                         # at top boundary
        drawDown()
        drawLeft()
        drawRight()
    else:                                               # at the rest of the locations
        drawUp()
        drawDown()
        drawLeft()
        drawRight()
    tortoise.setheading(cHeading)                       # set heading to saved heading

def localSearch():
    """check current block information

    Parameter
        None
    Return Value
        None
        
    """
    global itemCount                                    # this function can make changes to this global value                        
    
    x, y = checkLocation()                              # check index again after each move
    
    drawLocal(x,y)                                      # color current block according to map value
    
    if data[y][x] == 2 or data[y][x] == 6:              # if current block has an item
        item = getItem()                                # randomly get an item
        itemCount = itemCount + 1                       # update item number
        itemUpdater.clear()                             # clear item number display
        itemUpdater.write(itemCount,
                          False, "center",
                          ("Arial",20,"bold"))          # draw new item number
        data[y][x] = 7                                  # change map value to avoid repetition
        print("You got", item, "* 1") 
    elif data[y][x] == 4:                               # if current block is exit
        winProcedure()                                  # get ready to win
        
    if itemCount == 6:                                  # if all items are picked
        print("Unlock Achievement: Item Hunter")        # unlock achievement
        itemCount = 0                                   # reset item number to avoid repetition
        
    tortoise.fillcolor('red')                           # make the turtle red all the time
    screen.update()                                     # update screen after each button press

def winProcedure():
    """finish the game

    Parameter
        None

    Return Value
        None
        
    """
    timeUsed = time.time() - startTime                  # stop timer
    timeUsed = int(timeUsed)                            # time in seconds
    displayTime = "Time Used: "\
                  + str(timeUsed)\
                  + " seconds"                          # text to display time usage
    print("Congratulations! You beat the game.")
    print("Time used:",timeUsed,"seconds")
    
    tortoise.reset()
    itemUpdater.reset()
    searchUpdater.reset()
    tortoise.up()
    tortoise.hideturtle()
    itemUpdater.up()
    itemUpdater.hideturtle()
    searchUpdater.up()
    searchUpdater.hideturtle()

    # reset all the turtles
    
    tortoise.goto(15,10)
    tortoise.write("YOU WIN",False,
                   "center", ("Arial",50,"bold"))       # draw win message
    tortoise.goto(15,8)
    tortoise.write(displayTime,False,
                   "center", ("Arial",30,"bold"))       # draw time usage

def button(X,Y):
    """control the gamepad

    Parameter
        X: coordinate value
        Y: coordinate value

    Return Value
        None
        
    """
    global searchRight                                  
    global searchCount

    # this function can make changes to the two global values


    
    if 24 < X < 26 and (8-math.sqrt(3)) < Y < 8:        # up arrow area on screen
        x, y = checkLocation()                          # check index values if button is pressed
        if data[y-1][x] != 0:                           # check the next block in the intended direction
            moveUp()                                    # if the block is not wall, take action
            localSearch()                               # search the current block
    elif 24 < X < 26 and 2 < Y < (2+math.sqrt(3)):      # down arrow area on screen
        x, y = checkLocation()
        if data[y+1][x] != 0:
            moveDown()
            localSearch()
    elif 22 < X < (22+math.sqrt(3)) and 4 < Y < 6:      # left arrow area on screen
        x, y = checkLocation()
        if data[y][x-1] != 0:
            moveLeft()
            localSearch()
    elif (28-math.sqrt(3)) < X < 28 and 4 < Y < 6:      # right arrow area on screen
        x, y = checkLocation()
        if data[y][x+1] != 0:
            moveRight()
            localSearch()
    elif 24.2 < X < 25.8 and 4.2 < Y < 5.8:             # red button area on screen
        if searchRight == True:                         # if the player has search right
            search()                                    # the player may search
            searchCount = searchCount - 1               # but there is limit on search times
            if searchCount == 0:                        # if the player uses up search times
                searchRight = False                     # the player will lose search right
            searchUpdater.clear()                       # after each search, clear search display
            searchUpdater.write(searchCount,
                                False, "center",
                                ("Arial",20,"bold"))    # and draw new search times
            tortoise.fillcolor('red')                   # make the turtle red all the time
            screen.update()
        else:
            print("You can no longer search!")          # the player keeps searching without search right
    
def mainInterface():
    """draw the interface

    Parameter
        None

    Return Value
        None
        
    """
    screen.setup(1080,720)                              # set the size of window
    screen.setworldcoordinates(0,0,30,20)               # set coordinate
    tortoise.up()
    screen.tracer(0)                                    # do not show drawing process 
    drawMap()                                           # draw blocks
    drawGamepad()                                       # draw gamepad
    drawMiniwindow()                                    # draw status window
    drawStatus()                                        # draw status text

def main():
    """initialize the game

    Parameter
        None

    Return Value
        None
        
    """
    global startTime                                    # this function can make changes to this global value
    startUp.up()
    startUp.hideturtle()
    tortoise.hideturtle()
    itemUpdater.hideturtle()
    searchUpdater.hideturtle()                          # hide all the turtles at the beginning
    startUp.write("Type your name to start", False,
                  "center", ("Arial",30,"bold"))        # draw start screen
    getData3('manual.txt')                              # print user manual
    name = input("What's your name? ")                  # ask for name
    mainInterface()                                     # draw game interface
    startUp.hideturtle()
    tortoise.goto(25.25,15.4)
    tortoise.write(name, False, "center",
                   ("Arial",18,"bold"))                 # draw player's name
    tortoise.goto(0.5,0.5)
    tortoise.setheading(90)
    tortoise.fillcolor('red')                           # set up turtle for the game
    screen.update()                                     # update screen to show contents above
    
    startTime = time.time()                             # start a timer
    screen.onclick(button)                              # click to call button function
    screen.mainloop()                                   # enable interactions
    
data = getData('map.txt')                               # create map lists in global space
items = getData2('items.txt')                           # create item list in global space

tortoise = turtle.Turtle()
itemUpdater = turtle.Turtle()
searchUpdater = turtle.Turtle()
startUp = turtle.Turtle()
screen = turtle.Screen()

# create turtles and screen in global space

itemCount = 0                                           # initial value for item number
searchCount = 100                                       # initial value for search times
searchRight = True                                      # initial state of search right
startTime = 0                                           # initial value for timer

# necessary global values

main()
