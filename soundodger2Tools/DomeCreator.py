from tkinter import *
import internal.DomePatternCreator
import math

root = Tk()
root.title('Dome Pattern Creator')
root.configure(bg='white')

#DomeCircle
domeCircleLabel = Label(root, text='Dome Circle', font=('bold'), bg='white', fg='black')
domeCircleLabel.grid(row=0, column=0)

#time
domeCircleTimeLabel = Label(root, text='Dome Circle Time', bg='white', fg='black')
domeCircleTimeLabel.grid(row=1, column=0)
domeCircleTime = Scale(root, from_=0, to=600, orient=HORIZONTAL, bg='grey', fg='white')
domeCircleTime.grid(row=2, column=0)

#type
domeCircleTypeLabel = Label(root, text='Dome Circle Type (hard or soft)', bg='white', fg='black')
domeCircleTypeLabel.grid(row=3, column=0)
domeCircleTypeEntry = Entry(root, bg='grey', fg='white')
domeCircleTypeEntry.grid(row=4, column=0)

#sizeStart
domeCircleSSLabel = Label(root, text='Dome Circle Dome Start Size', bg='white', fg='black')
domeCircleSSLabel.grid(row=5, column=0)
domeCircleSS = Scale(root, from_=0, to=300, orient=HORIZONTAL, bg='grey', fg='white')
domeCircleSS.grid(row=6, column=0)

#sizeEnd
domeCircleESLabel = Label(root, text='Dome Circle Dome End Size', bg='white', fg='black')
domeCircleESLabel.grid(row=7, column=0)
domeCircleES = Scale(root, from_=0, to=300, orient=HORIZONTAL, bg='grey', fg='white')
domeCircleES.grid(row=8, column=0)

#Duration
domeCircleDirLabel = Label(root, text='Dome Circle Duration', bg='white', fg='black')
domeCircleDirLabel.grid(row=9, column=0)
domeCircleDir = Scale(root, from_=0, to=50, orient=HORIZONTAL, bg='grey', fg='white')
domeCircleDir.grid(row=10, column=0)

#Layer
domeCirclelLabel = Label(root, text='Dome Circle Layer', bg='white', fg='black')
domeCirclelLabel.grid(row=11, column=0)
domeCirclel = Scale(root, from_=1, to=10, orient=HORIZONTAL, bg='grey', fg='white')
domeCirclel.grid(row=12, column=0)

#Radius
domeCircleRadiusLabel = Label(root, text='Dome Circle Radius', bg='white', fg='black')
domeCircleRadiusLabel.grid(row=13, column=0)
domeCircleRadius = Scale(root, from_=1, to=500, orient=HORIZONTAL, bg='grey', fg='white')
domeCircleRadius.grid(row=14, column=0)

#offsetX
domeCircleXLabel = Label(root, text='Dome Circle X Offset', bg='white', fg='black')
domeCircleXLabel.grid(row=15, column=0)
domeCircleX = Scale(root, from_=-500, to=500, orient=HORIZONTAL, bg='grey', fg='white')
domeCircleX.grid(row=16, column=0)

#offsetY
domeCircleYLabel = Label(root, text='Dome Circle Y Offset', bg='white', fg='black')
domeCircleYLabel.grid(row=17, column=0)
domeCircleY = Scale(root, from_=-500, to=500, orient=HORIZONTAL, bg='grey', fg='white')
domeCircleY.grid(row=18, column=0)

#domeAmount
domeCircleAmLabel = Label(root, text='Dome Circle Dome Amount', bg='white', fg='black')
domeCircleAmLabel.grid(row=19, column=0)
domeCircleAm = Scale(root, from_=1, to=120, orient=HORIZONTAL, bg='grey', fg='white')
domeCircleAm.grid(row=20, column=0)

#EXEC
def domeCircleEXfunction():
    internal.DomePatternCreator.domeCircle(domeCircleTime.get(), domeCircleTypeEntry.get(), domeCircleSS.get(), domeCircleES.get(), domeCircleDir.get(), domeCirclel.get(), domeCircleRadius.get(), domeCircleX.get(), domeCircleY.get(), domeCircleAm.get())
    mLabel = Label(root, text='Succesfully wrote XML lines', bg='white', fg='black')
    mLabel.grid(row=22, column=0)

domeCircleEXEC = Button(root, text='Write XML lines for dome circle', bg='white', fg='black', command=domeCircleEXfunction)
domeCircleEXEC.grid(row=21, column=0)

#------------------------------
#DomeSquare
domeSquareLabel = Label(root, text='Dome Rectangle', font=('bold'), bg='white', fg='black')
domeSquareLabel.grid(row=0, column=1)

#time
BdomeCircleTimeLabel = Label(root, text='Dome Rectangle Time', bg='white', fg='black')
BdomeCircleTimeLabel.grid(row=1, column=1)
BdomeCircleTime = Scale(root, from_=0, to=600, orient=HORIZONTAL, bg='grey', fg='white')
BdomeCircleTime.grid(row=2, column=1)

#type
BdomeCircleTypeLabel = Label(root, text='Dome Rectangle Type (hard or soft)', bg='white', fg='black')
BdomeCircleTypeLabel.grid(row=3, column=1)
BdomeCircleTypeEntry = Entry(root, bg='grey', fg='white')
BdomeCircleTypeEntry.grid(row=4, column=1)

#sizeStart
BdomeCircleSSLabel = Label(root, text='Dome Rectangle Dome Start Size', bg='white', fg='black')
BdomeCircleSSLabel.grid(row=5, column=1)
BdomeCircleSS = Scale(root, from_=0, to=300, orient=HORIZONTAL, bg='grey', fg='white')
BdomeCircleSS.grid(row=6, column=1)

#sizeEnd
BdomeCircleESLabel = Label(root, text='Dome Rectangle Dome End Size', bg='white', fg='black')
BdomeCircleESLabel.grid(row=7, column=1)
BdomeCircleES = Scale(root, from_=0, to=300, orient=HORIZONTAL, bg='grey', fg='white')
BdomeCircleES.grid(row=8, column=1)

#Duration
BdomeCircleDirLabel = Label(root, text='Dome Rectangle Duration', bg='white', fg='black')
BdomeCircleDirLabel.grid(row=9, column=1)
BdomeCircleDir = Scale(root, from_=0, to=50, orient=HORIZONTAL, bg='grey', fg='white')
BdomeCircleDir.grid(row=10, column=1)

#Layer
BdomeCirclelLabel = Label(root, text='Dome Rectangle Layer', bg='white', fg='black')
BdomeCirclelLabel.grid(row=11, column=1)
BdomeCirclel = Scale(root, from_=1, to=10, orient=HORIZONTAL, bg='grey', fg='white')
BdomeCirclel.grid(row=12, column=1)

#offsetX
BdomeCircleXLabel = Label(root, text='Dome Rectangle X Offset', bg='white', fg='black')
BdomeCircleXLabel.grid(row=13, column=1)
BdomeCircleX = Scale(root, from_=-500, to=500, orient=HORIZONTAL, bg='grey', fg='white')
BdomeCircleX.grid(row=14, column=1)

#offsetY
BdomeCircleYLabel = Label(root, text='Dome Rectangle Y Offset', bg='white', fg='black')
BdomeCircleYLabel.grid(row=15, column=1)
BdomeCircleY = Scale(root, from_=-500, to=500, orient=HORIZONTAL, bg='grey', fg='white')
BdomeCircleY.grid(row=16, column=1)

#Width
BdomeCircleWidthLabel = Label(root, text='Dome Rectangle Width', bg='white', fg='black')
BdomeCircleWidthLabel.grid(row=17, column=1)
BdomeCircleWidth = Scale(root, from_=1, to=50, orient=HORIZONTAL, bg='grey', fg='white')
BdomeCircleWidth.grid(row=18, column=1)

#Height
BdomeCircleHeightLabel = Label(root, text='Dome Rectangle height', bg='white', fg='black')
BdomeCircleHeightLabel.grid(row=19, column=1)
BdomeCircleHeight = Scale(root, from_=1, to=50, orient=HORIZONTAL, bg='grey', fg='white')
BdomeCircleHeight.grid(row=20, column=1)

#domeAmount
BdomeCircleAmLabel = Label(root, text='Dome Rectangle Dome Amount', bg='white', fg='black')
BdomeCircleAmLabel.grid(row=21, column=1)
BdomeCircleAm = Scale(root, from_=1, to=120, orient=HORIZONTAL, bg='grey', fg='white')
BdomeCircleAm.grid(row=22, column=1)

#EXEC
def domeSquareEXfunction():
    #internal.DomePatternCreator.domeRectangle(time, type, sizestart, sizeEnd, duration, layer, offsetX, offsetY, width, height, domeAmount)
    internal.DomePatternCreator.domeRectangle(BdomeCircleTime.get(), BdomeCircleTypeEntry.get(), BdomeCircleSS.get(), BdomeCircleES.get(), BdomeCircleDir.get(), BdomeCirclel.get(), BdomeCircleX.get(), BdomeCircleY.get(), BdomeCircleWidth.get(), BdomeCircleHeight.get(), BdomeCircleAm.get())
    mLabel = Label(root, text='Succesfully wrote XML lines', bg='white', fg='black')
    mLabel.grid(row=24, column=1)

domeCircleEXEC = Button(root, text='Write XML lines for dome rectangle', bg='white', fg='black', command=domeSquareEXfunction)
domeCircleEXEC.grid(row=23, column=1)

#------------------------------
#DomeLine
domeLineLabel = Label(root, text='Dome Line', font=('bold'), bg='white', fg='black')
domeLineLabel.grid(row=0, column=2)

#time
BBdomeCircleTimeLabel = Label(root, text='Dome Line Time', bg='white', fg='black')
BBdomeCircleTimeLabel.grid(row=1, column=2)
BBdomeCircleTime = Scale(root, from_=0, to=600, orient=HORIZONTAL, bg='grey', fg='white')
BBdomeCircleTime.grid(row=2, column=2)

#type
BBdomeCircleTypeLabel = Label(root, text='Dome Line Type (hard or soft)', bg='white', fg='black')
BBdomeCircleTypeLabel.grid(row=3, column=2)
BBdomeCircleTypeEntry = Entry(root, bg='grey', fg='white')
BBdomeCircleTypeEntry.grid(row=4, column=2)

#sizeStart
BBdomeCircleSSLabel = Label(root, text='Dome Line Dome Start Size', bg='white', fg='black')
BBdomeCircleSSLabel.grid(row=5, column=2)
BBdomeCircleSS = Scale(root, from_=0, to=300, orient=HORIZONTAL, bg='grey', fg='white')
BBdomeCircleSS.grid(row=6, column=2)

#sizeEnd
BBdomeCircleESLabel = Label(root, text='Dome Line Dome End Size', bg='white', fg='black')
BBdomeCircleESLabel.grid(row=7, column=2)
BBdomeCircleES = Scale(root, from_=0, to=300, orient=HORIZONTAL, bg='grey', fg='white')
BBdomeCircleES.grid(row=8, column=2)

#Duration
BBdomeCircleDirLabel = Label(root, text='Dome Line Duration', bg='white', fg='black')
BBdomeCircleDirLabel.grid(row=9, column=2)
BBdomeCircleDir = Scale(root, from_=0, to=50, orient=HORIZONTAL, bg='grey', fg='white')
BBdomeCircleDir.grid(row=10, column=2)

#Layer
BBdomeCirclelLabel = Label(root, text='Dome Line Layer', bg='white', fg='black')
BBdomeCirclelLabel.grid(row=11, column=2)
BBdomeCirclel = Scale(root, from_=1, to=10, orient=HORIZONTAL, bg='grey', fg='white')
BBdomeCirclel.grid(row=12, column=2)

#offsetX
BBdomeCircleXLabel = Label(root, text='Dome Line X Offset', bg='white', fg='black')
BBdomeCircleXLabel.grid(row=13, column=2)
BBdomeCircleX = Scale(root, from_=-500, to=500, orient=HORIZONTAL, bg='grey', fg='white')
BBdomeCircleX.grid(row=14, column=2)

#offsetY
BBdomeCircleYLabel = Label(root, text='Dome Line Y Offset', bg='white', fg='black')
BBdomeCircleYLabel.grid(row=15, column=2)
BBdomeCircleY = Scale(root, from_=-500, to=500, orient=HORIZONTAL, bg='grey', fg='white')
BBdomeCircleY.grid(row=16, column=2)

#Length
BBdomeCircleWidthLabel = Label(root, text='Dome Line Length', bg='white', fg='black')
BBdomeCircleWidthLabel.grid(row=17, column=2)
BBdomeCircleWidth = Scale(root, from_=1, to=500, orient=HORIZONTAL, bg='grey', fg='white')
BBdomeCircleWidth.grid(row=18, column=2)

#Angle
BBdomeCircleHeightLabel = Label(root, text='Dome Line Angle', bg='white', fg='black')
BBdomeCircleHeightLabel.grid(row=19, column=2)
BBdomeCircleHeight = Scale(root, from_=0, to=360, orient=HORIZONTAL, bg='grey', fg='white')
BBdomeCircleHeight.grid(row=20, column=2)

#domeAmount
BBdomeCircleAmLabel = Label(root, text='Dome Line Dome Amount', bg='white', fg='black')
BBdomeCircleAmLabel.grid(row=21, column=2)
BBdomeCircleAm = Scale(root, from_=1, to=120, orient=HORIZONTAL, bg='grey', fg='white')
BBdomeCircleAm.grid(row=22, column=2)

#EXEC
def domeLineEXfunction():
    #internal.DomePatternCreator.domeLine(time, type, sizestart, sizeend, duration, layer, offsetX, offsetY, length, angle, domeAmount)
    internal.DomePatternCreator.domeLine(BBdomeCircleTime.get(), BBdomeCircleTypeEntry.get(), BBdomeCircleSS.get(), BBdomeCircleES.get(), BBdomeCircleDir.get(), BBdomeCirclel.get(), BBdomeCircleX.get(), BBdomeCircleY.get(), BBdomeCircleWidth.get(), BBdomeCircleHeight.get() * (math.pi / 180), BBdomeCircleAm.get())
    mLabel = Label(root, text='Succesfully wrote XML lines', bg='white', fg='black')
    mLabel.grid(row=24, column=2)

domeCircleEXEC = Button(root, text='Write XML lines for dome line', bg='white', fg='black', command=domeLineEXfunction)
domeCircleEXEC.grid(row=23, column=2)
#------------------------------
#DomePendulum
domePendulumLabel = Label(root, text='Dome Pendulum', font=('bold'), bg='white', fg='black')
domePendulumLabel.grid(row=0, column=3)

#time
BBBdomeCircleTimeLabel = Label(root, text='Dome Pendulum Time', bg='white', fg='black')
BBBdomeCircleTimeLabel.grid(row=1, column=3)
BBBdomeCircleTime = Scale(root, from_=0, to=600, orient=HORIZONTAL, bg='grey', fg='white')
BBBdomeCircleTime.grid(row=2, column=3)

#type
BBBdomeCircleTypeLabel = Label(root, text='Dome Pendulum Type (hard or soft)', bg='white', fg='black')
BBBdomeCircleTypeLabel.grid(row=3, column=3)
BBBdomeCircleTypeEntry = Entry(root, bg='grey', fg='white')
BBBdomeCircleTypeEntry.grid(row=4, column=3)

#sizeStart
BBBdomeCircleSSLabel = Label(root, text='Dome Pendulum Dome Start Size', bg='white', fg='black')
BBBdomeCircleSSLabel.grid(row=5, column=3)
BBBdomeCircleSS = Scale(root, from_=0, to=300, orient=HORIZONTAL, bg='grey', fg='white')
BBBdomeCircleSS.grid(row=6, column=3)

#sizeEnd
BBBdomeCircleESLabel = Label(root, text='Dome Pendulum Dome End Size', bg='white', fg='black')
BBBdomeCircleESLabel.grid(row=7, column=3)
BBBdomeCircleES = Scale(root, from_=0, to=300, orient=HORIZONTAL, bg='grey', fg='white')
BBBdomeCircleES.grid(row=8, column=3)

#Duration/simspeed
BBBdomeCircleDirLabel = Label(root, text='Dome Pendulum Simulation Speed (smaller is faster)', bg='white', fg='black')
BBBdomeCircleDirLabel.grid(row=9, column=3)
BBBdomeCircleDir = Scale(root, from_=1, to=100, orient=HORIZONTAL, bg='grey', fg='white')
BBBdomeCircleDir.grid(row=10, column=3)

#Layer
BBBdomeCirclelLabel = Label(root, text='Dome Pendulum Layer', bg='white', fg='black')
BBBdomeCirclelLabel.grid(row=11, column=3)
BBBdomeCirclel = Scale(root, from_=1, to=10, orient=HORIZONTAL, bg='grey', fg='white')
BBBdomeCirclel.grid(row=12, column=3)

#offsetX
BBBdomeCircleXLabel = Label(root, text='Dome Pendulum X Offset', bg='white', fg='black')
BBBdomeCircleXLabel.grid(row=13, column=3)
BBBdomeCircleX = Scale(root, from_=-500, to=500, orient=HORIZONTAL, bg='grey', fg='white')
BBBdomeCircleX.grid(row=14, column=3)

#offsetY
BBBdomeCircleYLabel = Label(root, text='Dome Pendulum Y Offset', bg='white', fg='black')
BBBdomeCircleYLabel.grid(row=15, column=3)
BBBdomeCircleY = Scale(root, from_=-500, to=500, orient=HORIZONTAL, bg='grey', fg='white')
BBBdomeCircleY.grid(row=16, column=3)

#Length
BBBdomeCircleWidthLabel = Label(root, text='Dome Pendulum Length', bg='white', fg='black')
BBBdomeCircleWidthLabel.grid(row=17, column=3)
BBBdomeCircleWidth = Scale(root, from_=1, to=500, orient=HORIZONTAL, bg='grey', fg='white')
BBBdomeCircleWidth.grid(row=18, column=3)

#animationLength
BBBdomeCircleAmLabel = Label(root, text='Dome Pendulum Animation Length', bg='white', fg='black')
BBBdomeCircleAmLabel.grid(row=19, column=3)
BBBdomeCircleAm = Scale(root, from_=1, to=100, orient=HORIZONTAL, bg='grey', fg='white')
BBBdomeCircleAm.grid(row=20, column=3)

#EXEC
def domePendEXfunction():
    #internal.DomePatternCreator.domePendulum(time, type, sizestart, sizeend, simspeed, layer, offsetX, offsetY, pendulumLength, pendulumVelocity, animationLength)
    internal.DomePatternCreator.domePendulum(BBBdomeCircleTime.get(), BBBdomeCircleTypeEntry.get(), BBBdomeCircleSS.get(), BBBdomeCircleES.get(), BBBdomeCircleDir.get()/100, BBBdomeCirclel.get(), BBBdomeCircleX.get(), BBBdomeCircleY.get(), BBBdomeCircleWidth.get(), BBBdomeCircleWidth.get(), BBBdomeCircleAm.get())
    mLabel = Label(root, text='Succesfully wrote XML lines', bg='white', fg='black')
    mLabel.grid(row=22, column=3)

domeCircleEXEC = Button(root, text='Write XML lines for dome pendulum', bg='white', fg='black', command=domePendEXfunction)
domeCircleEXEC.grid(row=21, column=3)

root.mainloop()