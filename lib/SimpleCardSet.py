from lib.SimpleCard import SimpleCard
from lib.SimpleLogger import * 
from lib.SimpleLogger import logger

class SimpleCardSet(object):
    '''
    attribute:
        self.cardset
        self.serialset
        self.handCount
        self.images

    function:
        self.add
        self.give
    '''
    def __init__(self, cardset=[]):
        try:
            self.hasClub2 = False
            self.hasSpadeQ = False
            self.cardset = []
            self.serialset = []
            if cardset:
                for c in cardset:
                    self.cardset.append(SimpleCard(c))
                    self.serialset.append(SimpleCard(c).serial)
        except:
            logger('ERROR', 'Cannot set hand in SimpleHand')
            raise
        self._sort_hand()
            
    def _set_hand_images(self):
        images = ''
        for h in self.cardset:
            images = images + h.image
        return images

    def _sort_hand(self):
        def hasClub2():
            return True if 41 in self.serialset else False
        def hasSpadeQ():
            return True if 12 in self.serialset else False
            
        if self.cardset:
            ranks = [card.serial for card in self.cardset]
            ranks.sort()

            hands = []
            for r in ranks:
                hands.append(SimpleCard(r))
    
            self.serialset = ranks
            self.cardset = hands
            self.handCount = len(self.cardset)
            self.images = self._set_hand_images()

            self.hasClub2 = hasClub2()
            self.hasSpadeQ = hasSpadeQ()
        else:
            self.images = []
            self.handCount = 0
            self.serialset = []

    def add(self, cards):
        if not type(cards) == list:
            cards = [cards]
        for c in cards:
            self.cardset.append(SimpleCard(c))
        self._sort_hand()

    def give(self, cards):
        if not type(cards) == list:
            cards = [cards]

        res = []
        scs = [SimpleCard(c) for c in cards]
        for sc in scs:
            for sh in self.cardset:
                if sh.serial == sc.serial:
                    self.cardset.remove(sh)
                    res.append(sc)

        self._sort_hand()
        return res
