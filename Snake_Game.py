import turtle
import time
import random

delay = 0.1

# create score
score = 0
high_score = 0


# set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
# screen.bgpic("snakebg2.gif")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.left(90)
head.shape("triangle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#  Creating Snake food as eluka
eluka = turtle.Turtle()
eluka.speed(0)
eluka.shape("circle")
eluka.color("red")
eluka.penup()
eluka.goto(0, 100)

parts = []

# creating a board for displaying score and highscore
score_board = turtle.Turtle()
score_board.speed(0)
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.goto(50,250)
score_board.write('Score: 0  High Score: 0', align="left", font=("arial", 10, "normal"))

# create a title board to display title
title_board = turtle.Turtle()

title_board.speed(0)

title_board.color("white")

title_board.penup()

title_board.hideturtle()

title_board.goto(-200,250)

title_board.write('Snake Game', align="right", font=("arial", 10, "normal"))

def upside():
	    if head.direction != "down":
	    	head.direction = "up"

    
def downside():
	if head.direction != "up":
		head.direction = "down"

               
def left():
	 	if head.direction != "right":
	 		head.direction = "left"

        

def right():
		if head.direction != "left":
			head.direction = "right"


# move functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.setheading(90)
        head.sety(y+20)
        
    if head.direction == "down":

        y = head.ycor()

        head.setheading(270)

        head.sety(y-20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setheading(180)
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setheading(0)
        head.setx(x+20)

# keyboard bindings
screen.listen()
screen.onkeypress(upside, "Up")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(downside,"Down")

# Main game loop
while True:
    screen.update()

    # Check for a collision with the border
    if head.xcor() > 500 or head.xcor() < -500 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the parts
        for part in parts:
            part.goto(1000, 1000)

        # Clear the parts list
        parts.clear()
        # reset score
        score = 0
        # Reset the delay
        delay = 0.1
        
        score_board.clear()
        score_board.write('Score: {}  High Score: {}'.format(score, high_score), align="left", font=("arial", 10, "normal"))        


    #Check for a collision with the eluka

    if head.distance(eluka)<20:
        # move the eluka to a random spot
        x = random.randint(-285, 285)
        y = random.randint(-285, 285)
        eluka.goto(x, y)

        # Adding new body parts
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("square")
        new_part.color("grey")
        new_part.penup()
        parts.append(new_part)

        # Shorten the delay
        delay -= 0.001
        
        # increasing score
        score +=5
        
        if score > high_score:
        	high_score = score
        score_board.clear()
        score_board.write('Score: {}  High Score: {}'.format(score, high_score), align="left", font=("arial", 10, "normal"))
    # Move the end part first in reverse order
    for index in range(len(parts)-1, 0, -1):
        x = parts[index-1].xcor()
        y = parts[index-1].ycor()
        parts[index].goto(x, y)
    # Move part 0 to where the head is
    if len(parts) > 0:
        x = head.xcor()
        y = head.ycor()
        parts[0].goto(x, y)

    move()
    # we wil check for head collisons with body part
    for part in parts:
    	if part.distance(head) < 20:
    		time.sleep(1)
    		head.goto(0, 0)
    		head.direction = "stop"
    		
    		# hide body parts
    		for part in parts:
    			part.goto(1000, 1000)
    			
    		# clear parts of list
    		parts.clear()
    		
    		# reset the score
    		score =0
    		
    		# score reset kavadaniki koncham delay
    		delay = 0.1
    		score_board.clear()
    		score_board.write('Score: {}  High Score: {}'.format(score, high_score), align="left", font=("arial", 10, "normal"))
    		
    
    time.sleep(delay)

screen.mainloop()
