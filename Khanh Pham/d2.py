import ccircle
import math
import random

window = ccircle.Window("Let's not")
window.toggleMaximized()

sizeX, sizeY = window.getSize()

count = 500
countInt = 0


a = int(min(sizeX , sizeY)* 0.25)

randX  = random.randint(a,sizeX - a)
randY  = random.randint(a,sizeY-a)
fcolor = countInt/count

while window.isOpen():
    # mouseX, mouseY = window.getMousePos()
    # a = mouseY/sizeY
    window.clear(0, 0, 0)
    if countInt == 0:
        randX = random.randint(a, sizeX - a)
        randY = random.randint(a, sizeY - a)
        countInt = count

    else:
        countInt -= 1
        fcolor = (countInt - 50)/ count
    window.drawCircle(randX, randY, a, fcolor,fcolor,fcolor)
    window.drawCircle(randX, randY+10, 150 ,fcolor, fcolor*2/3,fcolor/3)
    window.drawRect(randX-175,randY-175,350,200,fcolor,fcolor,fcolor)
    window.drawCircle(randX - 70, randY -70, 40, fcolor, 0, 0)
    window.drawCircle(randX + 70, randY -70, 40, fcolor, 0, 0)
    window.drawTri(randX-40,randY-40,randX,randY-110,randX-110,randY-110, fcolor, fcolor, fcolor)
    window.drawTri(randX+40,randY-40,randX,randY-110,randX+110,randY-110, fcolor, fcolor, fcolor)
    for i in range(0,4):
        window.drawLine(randX-125+50*i, randY +160, randX-100+50*i, randY+10, 5,fcolor,fcolor,fcolor )
    for i in range(0,4):
        window.drawLine(randX-75+50*i, randY+10, randX-50+50*i, randY+160, 5,fcolor,fcolor,fcolor )


    window.update()



