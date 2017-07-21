import ccircle
import World
import back
import Player
import time
import Moves
import Enemy


window = ccircle.Window('Cantercorn', 1024,512)
myWorld = World.World('test')
bg =  back.Back(0,0)
myWorld.add(bg)

lv = 2
px = 170
ex = 800

myPlayer1 = Player.Players(px,360,lv, True,'s','f','BlueBody.png','Heads.png')
myWorld.add(myPlayer1)

myPlayer2 = Player.Players(ex,360,lv, True,'left','right','RedBody.png','RHeads.png')
myWorld.add(myPlayer2)

m11 = 2
m12 = 6
myMoves1 = Moves.moves(15,120,m11,m12,'1','2',ex)
myWorld.add(myMoves1)

m21 = 3
m22 = 7
myMoves2 = Moves.moves(909,120,m21,m22,'n','m',px)
myWorld.add(myMoves2)

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
    print(dis)

    myMoves1.if_clicked(dis)
    myMoves2.if_clicked(dis)


    myWorld.draw(window)
    myWorld.update(dt)
    window.update()
