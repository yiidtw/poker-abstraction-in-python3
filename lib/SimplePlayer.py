#from lib.SimpleHand import SimpleHand
from lib.SimpleCardSet import SimpleCardSet
from lib.SimpleCard import SimpleCard
import random

class SimplePlayer(object):
    '''
        self.score
        self.isFirstHand
        self.position
        self.order
        self.hand
        self.stack
        self.isBot
    '''
    def __init__(self, position=-1, cards=[]):
        self.hands = SimpleCardSet(cards)
        self.stacks = SimpleCardSet()
        self.position = position
        self.isFirstHand = True
        self.score = 0
        self.order = 0
        self.isBot = True

    def receive_cards(self, cards=[]):
        self.hands.add(cards)

    def receive_score(self):
        pass

    def receive_stack(self, stacks=[]):
        pass

    def play(self):
        def pick_random_card(cards):
            ranks = []
            for c in cards:
                ranks.append(c.serial)
            random.shuffle(ranks)
            return ranks[0]

        if self.isBot:
            pickedSerial = pick_random_card(self.hands.cardset)
            cards = self.hands.give(pickedSerial)
            card = cards[0]
            return card
        else:
            pass
