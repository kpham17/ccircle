import ccircle
import World
import back
import Player
import time
import Moves

window = ccircle.Window('Cantercorn', 1024,512)
myWorld = World.World('test')
bg =  back.Back(0,0)
myWorld.add(bg)

lv = 2

myPlayer = Player.Player(480,360,lv)
myWorld.add(myPlayer)

m1 = 0
m2 = 3
myMoves = Moves.moves(30,120,m1,m2)
myWorld.add(myMoves)

start = time.time()
dt = 1.0/60.0
while window.isOpen():
    window.clear(0.8,0.8,0.8)
    myPlayer.move()
    myWorld.draw(window)
    if ccircle.isMouseDown('left'):
        mx, my = window.getMousePos()
        myMoves.if_clicked(mx,my)
    myWorld.update(dt)
    window.update()

