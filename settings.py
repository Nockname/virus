from random import sample, shuffle, uniform
from math import pi

PERCENTOFINFECTION=1
PERCENTOFDEATH=5
INFECTIONDISTANCE=30
INFECTIONTIME=25

MOVESPEED=1
MOVEROTATION=0.5

N_HUMANS=1000
numberOfHumans=N_HUMANS 
STARTINGINFECTED=20

WIDTH=500
HEIGHT=500

IMMUNITY=True
STOP_WHEN_VIRUS_GONE=True

CONVERT_METHOD="linear"
MAX_INFECT_COLOR=[100, 0, 0, 255]
MIN_INFECT_COLOR=[255, 150, 150, 255]
NO_INFECT_COLOR=[255, 255, 255, 255] 
BACKGROUND_COLOR=[0, 0, 0, 255]
IMMUNITY_COLOR=[255, 255, 0, 255]

COLORWHEEL=MAX_INFECT_COLOR + MIN_INFECT_COLOR + NO_INFECT_COLOR + BACKGROUND_COLOR+IMMUNITY_COLOR

startingInfectedList=[0]*N_HUMANS
for i in range(STARTINGINFECTED):
    startingInfectedList[i]=INFECTIONTIME
shuffle(startingInfectedList)

infection=[[-1 for _ in range(HEIGHT)] for _ in range(WIDTH)]
direction=[[False for _ in range(HEIGHT)] for _ in range(WIDTH)]
counter=0
for pos in sample(range(WIDTH*HEIGHT), N_HUMANS):
    infection[pos%WIDTH][pos//WIDTH] = startingInfectedList[counter]
    direction[pos%WIDTH][pos//WIDTH] = uniform(0, 2*pi)
    counter+=1

FRAMES=1000
FPS=10
VIDEO_NAME="virus"

#print(direction)