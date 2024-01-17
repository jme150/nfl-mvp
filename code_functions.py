"""
    NFL MVP Tracker -- Functions
    Judah Ellison
    December 2023/January 2024
"""
# Imports
import turtle
from code_VariableService import VariableService
import code_settings as s

# Temporary function to print coordinates clicked
def print_coordinates(x , y):
    print(f"({x}, {y})")

# Function to draw horizontal axis
def draw_horizontal_axis():
    '''
    FUNCTION: draw_horizontal_axis()
        Draws horizontal axis of graph
    PARAMETERS:
        None
    RETURNS:
        None (Draws axis with Turtle)
    '''
    # Pen up
    s.crayon.penup()
    # Move turtle to proper coordinates
    s.crayon.setposition(-580, -200)
    # Pen down
    s.crayon.pendown()
    # For loop to draw axis with tick marks for each week
    for i in range(18):
        # Draw top portion of tick mark
        s.crayon.setheading(90)
        s.crayon.forward(10)
        # Draw bottom portion of tick mark
        s.crayon.backward(20)
        # Draw week number
        s.crayon.penup()
        s.crayon.backward(20)
        s.crayon.setheading(0)
        if i < 10:
            adjustment = 3
        else:
            adjustment = 6
        s.crayon.backward(adjustment)
        s.crayon.write(i + 1, font= ("Arial", 15))
        s.crayon.forward(adjustment)
        s.crayon.setheading(90)
        # Draw axis
        s.crayon.forward(30)
        s.crayon.pendown()
        s.crayon.setheading(0)
        if i < 17:
            s.crayon.forward(70)
# Function to draw vertical axis
def draw_vertical_axis():
    '''
    FUNCTION: draw_vertical_axis()
        Draws vertical axis of graph
    PARAMETERS:
        None
    RETURNS:
        None (Draws axis with Turtle)
    '''
    # Pen up
    s.crayon.penup()
    # Move turtle to proper coordinates
    s.crayon.setposition(-580, -200)
    # Pen down
    s.crayon.pendown()
    # For loop to draw axis with tick marks for each week
    for i in range(8):
        # Draw right tick mark
        s.crayon.setheading(0)
        s.crayon.forward(10)
        # Draw left tick mark
        s.crayon.backward(20)
        # Draw odds label
        s.crayon.penup()
        s.crayon.backward(50)
        s.crayon.sety(s.crayon.ycor() - 9)
        s.crayon.write(f"+{1200 - (150 * i)}", font= ("Arial", 15))
        # Draw axis
        s.crayon.setpos(-580, s.crayon.ycor() + 9)
        s.crayon.pendown()
        s.crayon.setheading(90)
        if i < 7:
            s.crayon.forward(80)
    
# Function to draw graph
def draw_graph():
    '''
    FUNCTION: draw_graph()
        Draws the background graph for the tracker
    PARAMETERS:
        None
    RETURNS: 
        None (Draws graph with Turtle)
    '''
    # Draw horizontal axis
    draw_horizontal_axis()
    # Draw vertical axis
    draw_vertical_axis()