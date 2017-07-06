import ccircle

window = ccircle.Window()
window.toggleMaximized()

points = []

size = 5
rval = 0.5
gval = 0.5
bval = 0.5

while window.isOpen():
    window.clear(0.2,0.2,0.2)
    mx,my = window.getMousePos()

    if ccircle.isKeyDown('down'):
        size -= 5
    elif ccircle.isKeyDown('up'):
        size += 5

    if ccircle.isKeyDown('r'):
        if ccircle.isKeyDown('left'):
            rval -= 0.02
        elif ccircle.isKeyDown('right'):
            rval += 0.02
    if ccircle.isKeyDown('g'):
        if ccircle.isKeyDown('left'):
            gval -= 0.02
        elif ccircle.isKeyDown('right'):
            gval += 0.02
    if ccircle.isKeyDown('b'):
        if ccircle.isKeyDown('left'):
            bval -= 0.02
        elif ccircle.isKeyDown('right'):
            bval += 0.02

    if ccircle.isMouseDown('left'):
        points.append([mx,my,size,rval,gval,bval])
        print(points)

    for x,y,s,r,g,b in points:
         window.drawCircle(x,y,s,r,g,b)

    window.drawCircle(mx, my, size, rval, gval, bval)



    window.update()