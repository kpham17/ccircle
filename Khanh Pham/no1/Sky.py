class Cloud:
    def __init__(self,x,y,size,color,vx):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.vx = vx

    def draw(self,window):

        window.drawCircle(self.x,self.y,self.size,self.color,self.color,self.color,0.25)

    def update(self,dt,x,y):
        self.x += dt*self.vx
        if self.x > 800: self.x = 0
        if self.x < 0: self.x = 800