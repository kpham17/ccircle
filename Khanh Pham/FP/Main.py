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
myPlayer = Player.Player(px,360,lv)
myWorld.add(myPlayer)

ex = 800
myEnemy = Enemy.Enemy(ex,360, 3)
myWorld.add(myEnemy)

m1 = 2
m2 = 6
myMoves = Moves.moves(15,120,m1,m2)
myWorld.add(myMoves)

start = time.time()
dt = 1.0/60.0
while window.isOpen():
    window.clear(0.8,0.8,0.8)

    myPlayer.move()
    if ccircle.isKeyDown('d'):
        px += dt * 25
    if ccircle.isKeyDown('a'):
        px -= dt * 25
    if px > 940:
        px = 940
    if px < 100:
        px = 100

    myEnemy.move()
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

    if ccircle.isMouseDown('left') or ccircle.isKeyDown('T'):
        mx, my = window.getMousePos()
        myMoves.if_clicked(mx,my,dis)

    myWorld.draw(window,ex)
    myWorld.update(dt)
    window.update()
