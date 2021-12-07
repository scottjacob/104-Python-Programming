
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9013695
#    Student name: Scott Jacob
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  TREASURE MAP
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "follow_path".  You are required to
#  complete this function so that when the program is run it traces
#  a path on the screen, drawing "tokens" to indicate discoveries made
#  along the way, while using data stored in a list to determine the
#  steps to be taken.  See the instruction sheet accompanying this
#  file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

grid_size = 100 # pixels
num_squares = 7 # to create a 7x7 map grid
margin = 50 # pixels, the size of the margin around the grid
legend_space = 400 # pixels, the space to leave for the legend
window_height = grid_size * num_squares + margin * 2
window_width = grid_size * num_squares + margin +  legend_space
font_size = 18 # size of characters for the coords
starting_points = ['Top left', 'Top right', 'Centre',
                   'Bottom left', 'Bottom right']

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.  (Very keen students are welcome
# to draw their own background, provided they do not change the map's
# grid or affect the ability to see it.)
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():
    
    # Set up the drawing window with enough space for the grid and
    # legend
    setup(window_width, window_height)
    setworldcoordinates(-margin, -margin, window_width - margin,
                        window_height - margin)

    # Draw as quickly as possible
    tracer(False)

    # Choose a neutral background colour (if you want to draw your
    # own background put the code here, but do not change any of the
    # following code that draws the grid)
    bgcolor('light grey')

    # Get ready to draw the grid
    penup()
    color('slate grey')
    width(2)

    # Draw the horizontal grid lines
    setheading(0) # face east
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(0, y_coord)
        pendown()
        forward(num_squares * grid_size)
        
    # Draw the vertical grid lines
    setheading(90) # face north
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(x_coord, 0)
        pendown()
        forward(num_squares * grid_size)

    # Draw each of the labels on the x axis
    penup()
    y_offset = -27 # pixels
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_coord, y_offset)
        write(str(x_coord), align = 'center',
              font=('Arial', font_size, 'normal'))

    # Draw each of the labels on the y axis
    penup()
    x_offset, y_offset = -5, -10 # pixels
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_offset, y_coord + y_offset)
        write(str(y_coord), align = 'right',
              font=('Arial', font_size, 'normal'))

    # Mark the space for drawing the legend
    goto((num_squares * grid_size) + margin, (num_squares * grid_size) // 2)
    write('    Put your legend here', align = 'left',
          font=('Arial', 24, 'normal'))    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the follow_path function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_path function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_path function.
#
# Each of the data sets is a list of instructions expressed as
# triples.  The instructions have two different forms.  The first
# instruction in the data set is always of the form
#
#     ['Start', location, token_number]
#
# where the location may be 'Top left', 'Top right', 'Centre',
# 'Bottom left' or 'Bottom right', and the token_number is an
# integer from 0 to 4, inclusive.  This instruction tells us where
# to begin our treasure hunt and the token that we find there.
# (Every square we visit will yield a token, including the first.)
#
# The remaining instructions, if any, are all of the form
#
#     [direction, number_of_squares, token_number]
#
# where the direction may be 'North', 'South', 'East' or 'West',
# the number_of_squares is a positive integer, and the token_number
# is an integer from 0 to 4, inclusive.  This instruction tells
# us where to go from our current location in the grid and the
# token that we will find in the target square.  See the instructions
# accompanying this file for examples.
#

# Some starting points - the following fixed paths just start a path
# with each of the five tokens in a different location

fixed_path_0 = [['Start', 'Top left', 0]]
fixed_path_1 = [['Start', 'Top right', 1]]
fixed_path_2 = [['Start', 'Centre', 2]]
fixed_path_3 = [['Start', 'Bottom left', 3]]
fixed_path_4 = [['Start', 'Bottom right', 4]]

# Some miscellaneous paths which encounter all five tokens once

fixed_path_5 = [['Start', 'Top left', 0], ['East', 1, 1], ['East', 1, 2],
                ['East', 1, 3], ['East', 1, 4]]
fixed_path_6 = [['Start', 'Bottom right', 0], ['West', 1, 1], ['West', 1, 2],
                ['West', 1, 3], ['West', 1, 4]]
fixed_path_7 = [['Start', 'Centre', 4], ['North', 2, 3], ['East', 2, 2],
                ['South', 4, 1], ['West', 2, 0]]

# A path which finds each token twice

fixed_path_8 = [['Start', 'Bottom left', 1], ['East', 5, 2],
                ['North', 2, 3], ['North', 4, 0], ['South', 3, 2],
                ['West', 4, 0], ['West', 1, 4],
                ['East', 3, 1], ['South', 3, 4], ['East', 1, 3]]

# Some short paths

fixed_path_9 = [['Start', 'Centre', 0], ['East', 3, 2],
                ['North', 2, 1], ['West', 2, 3],
                ['South', 3, 4], ['West', 4, 1]]

fixed_path_10 = [['Start', 'Top left', 2], ['East', 6, 3], ['South', 1, 0],
                 ['South', 1, 0], ['West', 6, 2], ['South', 4, 3]]

fixed_path_11 = [['Start', 'Top left', 2], ['South', 1, 0], ['East', 2, 4],
                 ['South', 1, 1], ['East', 3, 4], ['West', 1, 3],
                 ['South', 2, 0]]

# Some long paths

fixed_path_12 = [['Start', 'Top right', 2], ['South', 4, 0],
                 ['South', 1, 1], ['North', 3, 4], ['West', 4, 0],
                 ['West', 2, 0], ['South', 3, 4], ['East', 2, 3],
                 ['East', 1, 1], ['North', 3, 2], ['South', 1, 3],
                 ['North', 3, 2], ['West', 1, 2], ['South', 3, 4],
                 ['East', 3, 0], ['South', 1, 1]]

fixed_path_13 = [['Start', 'Top left', 1], ['East', 5, 3], ['West', 4, 2],
                 ['East', 1, 3], ['East', 2, 2], ['South', 5, 1],
                 ['North', 2, 0], ['East', 2, 0], ['West', 1, 1],
                 ['West', 5, 0], ['South', 1, 3], ['East', 3, 0],
                 ['East', 1, 4], ['North', 3, 0], ['West', 1, 4],
                 ['West', 3, 1], ['South', 4, 1], ['East', 5, 1],
                 ['West', 4, 0]]

# "I've been everywhere, man!" - this path visits every square in
# the grid, with randomised choices of tokens

fixed_path_99 = [['Start', 'Top left', randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)]

# If you want to create your own test data sets put them here
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a path
# to follow.  Your program must work for any data set that can be
# returned by this function.  The results returned by calling this
# function will be used as the argument to your follow_path function
# during marking.  For convenience during code development and
# marking this function also prints the path to be followed to the
# shell window.
#
# Note: For brevity this function uses some Python features not taught
# in IFB104 (dictionaries and list generators).  You do not need to
# understand this code to complete the assignment.
#
def random_path(print_path = True):
    # Select one of the five starting points, with a random token
    path = [['Start', choice(starting_points), randint(0, 4)]]
    # Determine our location in grid coords (assuming num_squares is odd)
    start_coords = {'Top left': [0, num_squares - 1],
                    'Bottom left': [0, 0],
                    'Top right': [num_squares - 1, num_squares - 1],
                    'Centre': [num_squares // 2, num_squares // 2],
                    'Bottom right': [num_squares - 1, 0]}
    location = start_coords[path[0][1]]
    # Keep track of squares visited
    been_there = [location]
    # Create a path up to 19 steps long (so at most there will be 20 tokens)
    for step in range(randint(0, 19)):
        # Find places to go in each possible direction, calculating both
        # the new grid square and the instruction required to take
        # us there
        go_north = [[[location[0], new_square],
                     ['North', new_square - location[1], token]]
                    for new_square in range(location[1] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_south = [[[location[0], new_square],
                     ['South', location[1] - new_square, token]]
                    for new_square in range(0, location[1])
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_west = [[[new_square, location[1]],
                    ['West', location[0] - new_square, token]]
                    for new_square in range(0, location[0])
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        go_east = [[[new_square, location[1]],
                    ['East', new_square - location[0], token]]
                    for new_square in range(location[0] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        # Choose a free square to go to, if any exist
        options = go_north + go_south + go_east + go_west
        if options == []: # nowhere left to go, so stop!
            break
        target_coord, instruction = choice(options)
        # Remember being there
        been_there.append(target_coord)
        location = target_coord
        # Add the move to the list of instructions
        path.append(instruction)
    # To assist with debugging and marking, print the list of
    # instructions to be followed to the shell window
    print('Welcome to the Treasure Hunt!')
    print('Here are the steps you must follow...')
    for instruction in path:
        print(instruction)
    # Return the random path
    return path

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "follow_path" function.
#
# Draw Icon0 - Pac-man
def Icon0():
    penup()
    setheading(0) # all icons start drawing from easterly direction
    start = position() # set position to keep icons displaying correctly
    pencolor("yellow")
    pensize(4)
    forward(3) # adjust start position to fit icon in square
    right(90)
    forward(3)
    left(90) # finish adjusting start position
    
    fillcolor("yellow")
    right(45)
    pendown() # begin drawing
    begin_fill()
    forward(40)
    right(90)
    circle(-45, 300) # main pacman body with circle drawn to 300 degrees
    right(90)
    forward(40)
    left(45)
    forward(10)
    end_fill() # end filling main pacman
    penup()
    
    pencolor("white")
    right(180)
    forward(30)
    fillcolor("white")
    begin_fill()
    circle(10)
    end_fill()
    penup()
    
    left(90)
    forward(5)
    pencolor("black")
    fillcolor("black")
    begin_fill()
    pendown()
    circle(-4)
    end_fill()
    penup()
    
    goto(start) # goto original position so loop can continue

# Draw red pacman ghost
def Icon1():
    penup()
    setheading(0)
    start = position()
    forward(35)
    right(90)
    pencolor("red")
    pensize(4)
    fillcolor("red")
    pendown()
    begin_fill()
    forward(30)
    circle(-5, 180)
    circle(5, 180)
    circle(-5, 180)
    circle(5, 180)
    circle(-5, 180)
    circle(5, 180)
    circle(-5, 180)
    forward(40)
    circle(-35, 180)
    forward(20)
    end_fill()
    penup()
    # Draw Eyes for red ghost
    right(90)
    forward(15)
    right(90)
    forward(15)
    right(90)
    pencolor("white")
    fillcolor("white")
    begin_fill()
    circle(10)
    end_fill()
    penup()

    left(180)
    forward(20)
    pendown()
    begin_fill()
    circle(-10)
    end_fill()
    
    penup()
    left(90)
    forward(3)
    right(90)
    pencolor("purple")
    fillcolor("purple")
    pendown()
    begin_fill()
    circle(-6)
    end_fill()
    penup()

    right(180)
    forward(20)
    pendown()
    begin_fill()
    circle(5)
    end_fill()
    penup()

    goto(start)

# Draw Pacman Cherry
def Icon2():
    penup()
    start = position()
    setheading(0)
    forward(47)
    right(90)
    forward(20)
    pencolor("red")
    fillcolor("red")
    pendown()
    begin_fill()
    circle(-20, 180)
    circle(-10, 140)
    left(100)
    forward(8)
    circle(-10, 147)
    end_fill()
    penup()

    right(75)
    forward(60)
    setheading(240)
    pendown()
    begin_fill()
    circle(-20, 180)
    circle(-10, 140)
    left(100)
    forward(8)
    circle(-10, 147)
    end_fill()
    penup()
    
    right(180)
    circle(10, 147)
    forward(5)
    right(90)
    pencolor("green")
    pensize(5)
    pendown()
    circle(-25, 110)
    circle(-30, 110)
    penup()
    
    right(180)
    circle(30, 100)
    right(45)
    pendown()
    circle(-10, 100) # leaf stem length and angle
    left(90)
    fillcolor("green")
    begin_fill()
    pensize(4)
    circle(10, 100)
    left(90)
    circle(10, 100)
    end_fill()
    penup()

    goto(start)

# Draw Ghosty Ghost
def Icon3():
    penup()
    setheading(0)
    start = position()
    forward(35)
    right(90)
    pencolor("dark blue")
    pensize(4)
    fillcolor("dark blue")
    pendown()
    begin_fill()
    forward(30)
    circle(-5, 180)
    circle(5, 180)
    circle(-5, 180)
    circle(5, 180)
    circle(-5, 180)
    circle(5, 180)
    circle(-5, 180)
    forward(40)
    circle(-35, 180)
    forward(20)
    end_fill()
    penup()
    # Draw Eyes for red ghost
    right(90)
    forward(20)
    right(90)
    forward(30)
    right(90)
    pencolor("white")
    fillcolor("white")
    begin_fill()
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    right(90)
    forward(10)
    end_fill()
    penup()

    left(90)
    forward(20)
    pensize(1)
    pencolor("white")
    fillcolor("white")
    pendown()
    begin_fill()
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    left(90)
    forward(10)
    end_fill()
    penup()

    right(180)
    forward(30)
    right(90)
    forward(12)
    setheading(45)
    pendown()
    pensize(3)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(10)
    left(90)
    forward(10)
    right(90)
    forward(10)
    penup()

    goto(start)

# Draw Gamepad Icon
def Icon4():
    penup()
    setheading(0)
    start = position()
    forward(40)
    pencolor("black")
    fillcolor("black")
    pendown()
    begin_fill()
    right(90)
    forward(40)
    right(90)
    forward(80)
    right(90)
    forward(80)
    right(90)
    forward(80)
    right(90)
    forward(40)
    end_fill()
    penup()

    goto(start)
    pencolor("red")
    dot(30)
    
    forward(20)
    right(90)
    pendown()
    pencolor("green")
    fillcolor("green")
    begin_fill()
    pensize(2)
    forward(15)
    left(135)
    forward(20)
    left(90)
    forward(20)
    left(135)
    forward(15)
    end_fill()
    penup()
    goto(start)

    setheading(90)
    forward(20)
    right(90)
    pendown()
    pencolor("yellow")
    fillcolor("yellow")
    begin_fill()
    pensize(2)
    forward(15)
    left(135)
    forward(20)
    left(90)
    forward(20)
    left(135)
    forward(15)
    end_fill()
    penup()
    goto(start)

    setheading(180)
    forward(20)
    right(90)
    pendown()
    pencolor("blue")
    fillcolor("blue")
    begin_fill()
    pensize(2)
    forward(15)
    left(135)
    forward(20)
    left(90)
    forward(20)
    left(135)
    forward(15)
    end_fill()
    penup()
    goto(start)

    setheading(0)
    forward(20)
    right(90)
    pendown()
    pencolor("red")
    fillcolor("red")
    begin_fill()
    pensize(2)
    forward(15)
    left(135)
    forward(20)
    left(90)
    forward(20)
    left(135)
    forward(15)
    end_fill()
    penup()
    goto(start)


    goto(start)

# Headings for main loop
# could simply be placed in loop
# but unsure of re-use later

def North():
    setheading(90)

def South():
    setheading(270)

def East():
    setheading(0)

def West():
    setheading(180)

#***************************************************************#
#                         Follow Path                           #
#***************************************************************#

# Follow the path as per the provided dataset
def follow_path(random_path):
    
    # Set up counters for later use
    # counters start at zero not -1 as
    # legend icons are drawn outside of the main for loop

    total_counter = 0
    pac_man_counter = 0
    red_ghost_counter = 0
    sad_cherry_counter = 0
    ghosty_ghost_counter = 0
    gamepad_counter = 0
    
    #***************************************************************#
    #                           LEGEND                              #
    #***************************************************************#
    
    # Draw legend
    # Position Legend bg and set colours
    penup()
    goto(750, 700)
    setheading(0)
    pensize(4)
    pencolor("black")
    fillcolor("sky blue")
    pendown()
    begin_fill()
    # Loop for brevity
    for q in range(2):
        forward(350)
        right(90)
        forward(700)
        right(90)
    end_fill()
    penup()

    # Position and Write title of legend
    setheading(0)
    forward(175)
    setheading(270)
    forward(30)
    write("Pac-Man Icons: ", False, align="center", font=("Arial", 12, "bold"))

    # Draw Icons down side of legend
    # Write text for icon pac-man
    goto(810,600)
    Icon0()
    setheading(0)
    forward(70)
    write("Pac-Man: ", align="left", font=("Arial", 10, "bold"))
    
    # Write text for icon red ghost
    goto(810, 475)
    Icon1()
    setheading(0)
    forward(70)
    write("Red Ghost: ", align="left", font=("Arial", 10, "bold"))
    
    # Write text for icon sad cherry
    goto(810, 350)
    Icon2()
    setheading(0)
    forward(70)
    write("Sad Cherry: ", align="left", font=("Arial", 10, "bold"))
    
    # Write text for icon ghosty ghost
    goto(810, 225)
    Icon3()
    setheading(0)
    forward(70)
    write("Ghosty Ghost: ", align="left", font=("Arial", 10, "bold"))
    
    # Write text for Icon gamepad
    goto(810, 100)
    Icon4()
    setheading(0)
    forward(70)
    write("Gamepad: ", align="left", font=("Arial", 10, "bold"))
   

    #***************************************************************#
    #                           Main Loop                           #
    #***************************************************************#

    # Start Loop for drawing Icons
    # If block to determine which square to start in by performing
    # a boolean check for it
    # start coords are positioned for the center of each square in the grid
    ## print statements only uncommented for testing loop progression

    for i in random_path:
        if 'Top left' in i:
            penup()
            goto(50,650)
            #print("Top Left")
        elif 'Top right' in i:
            penup()
            goto(650,650)
            #print("Top right")
        elif 'Centre' in i:
            penup()
            goto(350,350)
            #print("Centre")
        elif 'Bottom left' in i:
            penup()
            goto(50,50)
            #print("Bottom Left")
        elif 'Bottom right' in i:
            penup()
            goto(650,50)
            #print("Bottom right")
        else:
            #print('No starting point')
            pass


        # If block to determine which heading to turn to for each new Icon
        # headings are referred to in separate functions as I was unsure
        # whether I would re-use them or not
        ## print statements only uncommented for testing loop progression

        if 'North' in i:
            penup()
            North()
            #print("North")
            pass
        elif 'South' in i:
            penup()
            South()
            #print("South")
            pass
        elif 'East' in i:
            penup()
            East()
            #print("East")
            pass
        elif 'West' in i:
            penup()
            West()
            #print("West")
            pass
        else:
            #print("No Direction")
            pass 
       

       # If block to determine how many squares to move
       # pass statements used to continue through the loop
       ## print statements only uncommented for testing loop progression

        if i[1] == 1:
            #print("Move 1 square")
            forward(100)
            pass
        elif i[1] == 2:
            #print("Move 2 squares")
            forward(200)
            pass
        elif i[1] == 3:
            #print("Move 3 squares")
            forward(300)
            pass
        elif i[1] == 4:
            #print("Move 4 squares")
            forward(400)
            pass
        elif i[1] == 5:
            #print("Move 5 squares")
            forward(500)
            pass
        elif i[1] == 6:
            #print("Move 6 squares")
            forward(600)
            pass
        else:
            #print("No squares to move to")
            pass


        # If block for checking which logo to draw based
        # on which int is present in list
        # each argument will add to the counter for the icon
        # as well as the total counter
        ## print statements only uncommented for testing loop progression

        if i[2] == 0:
            #print("Logo 0")
            Icon0()
            pac_man_counter = pac_man_counter + 1
            total_counter = total_counter + 1
            #print("pac_man: ", pac_man_counter)
            pass
        elif i[2] == 1:
            #print("Logo 1")
            Icon1()
            red_ghost_counter = red_ghost_counter + 1
            total_counter = total_counter + 1
            #print("red_ghost: ", red_ghost_counter)
            pass
        elif i[2] == 2:
            #print("Logo 2")
            Icon2()
            sad_cherry_counter = sad_cherry_counter + 1
            total_counter = total_counter + 1
            #print("sad_cherry: ", sad_cherry_counter)
            pass
        elif i[2] == 3:
            #print("Logo 3")
            Icon3()
            ghosty_ghost_counter = ghosty_ghost_counter + 1
            total_counter = total_counter + 1
            #print("ghosty_ghost: ", ghosty_ghost_counter)
            pass
        elif i[2] == 4:
            #print("Logo 4")
            Icon4()
            gamepad_counter = gamepad_counter + 1
            total_counter = total_counter + 1
            #print("gamepad: ", gamepad_counter)
            pass
        else:
            #print("No Logo to draw")
            pass
    
    ###########################################
    ## Print statements for testing counters ##
    ###########################################

    # print("total_counter: ", total_counter)
    # print("pac_man: ", pac_man_counter)
    # print("red_ghost: ", red_ghost_counter)
    # print("sad_cherry: ", sad_cherry_counter)
    # print("ghosty_ghost: ", ghosty_ghost_counter)
    # print("gamepad: ", gamepad_counter)
    

    #***************************************************************#
    #                           Counters                            #
    #***************************************************************#


    # Draw total counter next to icon title
    penup()
    goto(750, 700)
    setheading(0)
    forward(270)
    setheading(270)
    forward(30)
    pencolor("white")
    write(total_counter, False, align="center", font=("Arial", 12, "bold"))

    # Draw Counters down side of legend
    goto(810,600)
    setheading(0)
    forward(170)
    write(pac_man_counter, align="center", font=("Arial", 10, "bold"))

    # Moves to and displays counter after loop has finished
    goto(810, 475)
    setheading(0)
    forward(170)
    write(red_ghost_counter, align="center", font=("Arial", 10, "bold"))

    # Moves to and displays counter after loop has finished
    goto(810, 350)
    setheading(0)
    forward(170)
    write(sad_cherry_counter, align="center", font=("Arial", 10, "bold"))
    
    # Moves to and displays counter after loop has finished
    goto(810, 225)
    setheading(0)
    forward(170)
    write(ghosty_ghost_counter, align="center", font=("Arial", 10, "bold"))
    
    # Moves to and displays counter after loop has finished
    goto(810, 100)
    setheading(0)
    forward(170)
    write(gamepad_counter, align="center", font=("Arial", 10, "bold"))
    


        
            
#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tokens
title("Pac-Man Goes Treasure Hunting")

### Call the student's function to follow the path
### ***** While developing your program you can call the follow_path
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_path()" as the
### ***** argument to the follow_path function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_path function.
# follow_path(fixed_path_0) # <-- used for code development only, not marking
follow_path(random_path()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
