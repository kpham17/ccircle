import math


class Ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vx = 0
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
        a = self.x - x
        b = self.y - y
        if a == 0:
            self.vx *= -1.2
        elif 0 < abs(a) <= 2:
            self.vx *= -2 / (2*a)
        if b == 0:
            self.vy *= -1.2
        elif 0 < abs(b) <= 2:
            self.vy *= -2 / (2*b)
        if self.y > 500 or self.y < 0:
            self.vy *= -0.99
            self.y = 500
        if self.x > 800 or self.x < 0:
            self.vx *= -0.99






