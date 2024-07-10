import re


class Game:
    def guess(self, guessNumber):
        if guessNumber is None:
            raise TypeError
        if len(guessNumber) != 3:
            raise TypeError
        if re.search(r"\D", guessNumber):
            raise TypeError

        if guessNumber[0] == guessNumber[1] or \
                guessNumber[0] == guessNumber[2] or \
                guessNumber[1] == guessNumber[2]:
            raise TypeError