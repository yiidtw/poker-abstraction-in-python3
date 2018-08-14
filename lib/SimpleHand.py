from lib.SimpleCard import SimpleCard
from lib.SimpleLogger import * 
from lib.SimpleLogger import logger
import sys

class SimpleHand(object):
    '''
    attribute:
        self.hands
        self.handCount
        self.images

    function:
        self.add
        self.give
    '''
    def __init__(self, cardList=[]):
        try:
            self.hands = []
            if cardList:
                for c in cardList:
                    self.hands.append(SimpleCard(c))
        except:
            logger('ERROR', 'Cannot set hand in SimpleHand')
            #logger('ERROR', sys.exec_info()[0])
            raise
        self._sort_hand()
            
    def _set_hand_images(self):
        images = ''
        for h in self.hands:
            images = images + h.image
        return images

    def _sort_hand(self):
        if self.hands:
            ranks = [card.serial for card in self.hands]
            ranks.sort()
            hands = []
            for r in ranks:
                hands.append(SimpleCard(r))
    
            self.hands = hands
            self.handCount = len(self.hands)
            self.images = self._set_hand_images()
        else:
            self.images = []
            self.handCount = 0

    def add(self, cards):
        if not type(cards) == list:
            cards = [cards]
        for c in cards:
            self.hands.append(SimpleCard(c))
        self._sort_hand()

    def give(self, cards):
        if not type(cards) == list:
            cards = [cards]

        res = []
        scs = [SimpleCard(c) for c in cards]
        for sc in scs:
            for sh in self.hands:
                if sh.serial == sc.serial:
                    self.hands.remove(sh)
                    res.append(sc)

        self._sort_hand()
        return res
