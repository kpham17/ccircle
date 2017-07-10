import ccircle
import Sky
import world
import bush
import random
import time
import ball

window = ccircle.Window('lab 5', 800,600)
myWorld = world.World('d34d')
a = []
for i in range(200):
    x = random.randint(0,800)
    y = random.randint(0, 150)
    size = random.randint(50,75)
    color = random.uniform(0.5,1)
    vx = random.randint(-30,30)
    myWorld.add(Sky.Cloud(x,y,size,color,vx))

for i in range(1000):
    x = random.randint(0,800)
    y = random.randint(400, 800)
    size = random.randint(10,40)
    color = random.uniform(0.5,1)
    myWorld.add(bush.Bush(x,y,size,color))
for i in range(1):
    x = random.randint(200, 600)
    y = random.randint(200, 400)
    myWorld.add(ball.Ball(x,y))
    a.append([x,y])

start = time.time()
dt = 1.0/60.0
while window.isOpen():
    window.clear(0.8,0.8,0.8)
    x,y = window.getMousePos()
    my_ball.apply_force(100,1009.8)
    myWorld.draw(window)
    myWorld.update(dt,x,y)
    window.update()

    now = time.time()
    dt = now-start
    start = now