import ccircle

class Back:
    def __init__(self,x,y):
        self.image = ccircle.Image('BackGround.png')
        self.x = x
        self.y = y
        self.count = 0
        self.countdown = 0

    def draw(self,window,ex):
        self.image.draw(self.x, self.y, 1024, 512)
        self.image.draw(self.x+1024, self.y, 1024, 512)
        self.image.draw(self.x - 1024, self.y, 1024, 512)
        window.drawRect(0,0,100,512,0,0,1,.5)
        window.drawRect(924, 0, 100, 512, 1, 0, 0, .5)

    def update(self, dt):
        pass
        '''
        if ccircle.isKeyDown('right') or ccircle.isKeyDown('left') :
            self.countdown += dt
        if self.countdown >= 1.25:
            self.count += 1
            self.countdown = 0
        if ccircle.isKeyDown('right'):
            self.x-=dt*25
        if ccircle.isKeyDown('left'):
            self.x+=dt*25
        if self.x <= -1024:
            self.x = 0
        if self.x >= 1024:
            self.x = 0
        '''


