class World:
    def __init__(self,name):
        self.name = name
        self.objects=[]

    def add(self, obj):
        self.objects.append(obj)

    def draw(self,window):
        for obj in self.objects:
            obj.draw(window)

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)