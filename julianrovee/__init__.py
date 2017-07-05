import ccircle
from math import *


window = ccircle.Window("Let's just get it working!", 600, 400)
time = 0
while window.isOpen():
    window.clear(0, 0, 0)
    window.drawCircle(300,200,150,1,1,0) # Face
    window.drawCircle(300,230,100,0,0,0) # Mouth
    window.drawRect(200,100,200,130,1,1,0) # Mouth
    window.drawCircle(250, 175, 45, 0, 0, 0) # Eye
    window.drawCircle(350, 175, 45, 0, 0, 0) #Eye
    window.drawCircle(250,175,40,1,1,1)
    window.drawCircle(250,175,20,0,0,0)
    window.drawCircle(350, 175, 40, 1, 1, 1)
    window.drawCircle(350, 175, 20, 0, 0, 0)
    window.drawRect(200,175,200,55,1,1,0)
    window.drawRect(205,175,90,5,0,0,0)
    window.drawRect(305, 175, 90, 5, 0, 0, 0)
    window.update()