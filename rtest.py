import unittest
import rtriangle

class TestTriangle(unittest.TestCase):

    def setUp(self):
        pass

    def testRT(self):
        self.assertAlmostEqual(rtriangle.RtriangleProvider)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()