import unittest

from calculator import Calculate

class TestCalibrations(unittest.TestCase):
    def test_first(self):
        self.assertEqual(Calculate.getCalibration("3fiveone"), 31)
    def test_single_digit(self):
        self.assertEqual(Calculate.getCalibration("9g"), 99)
    def test_annoying_edge_case(self):
        self.assertEqual(Calculate.getCalibration("679one9nzsktvfseighteightwotjm"), 62)

if __name__ == '__main__':
    unittest.main()