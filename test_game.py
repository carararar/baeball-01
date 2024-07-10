from unittest import TestCase

from game import Game


class TestBaseball(TestCase):
    def test_baseball_when_input_is_none(self):
        self.game = Game()
        with self.assertRaises(TypeError):
            self.game.guess(None)

