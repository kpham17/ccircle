import ccircle
import random
class moves:
    def __init__(self,x,y,m1,m2):
        self.x = x
        self.y = y
        self.m1 = m1
        self.m2 = m2
        self.countdown = 0
        self.weapons= ccircle.Image('Weapons.png')

    def draw(self,window):
        window.drawRect(self.x , self.y - 90, 68, 68, 1, .843, 0)
        window.drawRect(self.x+4,self.y-86,60,60,0,0,0)

        window.drawRect(self.x, self.y, 68, 68, 1, .843, 0)
        window.drawRect(self.x + 4, self.y + 4, 60, 60, 0, 0, 0)

        if self.m1 == 0:
            self.weapons.drawSub(self.x, self.y - 90, 69, 69, 0, 0, 46, 46)
        elif self.m1 == 1:
            self.weapons.drawSub(self.x, self.y - 90, 69, 69, 47, 0, 46, 46)
        elif self.m1 == 2:
            self.weapons.drawSub(self.x, self.y - 90, 69, 69, 93, 0, 46, 46)
        elif self.m1 == 3:
            self.weapons.drawSub(self.x, self.y - 90, 69, 69, 139, 0, 46, 46)
        elif self.m1 == 4:
            self.weapons.drawSub(self.x, self.y - 90, 69, 69, 0, 47, 46, 46)
        elif self.m1 == 5:
            self.weapons.drawSub(self.x, self.y - 90, 69, 69, 47, 47, 46, 46)
        elif self.m1 == 6:
            self.weapons.drawSub(self.x, self.y - 90, 69, 69, 93, 47, 46, 46)
        elif self.m1 == 7:
            self.weapons.drawSub(self.x, self.y - 90, 69, 69, 139, 47, 46, 46)

        if self.m2 == 0:
            self.weapons.drawSub(self.x, self.y, 69, 69, 0, 0, 46, 46)
        elif self.m2 == 1:
            self.weapons.drawSub(self.x, self.y, 69, 69, 47, 0, 46, 46)
        elif self.m2 == 2:
            self.weapons.drawSub(self.x, self.y, 69, 69, 93, 0, 46, 46)
        elif self.m2 == 3:
            self.weapons.drawSub(self.x, self.y, 69, 69, 139, 0, 46, 46)
        elif self.m2 == 4:
            self.weapons.drawSub(self.x, self.y, 69, 69, 0, 47, 46, 46)
        elif self.m2 == 5:
            self.weapons.drawSub(self.x, self.y, 69, 69, 47, 47, 46, 46)
        elif self.m2 == 6:
            self.weapons.drawSub(self.x, self.y, 69, 69, 93, 47, 46, 46)
        elif self.m2 == 7:
            self.weapons.drawSub(self.x, self.y, 69, 69, 139, 47, 46, 46)

    def if_clicked(self, mx,my):
        if self.x<mx<self.x+69:
            if self.y-90< my <self.y<21:
                if self.m1 == 0:
                    print(random.randint(10,20))


    def update(self, dt):
        pass
