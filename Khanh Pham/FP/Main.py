import ccircle
import World
import back
import Player
import time

window = ccircle.Window('Cantercorn', 1024,512)
myWorld = World.World('test')
bg =  back.Back(0,0)
myWorld.add(bg)

myPlayer = Player.Player(480,360)
myWorld.add(myPlayer)

lv = 2

start = time.time()
dt = 1.0/60.0
while window.isOpen():
    window.clear(0.8,0.8,0.8)
    myPlayer.move()
    bg.move()
    myWorld.draw(window,lv)
    myWorld.update(dt)
    window.update()

