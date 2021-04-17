from settings import *
from virus import *
import os
import numpy as np
from PIL import Image


from math import log

class Graphics:
    @staticmethod
    def __convert(Input, Maximum, CONVERT_METHOD, COLORWHEEL):
        if Input>=1:
            if CONVERT_METHOD=="binary":
                magnitudePercent=1
            elif CONVERT_METHOD=="linear":
                magnitudePercent=(Input)/Maximum
            elif CONVERT_METHOD=="logarithmic":
                magnitudePercent=(log(Input))/log(Maximum)
            elif CONVERT_METHOD=="expontial":
                magnitudePercent=(10*Input)/log(Maximum)

            Red=int((COLORWHEEL[4]-COLORWHEEL[0])*magnitudePercent+COLORWHEEL[0])
            Green=int((COLORWHEEL[5]-COLORWHEEL[1])*magnitudePercent+COLORWHEEL[1])
            Blue=int((COLORWHEEL[6]-COLORWHEEL[2])*magnitudePercent+COLORWHEEL[2])
            Alpha=int((COLORWHEEL[7]-COLORWHEEL[3])*magnitudePercent+COLORWHEEL[3])
        if Input==0:
            Red=COLORWHEEL[8]
            Green=COLORWHEEL[9]
            Blue=COLORWHEEL[10]
            Alpha=COLORWHEEL[11]
        if Input==-1:
            Red=COLORWHEEL[12]
            Green=COLORWHEEL[13]
            Blue=COLORWHEEL[14]
            Alpha=COLORWHEEL[15]
        if Input==-2:
            Red=COLORWHEEL[16]
            Green=COLORWHEEL[17]
            Blue=COLORWHEEL[18]
            Alpha=COLORWHEEL[19]

        return Red, Green, Blue, Alpha

    @staticmethod
    def image(CONVERT_METHOD, COLORWHEEL, frame, numberOfHumans, infection, direction, IMMUNITY):
        infection, direction, numberOfHumans=SpreadVirus.calculate(infection.copy(), direction.copy(), 
        MOVESPEED, MOVEROTATION, INFECTIONDISTANCE, PERCENTOFINFECTION, numberOfHumans, IMMUNITY)

        resultInfections=infection

        pixels=np.ndarray( (WIDTH, HEIGHT, 4) )

        print(frame/FRAMES)

        for x in range(WIDTH):
            for y in range(HEIGHT):
                pixels[x][y]=Graphics.__convert(resultInfections[x][y], 
                INFECTIONTIME, CONVERT_METHOD, COLORWHEEL)

        image=Image.fromarray(np.uint8(pixels)).convert('RGB')
        image.save("./data/{}.png".format(frame))

        return numberOfHumans

placeHolder=True
for frame in range(0, FRAMES):
    if not placeHolder:
        break
    
    numberOfHumans=Graphics.image(CONVERT_METHOD, COLORWHEEL, 
    frame, numberOfHumans, infection, direction, IMMUNITY)

    if STOP_WHEN_VIRUS_GONE:
        placeHolder=False
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if infection[x][y]>=1:
                    placeHolder=True

    print(numberOfHumans)


os.system("rm ./{}.mov; ffmpeg -framerate {} -start_number 1 -i ./data/%d.png {}.mov".format(
    VIDEO_NAME, FPS, VIDEO_NAME))