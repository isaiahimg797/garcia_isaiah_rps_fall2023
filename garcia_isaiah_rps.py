# This code was created by Isaiah Garcia on 9/19/23

# all outside functions used
import turtle
from turtle import *
import os
import random
import time

# The os module allows us to access the current directory in order to access assets
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')


# define screen so its easier to type
screen = turtle.Screen()
# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

# size of the images the user can chose - used for hitbox calculation
rock_w, rock_h  = 256, 280
scissors_w, scissors_h = 256, 170
paper_w, paper_h = 256, 204

# setup the Screen class using the turtle module  
screen.setup(WIDTH + 4, HEIGHT + 8)  
# fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="white")

# canvas object
sc = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
sc._rootwindow.resizable(False, False)

# define where rock image is and places it on righ of screen - same thing for scissors and paper
rock_image = os.path.join(images_folder, 'rock.gif')
rock_instance = turtle.Turtle()
screen.addshape(rock_image)
rock_instance.shape(rock_image)
rock_instance.penup()
rock_pos_x = -300
rock_pos_y = 0
rock_instance.setpos(rock_pos_x,rock_pos_y)

paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
screen.addshape(paper_image)
paper_instance.shape(paper_image)
paper_instance.penup()
paper_pos_x = 0
paper_pos_y = 0
paper_instance.setpos(paper_pos_x,paper_pos_y)

scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
screen.addshape(scissors_image)
scissors_instance.shape(scissors_image)
scissors_instance.penup()
scissors_pos_x = 300
scissors_pos_y = 0
scissors_instance.setpos(scissors_pos_x,scissors_pos_y)

#defines cpu rock image, same for scissors and paper
cpu_rock_image = os.path.join(images_folder, 'cpu_rock.gif')
cpu_rock_instance = turtle.Turtle()
hideturtle()

cpu_scissors_image = os.path.join(images_folder, 'cpu_scissors.gif')
cpu_scissors_instance = turtle.Turtle()
hideturtle()

cpu_paper_image = os.path.join(images_folder, 'cpu_paper.gif')
cpu_paper_instance = turtle.Turtle()
hideturtle()

# makes turtle easier to write and makes a turtle for writing text
t = turtle.Turtle()
# instantiate a turtle for writing text
text = turtle.Turtle()
text.color('black')
text.hideturtle()


# function determies if there is a collision
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else: 
        return False


# function determines cpu choice and the player choice, then figures out who wins
def play(x, y):
        # cpu choice using random function
        computerlist = ["rock", "paper", "scissors"]
        computerInput = random.choice(computerlist)

        # clears instructions
        turtle.clear()

        # whichever image the user collides with is there choice, then hides the other choices
        if collide(x,y,rock_instance,rock_w,rock_h):
            print("I collided with rock")
            paper_instance.hideturtle()
            scissors_instance.hideturtle()
            userInput = "rock"
        elif collide(x,y,scissors_instance,scissors_w,scissors_h):
            print("I collided with scissors")
            paper_instance.hideturtle()
            rock_instance.hideturtle()
            userInput = "scissors"
            scissors_pos_x = -300
            scissors_pos_y = 0
            scissors_instance.setpos(scissors_pos_x,scissors_pos_y)
        elif collide(x,y,paper_instance,paper_w,paper_h):
            print("I collided with paper")
            scissors_instance.hideturtle()
            rock_instance.hideturtle()
            userInput = "paper"
            paper_pos_x = -300
            paper_pos_y = 0
            paper_instance.setpos(paper_pos_x,paper_pos_y)
        else:
            print("No collision")
        
        #code which figures out who won, bring the user choice to right and cpu choice to the left, writes out who won
        # if the computer and user picks the same thing - a tie
        if computerInput == userInput:
            print("It's a tie! I chose", computerInput, "you chose", userInput)
            if computerInput == "rock": 
                screen.addshape(cpu_rock_image)
                cpu_rock_instance.shape(cpu_rock_image)
                cpu_rock_instance.penup()
                cpu_rock_pos_x = 300
                cpu_rock_pos_y = 0
                cpu_rock_instance.setpos(cpu_rock_pos_x,cpu_rock_pos_y)
            elif computerInput == "paper": 
                screen.addshape(cpu_paper_image)
                cpu_paper_instance.shape(cpu_paper_image)
                cpu_paper_instance.penup()
                cpu_paper_pos_x = 300
                cpu_paper_pos_y = 0
                cpu_paper_instance.setpos(cpu_paper_pos_x,cpu_paper_pos_y)
            elif computerInput == "scissors":
                screen.addshape(cpu_scissors_image)
                cpu_scissors_instance.shape(cpu_scissors_image)
                cpu_scissors_instance.penup()
                cpu_scissors_pos_x = 300
                cpu_scissors_pos_y = 0
                cpu_scissors_instance.setpos(cpu_scissors_pos_x,cpu_scissors_pos_y)  
            t.write("It's a tie", align="center", font=("Arial",20))   
        # same thing if the computer picks rock
        elif computerInput == "rock":
            screen.addshape(cpu_rock_image)
            cpu_rock_instance.shape(cpu_rock_image)
            cpu_rock_instance.penup()
            cpu_rock_pos_x = 300
            cpu_rock_pos_y = 0
            cpu_rock_instance.setpos(cpu_rock_pos_x,cpu_rock_pos_y)
            if userInput == "scissors":
                    print("You lose, computer wins!")
                    t.write("You lose, computer wins!", align="center", font=("Arial",20))
            elif userInput == "paper":
                    print("You win!")
                    t.write("You win!", align="center", font=("Arial",20))
        # same thing if the computer picks scissors
        elif computerInput == "scissors":
            screen.addshape(cpu_scissors_image)
            cpu_scissors_instance.shape(cpu_scissors_image)
            cpu_scissors_instance.penup()
            cpu_scissors_pos_x = 300
            cpu_scissors_pos_y = 0
            cpu_scissors_instance.setpos(cpu_scissors_pos_x,cpu_scissors_pos_y)    
            if userInput == "paper":
                    print("You lose, computer wins!")
                    t.write("You lose, computer wins!", align="center", font=("Arial",20))
            elif userInput == "rock":
                    print("You win!")
                    t.write("You win!", align="center", font=("Arial",20))
        # same thing if computer picks paper
        elif computerInput == "paper":
            screen.addshape(cpu_paper_image)
            cpu_paper_instance.shape(cpu_paper_image)
            cpu_paper_instance.penup()
            cpu_paper_pos_x = 300
            cpu_paper_pos_y = 0
            cpu_paper_instance.setpos(cpu_paper_pos_x,cpu_paper_pos_y)
            if userInput == "rock":
                    print("You lose, computer wins!")
                    t.write("You lose, computer wins!", align="center", font=("Arial",20))
            elif userInput == "scissors":
                    print("You win!")
                    t.write("You win!", align="center", font=("Arial",20))
        #thanks the user for playing, uses time function to allow the user to actually read the text that pops up
        time.sleep(0.75)
        screen.clear()
        turtle.write("Thanks for playing!", align="center", font=("Arial",20))
        time.sleep(0.75)
        screen.bye()

#moves turtle to top of screen and gives user instructions
turtle.penup()
turtle.setposition(0,150)
turtle.pendown()
turtle.write("Choose Rock Paper or Scissors", align="center", font=("Arial",20))

#run the play function once a hitbox is clicked
screen.onclick(play)

# needed to be last 
screen.mainloop()
