class Bush:
    def __init__(self,x,y,size,color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self,window):
        window.drawCircle(self.x,self.y,self.size,0.3,self.color,0.3,0.5)

    def update(self, dt,x,y):
        pass