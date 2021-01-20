import turtle
#create object for this turtle
tu = turtle.Turtle()                    # T capital
tu.screen.bgcolor("black")              #to change background to black
tu.pensize(2)                           #size of pen
tu.color("green")                       #initially the color of turtle will be green
#so now we start our turtle will be in right direction
#so to make it upward we will turn it left by 90 degrees
tu.left(90)
#now it will go in upward direction
#we will bring turtle down
tu.backward(100)
tu.speed(200)#speed of turtle
tu.shape('turtle')
#changes arrow into turtle shape

#we will use recursion function to draw the tree
def tree(i):
    if i<10:
        return
        #this is the base condition to stop recursion

    else:
        tu.forward(i)          #we will move our tree in forward direction
        tu.color('orange')#after making line we will make flower of orange colour
        which will be circle
        tu.circle(2)
        #after the flower is drawn we want our color back to brown to make the branches
        tu.color("brown")

        #now we want to draw it in left direction
        tu.left(30)   #so when it goes to left it will again draw flower and it will go on
                      till the value of i becomes less than 10
        tree(3*i/4)   #3*100/4 = 75 now value of i is 75 again 3*75/4 = 56.25 now again i is 56.25 again 3*56.25/4
                      this will go on
        tu.right(60)  #once left part is done it will come back by backward() and then it will go in right direction
        tree(3*i/4)
        tu.left(30)
        tu.backward(i)

tree(100)
tu.color("green")
tu.forward(100)
tu.backward(100)
turtle.done()