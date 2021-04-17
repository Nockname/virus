from settings import *
from math import sin, cos
from random import uniform, random

class SpreadVirus:
    @staticmethod
    def __inGrid(xCord, yCord):
        return xCord >= 0 and yCord >= 0 and xCord < WIDTH and yCord < HEIGHT

    @staticmethod
    def __nextHumanPos(xCord, yCord, infection, direction, MOVESPEED, MOVEROTATION):

        randomAngle=uniform(-MOVEROTATION, MOVEROTATION)+direction[xCord][yCord]

        nextX = int(xCord + MOVESPEED*cos(randomAngle))
        nextY = int(yCord + MOVESPEED*sin(randomAngle))

        
        direction[xCord][yCord]=randomAngle

        if SpreadVirus.__inGrid(nextX, nextY):
            if infection[nextX][nextY]==-1:
                infection[nextX][nextY]=infection[xCord][yCord]
                infection[xCord][yCord]=-1

                direction[nextX][nextY]=randomAngle
                direction[xCord][yCord]=False

        return infection, direction

    @staticmethod
    def calculate(infection, direction, MOVESPEED, MOVEROTATION, INFECTIONDISTANCE, PERCENTOFINFECTION, numberOfHumans, IMMUNITY):

        #decrease infection time by 1 and possibly kill people
        for xValue in range(WIDTH):
            for yValue in range(HEIGHT):
                if infection[xValue][yValue]>=1:
                    if random() < PERCENTOFDEATH/100:
                        infection[xValue][yValue]=-1
                        direction[xValue][yValue]=False
                        numberOfHumans-=1

                    else:
                        if infection[xValue][yValue]==1 and IMMUNITY:
                            infection[xValue][yValue]=-2
                        else:
                            infection[xValue][yValue]-=1

        #print("Kill Done")
        # print(max(max(x) if isinstance(x, list) else x for x in  infection))

        #getting infection
        for xValue in range(WIDTH):
            for yValue in range(HEIGHT):
                if infection[xValue][yValue]==0:
                    
                    #cycle through all pixels near the pixel
                    isBreak=False
                    for xChange in range(-INFECTIONDISTANCE, INFECTIONDISTANCE+1):
                        if isBreak:
                            isBreak=False
                            break
                        for yChange in range(-INFECTIONDISTANCE, INFECTIONDISTANCE+1):
                            #Check coordinate
                            if SpreadVirus.__inGrid(xValue+xChange, yValue+yChange):
                                if infection[xValue+xChange][yValue+yChange]>1:
                                    if xChange*xChange+yChange*yChange<=INFECTIONDISTANCE*INFECTIONDISTANCE:
                                        #Possibly give infection
                                        if random() < PERCENTOFINFECTION/100:
                                            infection[xValue][yValue] = INFECTIONTIME
                                            isBreak=True
                                            break
        
        #print("INFECTION SPREAD DONE")

        #moving to next position
        for xValue in range(WIDTH):
            for yValue in range(HEIGHT):
                infection, direction=SpreadVirus.__nextHumanPos(xValue, yValue, infection, direction, MOVESPEED, MOVEROTATION)
        
        return infection, direction, numberOfHumans