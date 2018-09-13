import random


class RTriangle():
    def getApexX1(self):
        return self.X1
    def getApexX2(self):
        return self.X2
    def getApexX3(self):
        return self.X3
    def getApexY1(self):
        return self.Y1
    def getApexY2(self):
        return self.Y2
    def getApexY3(self):
        return self.Y3


class RtriangleProvider(RTriangle):

    def getRtriangle(self):

        def getApexX1():
            X1 = random.randint(0, 10)
            return X1
        def getApexX2():
            X2 = random.randint(0, 10)
            return X2
        def getApexX3():
            X3 = random.randint(0, 10)
            return X3
        def getApexY1():
            Y1 = random.randint(0, 10)
            return Y1
        def getApexY2():
            Y2 = random.randint(0, 10)
            return Y2
        def getApexY3():
            Y3 = random.randint(0, 10)
            return Y3

        while True:

            X1 = getApexX1()
            X2 = getApexX2()
            X3 = getApexX3()
            Y1 = getApexY1()
            Y2 = getApexY2()
            Y3 = getApexY3()

            '''Скалярное произведение взаимно перпендикулярных векторов равно нулю.'''

            dotP1 = ((X2 - X1) * (X3 - X1) + (Y2 - Y1) * (Y3 - Y1))
            dotP2 = ((X1 - X2) * (X3 - X2) + (Y1 - Y2) * (Y3 - Y2))
            dotP3 = ((X1 - X3) * (X2 - X3) + (Y1 - Y3) * (Y2 - Y3))

            print(X1, X2, X3, Y1, Y2, Y3)
            print(dotP1, dotP2, dotP3)

            if not (dotP1 != 0 and dotP2 != 0 and dotP3 != 0):
                break
        return X1, X2, X3, Y1, Y2, Y3


if __name__ == '__main__':

    newTriangle = RtriangleProvider()
    newTriangle.getRtriangle()




