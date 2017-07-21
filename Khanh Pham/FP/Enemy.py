import ccircle

class Enemy:
    def __init__(self,x,y,lv):
        self.lv = lv
        self.x = x
        self.y = y
        self.count = 0
        self.countdown = 0
        self.facing  =  False
        self.image1 = ccircle.Image('RedBody.png')
        self.heads = ccircle.Image('RHeads.png')

    def move(self):
        if ccircle.isKeyDown('left'):
            self.facing = False
        elif ccircle.isKeyDown('right'):
            self.facing = True
        else:
            self.count = 0

    def draw(self,window,ex):
        for i in range(4):
            if self.facing:
                if self.count == 0:
                    self.image1.drawSub(self.x, self.y, 69, 69, 276, 0, 69, 69)
                elif self.count%4 == i:
                    self.image1.drawSub(self.x, self.y, 69, 69, 70*i-(i-1), 0, 69, 69)
                if self.lv == i:
                    self.heads.drawSub(self.x + 8, self.y - 61, 50, 70, 51*i-(i-1), 0, 50, 70)
            if not self.facing:
                if self.count == 0:
                    self.image1.drawSub(self.x, self.y, 69, 69, 0, 70, 69, 69)
                elif self.count % 4 == i:
                    self.image1.drawSub(self.x, self.y, 69, 69, 70*(4-i)-(3-i), 70, 69, 69)
                if self.lv == i:
                    self.heads.drawSub(self.x + 11, self.y - 61, 50, 70, 51*(3-i)-(2-i), 71, 50, 70)




    def update(self, dt):

        if ccircle.isKeyDown('left') or ccircle.isKeyDown('right') :
            self.countdown += dt
        if self.countdown >= 1:
            self.count += 1
            self.countdown = 0
        if ccircle.isKeyDown('right'):
            self.x += dt * 25
        if ccircle.isKeyDown('left'):
            self.x -= dt * 25
        if self.x>940:
            self.x = 940
        if self.x<0:
            self.x = 0


