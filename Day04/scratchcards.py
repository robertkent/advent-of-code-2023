import re

class Card:

    points = 0
    numberOfCards = 1

    def __init__(self, numbers: [], winners: []) -> None:
        self.numbers = set(numbers)
        self.winners = set(winners)
        self.calculatePoints()

    def calculatePoints(self):
        for match in self.numbers.intersection(self.winners):
            if self.points == 0:
                setattr(self, 'points', 1)
            else: 
                setattr(self, 'points', self.points + self.points)

    def calculateWinningFollowingCards(self):
        return len(self.numbers.intersection(self.winners))

    def addCopyOfCard(self):
        setattr(self, 'numberOfCards', self.numberOfCards + 1)
    
    @property
    def getPoints(self):
        return self.points
    
    @property
    def getNumberOfCards(self):
        return self.numberOfCards
    


class ScratchCards:
    def __init__(self, input: str, newRules = False) -> None:
        self.cards = []
        self.newCardRules = []
        self.newRules = newRules
        self.input = input.split('\n')
        self.setup()
        if self.newRules:
            self.setupNewRules()

    def setup(self):
        for line in self.input:
            # get the card number - the numbers on card and the winning values
            cardNumbers, cardWinners = self.getNumberLists(line)
            self.cards.append(Card(cardNumbers, cardWinners))

    def getNumberLists(self, line):
        cp = line.split(':')
        cn = cp[1].strip().split('|')
        cardNumbers = [x for x in cn[0].strip().split(' ') if x != '']
        cardWinners = [x for x in cn[1].strip().split(' ') if x != '']

        return (cardNumbers, cardWinners)

    def setupNewRules(self):
        for line in self.input:
            cardNumbers, cardWinners = self.getNumberLists(line)
            self.newCardRules.append(Card(cardNumbers, cardWinners))

        idx = 0
        for card in self.newCardRules:
            for run in range(card.numberOfCards):
                winners = card.calculateWinningFollowingCards()
                if winners:
                    self.addCopiesToCards(idx, winners)
            idx += 1



    def addCopiesToCards(self, idx, winners):
        for i in range(winners):
            i = i + 1
            if idx + i < len(self.newCardRules):
                self.newCardRules[idx + i].addCopyOfCard()

    def checkCards(self):
        return self.newCardRules if self.newCardRules else self.cards
    
    def calculateTotalPoints(self):
        sum = 0
        for card in self.cards:
            sum += card.getPoints

        return sum
    
    def totalNumberOfCards(self):
        sum = 0
        for card in self.newCardRules:
            sum += card.getNumberOfCards

        return sum
    

class GetCards:
    def runGame():
        input = ""
        f = open('puzzleInput.txt', 'r')
        for x in f:
            input += x

        print(ScratchCards(input).calculateTotalPoints())
        print(ScratchCards(input, True).totalNumberOfCards())

if __name__ == '__main__':
    GetCards.runGame()