import ccircle

class Player:
    def __init__(self,x,y,lv):
        self.lv = lv
        self.x = x
        self.y = y
        self.count = 0
        self.countdown = 0
        self.facing  =  True
        self.image1 = ccircle.Image('Bluebody.png')
        self.image2 = ccircle.Image('Bluebody2.png')
        self.heads = ccircle.Image('Heads.png')

    def move(self):
        if ccircle.isKeyDown('a'):
            self.facing = False
        elif ccircle.isKeyDown('d'):
            self.facing = True
        else:
            self.count = 0

    def draw(self,window,ex):
        if self.facing:
            if self.count==0:
                self.image1.drawSub(self.x, self.y, 69, 69, 276, 0, 69, 69)
            elif self.count % 4 == 0:
                self.image1.drawSub(self.x, self.y, 69, 69, 0,0,69,69)
            elif self.count % 4 == 1:
                self.image1.drawSub(self.x, self.y, 69, 69, 70, 0, 69, 69)
            elif self.count % 4 == 2:
                self.image1.drawSub(self.x, self.y, 69, 69, 139, 0, 69, 69)
            elif self.count % 4 == 3:
                self.image1.drawSub(self.x, self.y, 69, 69, 208, 0, 69, 69)
            if self.lv == 0:
                self.heads.drawSub(self.x+8, self.y-60, 50, 70, 0, 0, 50, 70)
            elif self.lv == 1:
                self.heads.drawSub(self.x+8, self.y-60, 50, 70, 51, 0, 50, 70)
            elif self.lv == 2:
                self.heads.drawSub(self.x+8, self.y-60, 50, 70, 102, 0, 50, 70)
            elif self.lv == 3:
                self.heads.drawSub(self.x+8, self.y-60, 50, 70, 153, 0, 50, 70)


        if not self.facing:
            if self.count == 0:
                self.image2.drawSub(self.x, self.y, 69, 69, 276, 0, 69, 69)
            elif self.count % 4 == 3:
                self.image2.drawSub(self.x, self.y, 69, 69, 0, 0, 69, 69)
            elif self.count % 4 == 2:
                self.image2.drawSub(self.x, self.y, 69, 69, 70, 0, 69, 69)
            elif self.count % 4 == 1:
                self.image2.drawSub(self.x, self.y, 69, 69, 139, 0, 69, 69)
            elif self.count % 4 == 0:
                self.image2.drawSub(self.x, self.y, 69, 69, 208, 0, 69, 69)
            if self.lv == 0:
                self.heads.drawSub(self.x+12, self.y-60, 50, 70, 153, 71, 50, 70)
            elif self.lv == 1:
                self.heads.drawSub(self.x+12, self.y-60, 50, 70, 103, 71, 50, 70)
            elif self.lv == 2:
                self.heads.drawSub(self.x+12, self.y-60, 50, 70, 51, 71, 50, 70)
            elif self.lv == 3:
                self.heads.drawSub(self.x+12, self.y-60, 50, 70, 0, 71, 50, 70)



    def update(self, dt):

        if ccircle.isKeyDown('a') or ccircle.isKeyDown('d') :
            self.countdown += dt
        if self.countdown >= 1:
            self.count += 1
            self.countdown = 0
        if ccircle.isKeyDown('d'):
            self.x += dt * 25
        if ccircle.isKeyDown('a'):
            self.x -= dt * 25
        if self.x>940:
            self.x = 940
        if self.x<100:
            self.x = 100


