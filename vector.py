class Vector_1:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(p1, p2):
        x1 = p1.x
        y1 = p1.y

        x2 = p2.x
        y2 = p2.y

        x_koord = x1 + x2
        y_koord = y1 + y2
        return x_koord, y_koord


    def len(self, x_koord, y_koord):
        length = (x_koord**2 + y_koord**2) ** 0.5
        print(length)

    def __del__(self):
        pass

