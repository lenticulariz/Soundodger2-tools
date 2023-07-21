def format_CodeToSDbullet(time, enemy, pattern, duration, type, color, aim, offset, speed, spread, amount, layer):
    if color != 1:
        if pattern == "stream":
            s = f'<Bullet time="{time}" en="{enemy}" patt="{pattern}" type="{type}" col="{color}" aim="{aim}" amt="{amount}" dur="{duration}" offset="{offset}" speed="{speed}" spread="{spread}" lyr="{layer}" />'
        else:
            s = f'<Bullet time="{time}" en="{enemy}" patt="{pattern}" type="{type}" col="{color}" aim="{aim}" amt="{amount}" offset="{offset}" speed="{speed}" spread="{spread}" lyr="{layer}" />'
    else:
        if pattern == "stream":
            s = f'<Bullet time="{time}" en="{enemy}" patt="{pattern}" type="{type}" col="{color}" aim="{aim}" amt="{amount}" dur="{duration}" offset="{offset}" speed="{speed}" spread="{spread}" lyr="{layer}" />'
        else:
            s = f'<Bullet time="{time}" en="{enemy}" patt="{pattern}" type="{type}" aim="{aim}" amt="{amount}" offset="{offset}" speed="{speed}" spread="{spread}" lyr="{layer}" />'

    print(s)
    return s

def format_CodeToAngle(time, angle, layer):
    s = f'<ArenaAngle time="{time}" angle="{angle}" lyr="{layer}" />'

    print(s)
    return s

def format_CodeToSize(time, size):
    s = f'<Event type="size" time="{time}" val="{size}" />'

    print(s)
    return s

def format_CodeToDome(time, type, sizeStart, sizeEnd, duration, posX, posY, layer):
    s = f'<Dome time="{time}" type="{type}" size="{sizeStart},{sizeEnd}" dur="{duration}" place="coord" pos="{posX},{posY}" lyr="{layer}" />'

    print(s)
    return s

def format_CodeToSpinrate(time, spinRate):
    s = f'<Event type="spin" time="{time}" val="{spinRate}" />'

    print(s)
    return s
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

#<Event type="spin" time="1.683" val="1" />
