import unittest
from scratchcards import ScratchCards

example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

part_two = """Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3: 1 21 53 59 44 | 69 82 63 72 16 21 14 1
Card 4: 41 92 73 84 69 | 59 84 76 51 58 5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

class TestScratchCards(unittest.TestCase):
    def test_winning_line(self):
        cards = ScratchCards(example).checkCards()
        self.assertEqual(cards[0].getPoints, 8)
        self.assertEqual(cards[1].getPoints, 2)
        self.assertEqual(cards[2].getPoints, 2)
        self.assertEqual(cards[3].getPoints, 1)
        self.assertEqual(cards[4].getPoints, 0)
        self.assertEqual(cards[5].getPoints, 0)

    def test_total_points(self):
        self.assertEqual(ScratchCards(example).calculateTotalPoints(), 13)

    def test_total_number_of_different_cards(self):
        cards = ScratchCards(example, True).checkCards()
        self.assertEqual(cards[0].getNumberOfCards, 1)
        self.assertEqual(cards[1].getNumberOfCards, 2)
        self.assertEqual(cards[2].getNumberOfCards, 4)
        self.assertEqual(cards[3].getNumberOfCards, 8)
        self.assertEqual(cards[4].getNumberOfCards, 14)
        self.assertEqual(cards[5].getNumberOfCards, 1)

    def test_total_number_of_cards(self):
        self.assertEqual(ScratchCards(example, True).totalNumberOfCards(), 30)

if __name__ == '__main__':
    unittest.main()