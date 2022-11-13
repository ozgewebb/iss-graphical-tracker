"""
Ozge Webb - 2020-11-29
ISS Tracking Project:
FINAL - SKILLS EXAM PROJECT: DISPLAY ISS INFORMATION GRAPHICALLY

This project calculates (in statute miles) and timestamps the distance from the ISS
to Dallas College Richland Campus and the outcome for this project creates a visual display of the ISS location-based solely
on the ISS Open Notify website http://open-notify.org/ information.

**************************************
The package "requests" is a Python library that handles making HTTP requests.
The package "haversine" calculates distance between two points on Earth using the latitude and longitude.
"""
import time
from haversine import haversine, Unit
import requests
from turtle import *


def ISSturtlePlotSetup():  # Graphical display program
    mode('logo')  # Logo coordinates N=0°; S=180°; E=90°; W=270°;
    style = ('Times', 20, 'bold')  # Set type style
    style2 = ('Times', 10, 'bold')  # Set type style

    # Initialize turtle and set positions
    nw = (-100, 100)
    ne = (100, 100)
    se = (100, -100)
    sw = (-100, -100)
    reset()
    clear()
    home()

    # Create display grid
    hideturtle()
    penup()
    setposition(0, 250)
    write("Ozge Webb's Graphical ISS Tracker", font=style, align='center')
    setposition(0, 230)
    write("Light Blue = 8500+ Miles; Green = 6000-8499 Miles", font=style2, align='center')
    setposition(0, 210)
    write("Yellow = 1000-5999 Miles; Red = 0-999 Miles", font=style2, align='center')
    home()
    pendown()
    pensize(5)
    forward(180)
    back(360)
    home()
    left(90)
    forward(180)
    back(360)
    home()
    penup()
    hideturtle()

    # Label the display grid
    setposition(nw)
    write('NW', font=style, align='center')
    setposition(ne)
    write('NE', font=style, align='center')
    setposition(se)
    write('SE', font=style, align='center')
    setposition(sw)
    write('SW', font=style, align='center')
    time.sleep(1)
    hideturtle()

    # Set turtle properties
    shape('triangle')
    turtlesize(3, 2, 4)
    penup()


# End ISSturtlePlotSetup

def getISS_Position():  # Query Open APIs From Space for ISS position
    url = 'http://api.open-notify.org/iss-now'
    coords = requests.get(url).json()
    get_coords = (float(coords['iss_position']['latitude']), float(coords['iss_position']['longitude']))
    return get_coords


# End function getISS_Position()

iss = getISS_Position()


def dist_to_RCL():
    richlandcollege = (32.9214, -96.7285)  # latitude and longitude information for RLC
    distance = (haversine((getISS_Position()), richlandcollege, Unit.MILES))
    distance = round(float(distance))
    return distance


rlc = dist_to_RCL()

"""
    print("ISS Distance from Richland College: ", int(dist_to_RCL()), " miles.")
    print("Current ISS Position lat/long", list(getISS_Position()), "\n")  
    time.sleep(1)
"""


# Assign turtle fill colors according to distance ranges
def ISSdistColor(rlc):
    if rlc >= 8500:
        distColor = ('lightblue')
    if rlc >= 6000 and rlc < 8500:
        distColor = ('green')
    if rlc >= 1000 and rlc < 6000:
        distColor = ('yellow')
    if rlc < 1000:
        distColor = ('red')
    return (distColor)


# End ISSdistColor

distColor = ISSdistColor(rlc)


def ISSturtlePlotNW(distColor):
    # Test the turtle position in the NW quadrant and change fill color
    hideturtle()
    color('black', distColor)
    setposition(-100, 75)
    showturtle()


# End ISSturtlePlotNW

def ISSturtlePlotNE(distColor):
    # Test the turtle position in the NW quadrant and change fill color
    hideturtle()
    color('black', distColor)
    setposition(100, 75)
    showturtle()


# End ISSturtlePlotNE

def ISSturtlePlotSE(distColor):
    # Test the turtle position in the NW quadrant and change fill color
    hideturtle()
    color('black', distColor)
    setposition(100, -125)
    showturtle()


# End ISSturtlePlotSE

def ISSturtlePlotSW(distColor):
    # Test the turtle position in the SW quadrant and change fill color
    hideturtle()
    color('black', distColor)
    setposition(-100, -125)
    showturtle()


# End ISSturtlePlotSW

def graphic():
    la = iss[0]  # latitude as a floating point value
    lo = iss[1]  # longitude as a floating point value
    if (la < 0) and (lo < 0):
        ISSturtlePlotSW(distColor)
    if (la > 0) and (lo > 0):
        ISSturtlePlotNE(distColor)
    if (la < 0) and (lo > 0):
        ISSturtlePlotSE(distColor)
    if (la > 0) and (lo < 0):
        ISSturtlePlotNW(distColor)


while True:
    print("ISS Distance from Richland College: ", int(dist_to_RCL()), " miles.")
    print("Current ISS Position lat/long", list(getISS_Position()), "\n")
    time.sleep(1)
    ISSturtlePlotSetup()
    graphic()

# print("The Richland College current 'color code' is", distColor)
