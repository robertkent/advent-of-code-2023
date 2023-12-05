import unittest

from almanac import Almanac

class TestAlmanac(unittest.TestCase):

    def test_get_lowest_location_from_list_of_seeds(self):
        self.assertEqual(Almanac('puzzleExample.txt').getLowestLocationNumber(), 35)

    def test_get_lowest_location_from_range_of_seeds(self):
        self.assertEqual(Almanac('puzzleExample.txt', True).getLowestLocationNumber(), 46)

if __name__ == '__main__':
    unittest.main()