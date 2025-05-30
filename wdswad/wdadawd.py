from direct.showbase.ShowBase import ShowBase
import math, sys, random


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.fighter = self.loader.loadModel('./Assets/sphere')
        self.fighter.reparentTo(self.render)
        self.fighter.setColorScale(1.0, 0.0, 0.0, 1.0)

        self.accept('escape', self.quit)

        self.parent = self.loader.loadModel("./Assets/cube")

        x = 0
        for i in range(100)
            theta = x
        self.placeholder2 = self.render.attachNewNode('Placeholder2')

    def quit(self):
        sys.exit()


app = MyApp()
app.run()