from math import *
import ccircle

wx = 400
wy = 600
dots_x = 10
dots_y = 5
window = ccircle.Window("Let's go boys",wx+20,wy+20)
playerPos = wx/2


while window.isOpen():
    window.clear(0,0,0)
    if ccircle.isKeyDown('left'):
        window.clear(0,0,0)

    for i in range(0,dots_x):
        print(i * wx/dots_x + wx/(2*dots_x))
        for j in range(0,dots_y):
            window.drawRect(i * wx/dots_x + wx/(2*dots_x),j * wx/ dots_x + wx/(2*dots_x),wx/(dots_x*3),wx/(dots_x*3))
    window.drawTri()
    window.update()
