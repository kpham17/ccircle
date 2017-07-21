import ccircle
import World
import back
import Player
import time
import Moves
import Enemy

state0 = []
state1 = []
pg = 0

state2 = []

choosecount = 0
choosecount2 = 0

title = ccircle.Font('Broadview Regular.ttf')


window = ccircle.Window('Cantercorn', 1024,512)
myWorld = World.World('test')
bg =  back.Back(0,0)
myWorld.add(bg)
state1.append(bg)
state0.append(bg)
state2.append(bg)

ps1 = False
ps2 = False
lv = 2
px = 140
ex = 800

myPlayer1 = Player.Players(px,360,lv, True,'s','f','BlueBody.png','Heads.png')
state1.append(myPlayer1)

myPlayer2 = Player.Players(ex,360,lv, False,'left','right','RedBody.png','RHeads.png')
state1.append(myPlayer2)

m11 = 2
m12 = 6
myMoves1 = Moves.moves(15,120,m11,m12,'1','2',ex,'left','right')


m21 = 3
m22 = 7
myMoves2 = Moves.moves(930,120,m21,m22,'n','m',px,'s','f')


start = time.time()
dt = 1.0/60.0




while window.isOpen():
    window.clear(0.8,0.8,0.8)

    myPlayer1.move()
    if ccircle.isKeyDown('f'):
        px += dt * 25
    if ccircle.isKeyDown('s'):
        px -= dt * 25
    if px > 940:
        px = 940
    if px < 100:
        px = 100

    myPlayer2.move()
    if ccircle.isKeyDown('left'):
        ex -= dt * 25
    if ccircle.isKeyDown('right'):
        ex += dt * 25
    if ex > 940:
        ex = 940
    if ex < 100:
        ex = 100

    dis = abs(ex -px)


    if pg == 0:
        myWorld.objects = state0
        myWorld.draw(window)
        window.drawRect(0,0,1025,512,0,0,0,.5)
        title.drawCentered('CANTORCORN', 512, 180, 31, 0.6, 0, 0.4)
        title.drawCentered('CANTORCORN',512,170,30,1,0,0.8)
        window.drawRect(260,270, 200, 50, 0.7,0.7,0.7)
        window.drawRect(560, 270, 200, 50, 0.7, 0.7, 0.7)
        title.drawCentered('Start', 360, 295, 20, 0.2, 0.2, 0.2)
        title.drawCentered('Rules',660,295,20,0.2,0.2,0.2)

        mx,my = window.getMousePos()
        if 260<mx<460 and 270<my<320 and ccircle.isMouseDown('left'):
            pg = 2
    if pg == 2:
        myWorld.objects = state0
        myWorld.draw(window)
        window.drawRect(0, 0, 1025, 512, 0, 0, 0, .5)
        weapon = ccircle.Image('Weapons.png')
        for i in range(8):
            mx, my = window.getMousePos()
            window.drawRect(25,1+61*i-(i-1), 50, 50, 0, 0, 0)
            window.drawRect(940, 1 + 61 * i - (i - 1), 50, 50, 0, 0, 0)
            if i < 4:
                ly = 0
                a = i
            else:
                ly = 47
                a = i - 4
            weapon.drawSub(25, 1+62*i-(i-1), 46, 46, 47 * a - (a - 1), ly, 46, 46)
            weapon.drawSub(940, 1 + 62 * i - (i - 1), 46, 46, 47 * a - (a - 1), ly, 46, 46)
            if 1+61*i-(i-1)< my < 51+61*i-(i-1) and ccircle.wasKeyPressed('z'):
                if 25 < mx < 75:
                    if choosecount == 0:
                        m11 = i
                    elif choosecount == 1:
                        m12 = i
                    choosecount += 1
                if 940 < mx < 990:
                    if choosecount2 == 0:
                        m21 = i
                    elif choosecount2 == 1:
                        m22 = i
                    choosecount2 += 1

            window.drawRect(25, 1+62*m11-(m11-1), 50, 50, 0.7, 0.7, 0)
            window.drawRect(25, 1+62*m12-(m12-1), 50, 50, 0.7, 0.7, 0)
            window.drawRect(940, 1+62*m21-(m21-1), 50, 50, 0.7, 0.7, 0)
            window.drawRect(940, 1+62*m22-(m22-1), 50, 50, 0.7, 0.7, 0)



            window.drawRect(412, 400, 200, 50, 0.7, 0.7, 0.7)
            title.drawCentered('Enter', 512, 425, 20, 0.2, 0.2, 0.2)
            if 412 < mx < 612 and 400 < my < 450 and ccircle.isMouseDown('left'):
                pg = 1



    if pg == 1:
        myWorld.objects = state1
        myWorld.draw(window)
        myMoves1.draw(window,m11,m12)
        myMoves2.draw(window,m21,m22)
        myMoves1.if_clicked(dis)
        myMoves2.if_clicked(dis)
        if myMoves2.eh <= 0 or myMoves1.eh <= 0:
            pg  = 0
        myMoves2.update(dt)
        myMoves1.update(dt)

    myWorld.update(dt)
    window.update()
