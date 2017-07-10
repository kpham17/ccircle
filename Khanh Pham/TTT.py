import ccircle
'''
def change(list,b1,b2):
    if list[b1][b2] != -1:
        if list[b1][b2] % 2 == 0:
            list[b1][b2] = 0
        else:
            list[b1][b2] = 1
        return(list[b1][b2])
'''

window = ccircle.Window("Tic-tac-toe",530,548)

a = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
b = 0
win = False
while window.isOpen():

    window.clear(0.8, 0.8, 0.8)
    for i in range(2):
        window.drawRect(170+170*i, 0, 2, 512, 0, 0, 0)
    for i in range(2):
        window.drawRect(0,170 +170*i, 512,2, 0, 0, 0)
    if not win:
        if ccircle.isMouseDown("left"):
            x,y = window.getMousePos()
            for i in range(3):
                for j in range(3):
                    if 172*i < x < 170+172*i and 172*j < y < 170+172*j :
                        if a[i][j] == -1:
                            if b % 2 == 0:
                                a[i][j] = 0
                            else:
                                a[i][j] = 1
                            b += 1


    for i in range(3):
        for j in range(3):
            z=a[i]
            if z[j] != -1:
                if z[j] % 2 == 0:
                    window.drawCircle(85+172*i,85+172*j,80,1,0,0)
                    window.drawCircle(85 + 172 * i, 85 + 172 * j, 75, 0.8, 0.8, 0.8)
                else:
                    window.drawRect(5+172*i,5+172*j,160,160,0,0,1)
                    window.drawRect(10 + 172 * i, 10 + 172 * j, 150, 150, 0.8, 0.8, 0.8)
    for i in range(3):
        if ((a[i][0] == 0 and a[i][1] == 0 and a[i][2] == 0) or
                (a[0][i] == 0 and a[1][i] == 0 and a[2][i] == 0) or
                (a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0) or
                (a[0][2] == 0 and a[1][1] == 0 and a[2][0] == 0)):
            window.drawRect(0, 0, 512, 512, 1, 0, 0,0.25)
            win = True
        elif ((a[i][0] == 1 and a[i][1] == 1 and a[i][2] == 1) or
                (a[0][i] == 1 and a[1][i] == 1 and a[2][i] == 1) or
                (a[0][0] == 1 and a[1][1] == 1 and a[2][2] == 1) or
                (a[0][2] == 1 and a[1][1] == 1 and a[2][0] == 1)):
            window.drawRect(0, 0, 512, 512, 0, 0, 1, 0.25)
            win = True

    window.update()

