from direct.showbase.ShowBase import ShowBase
import math, sys, random

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.fighter = self.loader.loadModel('./Assets/sphere')
        self.fighter.reparentTo(self.render)
        self.fighter.setColorScale(1.0, 0.0, 0.0, 1.0)
        self.set_background_color(0,0,0)

        self.accept('escape', self.quit)

        self.parent = self.loader.loadModel("./Assets/cube")

        x = 0 # use position of circle as center
        for i in range(100):
            theta = x
            self.placeholder2 = self.render.attachNewNode('Placeholder2') # put in the renderer
            self.placeholder2.setPos(50.0 * math.cos(theta), 50.0 * math.sin(theta), 0.0 * math.tan(theta))
            red = 0.6 + random.random() * 0.4
            green = 0.6 + random.random() * 0.4
            blue = 0.6 + random.random() * 0.4
            self.placeholder2.setColorScale(red, green, blue, 1.0)
            self.parent.instanceTo(self.placeholder2)
            x = x + 0.06 # adds incrementing spacing 

    def quit(self):
        sys.exit()

app = MyApp()
app.run()