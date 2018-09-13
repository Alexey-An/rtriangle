'''
Перед запуском установить  Python 3.5.0 или выше.
Тест запускается из командной строки:
python3 -m unittest -v rtest.py
или просто
python -m unittest -v rtest.py (в зависимости от настроек системы)
'''


import unittest
import rtriangle

class TestTriangle(unittest.TestCase):

    def setUp(self):
        pass


# С точки зрения математики проверка основывается на вычислении скалярного произведения, вычисление которого
# используется для генерации прямоугольного треугольника в методе getRtriangle(). Наверное, было бы правильно
# реализовать разные алгоритмы...

    def testRT(self):
        self.X1, self.X2, self.X3, self.Y1, self.Y2, self.Y3 = rtriangle.RtriangleProvider.getRtriangle(self)
        self.dp1 = ((self.X2 - self.X1) * (self.X3 - self.X1) + (self.Y2 - self.Y1) * (self.Y3 - self.Y1))
        self.dp2 = ((self.X1 - self.X2) * (self.X3 - self.X2) + (self.Y1 - self.Y2) * (self.Y3 - self.Y2))
        self.dp3 = ((self.X1 - self.X3) * (self.X2 - self.X3) + (self.Y1 - self.Y3) * (self.Y2 - self.Y3))
        self.assertTrue(self.dp1 == 0 or self.dp2 == 0 or self.dp3 == 0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

