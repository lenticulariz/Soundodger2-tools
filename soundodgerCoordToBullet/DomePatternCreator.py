import math
import SDformat

f = open('writeIn.txt', "w")
linesToWrite = []

#format_CodeToDome(time, type, sizeStart, sizeEnd, duration, posX, posY, layer)
#types: hard, soft

def domeCircle(time, type, sizeStart, sizeEnd, duration, layer, radius, offsetX, offsetY, domeAmount):
    for dome in range(domeAmount):
        linesToWrite.append(SDformat.format_CodeToDome(time, type, sizeStart, sizeEnd, duration, offsetX + (math.cos(dome) * radius), offsetY + (math.sin(dome) * radius), layer))

def domeRectangle(time, type, sizeStart, sizeEnd, duration, layer, offsetX, offsetY, width, height, domeAmount):
    for dome in range(domeAmount):
        #top side
        linesToWrite.append(SDformat.format_CodeToDome(time, type, sizeStart, sizeEnd, duration, offsetX + ((dome - (domeAmount/2)) * width), offsetY + (height * (domeAmount/2)), layer))
    for dome in range(domeAmount):
        #bottom side
        linesToWrite.append(SDformat.format_CodeToDome(time, type, sizeStart, sizeEnd, duration, offsetX + ((dome - (domeAmount/2)) * width), offsetY - (height * (domeAmount/2)), layer))
    for dome in range(domeAmount):
        #left side
        linesToWrite.append(SDformat.format_CodeToDome(time, type, sizeStart, sizeEnd, duration, offsetX - (width * (domeAmount/2)), offsetY + ((dome - (domeAmount/2)) * height), layer))
    for dome in range(domeAmount):
        #right side
        linesToWrite.append(SDformat.format_CodeToDome(time, type, sizeStart, sizeEnd, duration, offsetX + (width * (domeAmount/2)), offsetY + ((dome - (domeAmount/2)) * height), layer))

def domePendulum(time, type, sizeStart, sizeEnd, simSpeed, layer, offsetX, offsetY, pendulumLength, pendulumVelocity, animationLength):
    g = 9.8
    T = (2 * math.pi) * math.sqrt(pendulumLength/g)
    for frame in range(animationLength):
        
        ThetaX = math.sin((math.pi * (frame*10)) * T) * pendulumVelocity
        ThetaY = -1 * math.sqrt((pendulumLength**2) - (ThetaX**2))
        linesToWrite.append(SDformat.format_CodeToDome(time+(frame*simSpeed), type, sizeStart, sizeEnd, simSpeed, 
                                                        offsetX + (ThetaX), 
                                                        offsetY + (ThetaY),
                                                        layer))

def domeCustomParametric(time, type, sizeStart, sizeEnd, duration, layer, offsetX, offsetY, domeAmount, a):
    #write your own parametric function and graph it with domes!
    #do it in the offset X and offset Y parameters
    #replace where the x would be with dome
    for dome in range(domeAmount):
        linesToWrite.append(SDformat.format_CodeToDome(time, type, sizeStart, sizeEnd, duration, offsetX + ((math.cos(dome) + math.sin(dome*4)) * a), offsetY + ((math.sin(dome) + math.cos(dome*4)) * a), layer))

def domeCustomAnimatedParametric(time, simSpeed, type, sizeStart, sizeEnd, layer, offsetX, offsetY, domeAmount, a, animationLength):
    #write your own parametric function and graph it with domes!
    #do it in the offset X and offset Y parameters
    #replace where the x would be with dome
    #The time variable is frame
    for frame in range(animationLength):
        for dome in range(domeAmount):
            linesToWrite.append(SDformat.format_CodeToDome(time+(frame*simSpeed), type, sizeStart, sizeEnd, simSpeed, 
                                                           offsetX + (math.cos(dome + (frame/2)) * a), 
                                                           offsetY + (math.cos(dome) * a), 
                                                           layer))

#--
#code goes here

#--

for line in linesToWrite:
    f.write(line)
    f.write('\n')