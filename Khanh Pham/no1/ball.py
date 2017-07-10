class Ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vx = 200
        self.vy = 0
        self.fx = 0
        self.fy = 0
        self.mass  = 1
    def apply_force(self,fx,fy):
        self.fx+=fx
        self.fy+=fy

    def draw(self,window):

        window.drawCircle(self.x,self.y,16,1,0,0.2,1)

    def update(self,dt,x,y):
        accelX = self.fx/self.mass
        accelY = self.fy / self.mass
        self.vx += dt*accelX
        self.vy += dt*accelY
        self.x += dt * self.vx
        self.y += dt * self.vy
        self.fx =0
        self.fy = 0
        if self.y > 500:
            self.vy*=-0.99
            self.y = 500
        if self.x > 800 or self.x < 0:
            self.vx*=-0.99
        if self.y == y and self.x == x:
            self.vy*=-0.99

