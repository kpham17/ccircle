import ccircle
import random
class moves:
    def __init__(self,x,y,m1,m2):
        self.x = x
        self.y = y
        self.m1 = m1
        self.m2 = m2
        self.countdown1 = 0
        self.countdown2 = 0
        self.weapons= ccircle.Image('Weapons.png')
        self.lg = 0
        self.lf = 0

    def draw(self,window):
        window.drawRect(self.x , self.y - 90, 68, 68, 1, .843, 0)
        window.drawRect(self.x+4,self.y-86,60,60,0,0,0)

        window.drawRect(self.x, self.y, 68, 68, 1, .843, 0)
        window.drawRect(self.x + 4, self.y + 4, 60, 60, 0, 0, 0)

        for i in range(8):
            if i < 4:
               self.lg = 90
               self.lf = 0
            elif i >= 4:
                self.lg  = 0
                self.lf = 47
            if self.m1 == i:
                self.weapons(self.x,self.y - self.lg,69,69,47*i - (i+1),self.lf,46,46)
        for i in range(8):
            if i < 4:
               self.lg = 90
               self.lf = 0
            elif i >= 4:
                self.lg  = 0
                self.lf = 47
            if self.m2 == i:
                self.weapons(self.x,self.y - self.lg,69,69,47*i - (i+1),self.lf,46,46)



    def if_clicked(self, mx,my):
        if self.x<mx<self.x+69:
            if self.y-90< my < self.y - 21:
                if self.m1 == 0 and self.countdown1 <= 0:
                    print(random.randint(20,30))
                    self.countdown1 = 6
                elif self.m1 == 1and self.countdown1 <= 0:
                    print(random.randint(30,40))
                    self.countdown1 = 7
                elif self.m1 == 2and self.countdown1 <= 0:
                    for i in range(3):
                        print(random.randint(0,10))
                    self.countdown1 = 5
                elif self.m1 == 3and self.countdown1 <= 0:
                    for i in range(5):
                        print(random.randint(0, 7))
                    self.countdown1 = 6
                elif self.m1 == 4and self.countdown1 <= 0:
                    self.countdown1 = 20
                elif self.m1 == 5 and self.countdown1 <= 0:
                    print(random.randint(25,35))
                    self.countdown1 = 6
                elif self.m1 == 6 and self.countdown1 <= 0:
                    print(random.randint(40,50))
                    self.countdown1 = 15
                elif self.m1 == 7 and self.countdown1 <= 0:
                    print(22)
                    self.countdown1 = 6
            if self.y< my < self.y +69:
                if self.m2 == 0 and self.countdown2 <= 0:
                    print(random.randint(20, 30))
                    self.countdown2 = 5
                elif self.m2 == 1 and self.countdown2 <= 0:
                    print(random.randint(30, 40))
                    self.countdown2 = 7
                elif self.m2 == 2 and self.countdown2 <= 0:
                    for i in range(3):
                        print(random.randint(0, 10))
                    self.countdown2 = 5
                elif self.m2 == 3 and self.countdown2 <= 0:
                    for i in range(5):
                        print(random.randint(0, 7))
                    self.countdown2 = 6
                elif self.m2 == 4 and self.countdown2 <= 0:
                    self.countdown2 = 20
                elif self.m2 == 5 and self.countdown2 <= 0:
                    print(random.randint(25, 35))
                    self.countdown2 = 6
                elif self.m2 == 6 and self.countdown2 <= 0:
                    print(random.randint(40, 50))
                    self.countdown2 = 15
                elif self.m2 == 7 and self.countdown2 <= 0:
                    print(22)
                    self.countdown2 = 6

    def update(self, dt):
        self.countdown1 -=dt
        self.countdown2 -=dt
