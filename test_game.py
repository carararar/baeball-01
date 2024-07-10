from unittest import TestCase

from game import Game


class TestBaseball(TestCase):
    def setUp(self):
        self.game = Game()
        super().setUp()

    def assert_illegal_argument(self, guessNumber):
        try:
            self.game.guess(guessNumber)
            self.fail()
        except TypeError:
            pass


    def test_game_should_raise_exception_when_invalid_input(self):
        self.assert_illegal_argument(None)
        self.assert_illegal_argument("12")
        self.assert_illegal_argument("1234")
        self.assert_illegal_argument("12a")
        self.assert_illegal_argument("121")

    def test_game_should_return_solve_result_when_matched_input(self):
        self.game.question = "123"
        result: GameResult = self.game.guess("123")
        self.assertIsNotNone(result)
        self.assertTrue(result.solved)
        self.assertEqual(3, result.strikes)
        self.assertEqual(0, result.balls)