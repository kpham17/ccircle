import ccircle

class Back:
    def __init__(self,x,y):
        self.image = ccircle.Image('BackGround.png')
        self.x = x
        self.y = y
        self.count = 0
        self.countdown = 0

    def move(self):
        if ccircle.isKeyDown('left'):
            self.x+=1
        elif ccircle.isKeyDown('right'):
            self.x-=1
        if self.x <= -1024:
            self.x = 0
        if self.x >= 1024:
            self.x = 0


    def draw(self,window,lv):
        self.image.draw(self.x, self.y, 1024, 512)
        self.image.draw(self.x+1024, self.y, 1024, 512)
        self.image.draw(self.x - 1024, self.y, 1024, 512)
        window.drawRect(0,0,150,512,0,0,0,.5)

    def update(self, dt):
        if ccircle.isKeyDown('right') or ccircle.isKeyDown('left') :
            self.countdown += dt
        if self.countdown >= 1.25:
            self.count += 1
            self.countdown = 0
