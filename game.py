import re

from game_result import GameResult


class Game:
    def __init__(self) -> None:
        super().__init__()
        self.question = ""
    def guess(self, guessNumber) -> GameResult:
        self.assert_illegal_value(guessNumber)
        return GameResult(True, 3, 0)

    def assert_illegal_value(self, guessNumber):
        if guessNumber is None:
            raise TypeError
        if len(guessNumber) != 3:
            raise TypeError
        if re.search(r"\D", guessNumber):
            raise TypeError
        if self.is_duplicated_number(guessNumber):
            raise TypeError

    def is_duplicated_number(self, guessNumber):
        return guessNumber[0] == guessNumber[1] or \
            guessNumber[0] == guessNumber[2] or \
            guessNumber[1] == guessNumber[2]