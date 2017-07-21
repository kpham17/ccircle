import ccircle
import Util
import random
class moves:
    def __init__(self,x,y,m1,m2,k1,k2,ex,ek1,ek2):
        self.x = x
        self.y = y
        self.m1 = m1
        self.m2 = m2
        self.k1 = k1
        self.k2 = k2
        self.ek1 = ek1
        self.ek2 = ek2
        self.countdown1 = 0
        self.countdown2 = 0
        self.weapons= ccircle.Image('Weapons.png')
        self.ly = 0
        self.a = 0
        self.hit = 0
        self.attack = ccircle.Image('Attack.png')
        self.fa  = ccircle.Font('Broadview Regular.ttf')
        self.da = []
        self.dl  =[]
        self.eh = 200
        self.mt1 = 1
        self.mt2 = 1
        self.ex = ex
        self.shield = False


    def draw(self,window,m1,m2):

        window.drawRect(self.x , self.y - 90, 68, 68, 1, .843, 0)
        window.drawRect(self.x+4,self.y-86,60,60,0,0,0)

        window.drawRect(self.x, self.y, 68, 68, 1, .843, 0)
        window.drawRect(self.x + 4, self.y + 4, 60, 60, 0, 0, 0)

        for i in range(8):
            if i<4:
                self.ly = 0
                self.a = i
            else:
                self.ly = 47
                self.a = i-4
            if m1 == i:
                self.weapons.drawSub(self.x, self.y - 90, 69, 69, 47*self.a -(self.a-1), self.ly, 46, 46)
            if m2 == i:
                self.weapons.drawSub(self.x, self.y, 69, 69, 47*self.a -(self.a-1), self.ly, 46, 46)

        if self.hit > 0 and len(self.da) != 0:
            self.attack.draw(self.ex, 340, 90, 90)
            for i in range(len(self.da)):
                self.dl.append([random.randint(15, 75), random.randint(15, 90)])
            for i in range(len(self.da)):
                if self.shield:
                    self.fa.drawCentered(str(self.da[i]*1/2), self.ex + self.dl[i][0], 330 + self.dl[i][1], 11, 0.1, 0.5, 0.5)
                    self.fa.drawCentered(str(self.da[i]*1/2), self.ex + self.dl[i][0], 330 + self.dl[i][1], 8, 0.2, 1, 1)
                    self.shield = False

                else:
                    self.fa.drawCentered (str(self.da[i]),self.ex + self.dl[i][0],330 + self.dl[i][1], 11,0.1,0.5,0.5)
                    self.fa.drawCentered (str(self.da[i]),self.ex + self.dl[i][0],330 + self.dl[i][1], 8,0.2,1,1)

        if self.eh < 0:
            self.eh = 0
        window.drawRect(955 - self.x, 250,50,200,0,0,0)
        window.drawRect(955 - self.x, 250, 50, self.eh, 0, 1, 0)
        window.drawRect(self.x+4,self.y-86,60,60 *self.countdown1/self.mt1,1,1,1,0.5)
        window.drawRect(self.x+4,self.y+4,60,60 *self.countdown2/self.mt2,1,1,1,0.5)


    def if_clicked(self,ex,m1,m2):
        if ccircle.wasKeyPressed(self.k1) and self.countdown1 <= 0:
            self.hit = 3.5
            self.dl = []
            self.da = []
            if m1 == 0 and ex<200:
                self.da = [random.randint(20,30)]
                self.countdown1 = 6
                self.mt1 = 6
            elif m1 == 1 and ex<200:
                self.da = [random.randint(30,40)]
                self.countdown1 = 10
                self.mt1 = 7
            elif m1 == 2 and ex<600:
                for i in range(3):
                    self.da.append(random.randint(0,12))
                self.countdown1 = 6
                self.mt1 = 5
            elif m1 == 3and ex<400:
                for i in range(5):
                    self.da.append(random.randint(0, 7))
                self.countdown1 = 7
                self.mt1 = 6
            elif m1 == 4:
                self.countdown1 = 20
                self.mt1 = 20
                self.shield = True
            elif m1 == 5 and ex<250:
                self.da = [random.randint(25,35)]
                self.countdown1 = 8
                self.mt1 = 8
            elif m1 == 6 and ex<100:
                self.da = [random.randint(40,50)]
                self.countdown1 = 15
                self.mt1 = 15
            elif m1 == 7 and ex<400:
                self.da =[22]
                self.countdown1 = 6
                self.mt1 = 6
            self.eh -= sum(self.da)

        if ccircle.wasKeyPressed(self.k2) and self.countdown2 <= 0:
            self.hit = 2
            self.da = []
            self.dl = []
            self.store = True
            if m2 == 0and ex<200:
                self.da = [random.randint(20, 30)]
                self.countdown2 = 6
                self.mt2 = 6
            elif m2 == 1and ex<200:
                self.da = [random.randint(30, 40)]
                self.countdown2 = 10
                self.mt2 = 7
            elif m2 == 2and ex<600:
                for i in range(3):
                    self.da.append(random.randint(0, 12))
                self.countdown2 = 5
                self.mt2 = 5
            elif m2 == 3and ex<400:
                for i in range(5):
                    self.da.append(random.randint(0, 7))
                self.countdown2 = 6
                self.mt2 = 6
            elif m2 == 4:
                self.countdown2 = 20
                self.mt2 = 20
                self.shield = True
            elif m2 == 5 and ex<250:
                self.da = [random.randint(25, 35)]
                self.countdown2 = 8
                self.mt2 = 6
            elif m2 == 6 and ex<100:
                self.da = [random.randint(40, 50)]
                self.countdown2 = 15
                self.mt2 = 15
            elif m2 == 7and ex<400:
                self.da = [22]
                self.countdown2 = 7
                self.mt2 = 7
            self.eh -= sum(self.da)

    def update(self, dt):
        self.countdown1 -=dt
        self.countdown2 -=dt
        if self.countdown1<0:
            self.countdown1 = 0
        if self.countdown2<0:
            self.countdown2 = 0
        self.hit -= dt

        if ccircle.isKeyDown(self.ek2):
            self.ex += dt * 25
        if ccircle.isKeyDown(self.ek1):
            self.ex -= dt * 25
        if self.ex > 940:
            self.ex = 940
        if self.ex < 100:
            self.ex = 100
