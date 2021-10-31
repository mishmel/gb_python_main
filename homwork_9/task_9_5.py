class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start rendering')

class Pen(Stationery):

    def draw(self):
        print('Writes with black paste')


class Pencil(Stationery):

    def draw(self):
        print('Draws a thin line')


class Handle(Stationery):

    def draw(self):
        print('Draws a thick line')

stationery = Stationery('feather')
pen = Pen('parker')
pencil = Pencil('kooh_i_noor')

stationery.draw()
pen.draw()
pencil.draw()