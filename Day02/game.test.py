import unittest

from game import GameEvaluator

testGame = { 
    "game": 1, 
    "draws": [
        { 
            "colors": {
                "blue": 2,
                "green": 1,
                "red": 5
            },
            "possible": True
        },
        { 
            "colors": {
                "blue": 8,
                "green": 2,
                "red": 6
            },
            "possible": True
        },
        { 
            "colors": {
                "blue": 3,
                "green": 2,
                "red": 8
            },
            "possible": True
        },
        { 
            "colors": {
                "blue": 19,
                "green": 1,
                "red": 6
            },
            "possible": False
        },
        { 
            "colors": {
                "blue": 17,
                "red": 1
            },
            "possible": False
        }
    ],
    "power": 304
}

cubeLimits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

class TestCalibrations(unittest.TestCase):
    def test_line(self):
        self.maxDiff = None
        self.assertDictEqual(GameEvaluator.parseLine(
                "Game 1: 5 red, 1 green, 2 blue; 2 green, 8 blue, 6 red; 8 red, 3 blue, 2 green; 6 red, 1 green, 19 blue; 1 red, 17 blue"
            ), testGame
        )

    def test_if_possible_with_cube_limits_single_draws(self):
        self.assertFalse(GameEvaluator.isGamePossibleWithLimits(
                {
                    "blue": 19,
                    "green": 1,
                    "red": 6
                }
            )
        )

        self.assertTrue(GameEvaluator.isGamePossibleWithLimits(
                {
                    "blue": 5,
                    "green": 1,
                    "red": 6
                }
            )
        )

    def test_power_of_single_set(self):
        self.assertEqual(GameEvaluator.parseLine("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")['power'], 48)

        self.assertEqual(
            GameEvaluator.parseLine("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")['power'], 12)

        self.assertEqual(
            GameEvaluator.parseLine("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")['power'], 1560)

        self.assertEqual(
            GameEvaluator.parseLine("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")['power'], 630)

        self.assertEqual(
            GameEvaluator.parseLine("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")['power'], 36)
        
    def test_correct_answer_for_powers(self):
        self.assertEqual(
            GameEvaluator.totalProductsOfCubes([testGame]), 304)

if __name__ == '__main__':
    unittest.main()