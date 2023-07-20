import math
import SDformat

#format_CodeToSDbullet(time, enemy, pattern, duration, type, color, aim, offset, speed, layer)

#--format_CodeToSDbullet possibles:
#time: 0-len(song)
#enemy: 0-amountOfEnemies
#pattern: stream, normal, burst
#duration: leave 0 if there is none. 0-inf
#type: arrow, homing, bubble, plus, heart
#color: 1-len(colors)
#aim: center, player, world
#offset: any positive number
#speed: any number
#spread: any number
#amount: any number
#layer 1-9

f = open('writeIn.txt', "w")
linesToWrite = []

def arena_to_coord(x, y, startOffset):
    Ang = math.atan2(x, y)
    AngInDeg = Ang * (180/math.pi)

    p1 = ((x)**2) + ((y)**2)
    sizeBase = (math.sqrt(p1))/5

    linesToWrite.append(SDformat.format_CodeToAngle(startOffset, AngInDeg, 1))
    linesToWrite.append(SDformat.format_CodeToSize(startOffset, sizeBase))
    linesToWrite.append(SDformat.format_CodeToSDbullet(startOffset, 1, "normal", 0, "bubble", 1, "center", 0, 0, 0, 1, 1))

for line in linesToWrite:
    f.write(line)
    f.write('\n')
