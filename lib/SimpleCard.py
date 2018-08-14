from math import floor
from lib.SimpleLogger import * 
import sys

class SimpleCard(object):
    '''
    attribute:
        self.rank
        self.suit
        self.image
        self.info
        self.serial
        self.rankSerial
        self.suitSerial
    '''

    def __init__(self, card):
        def _short_str_suit_to_serial(_suit):
            table = {
                'S': 0,
                'H': 1,
                'D': 2,
                'C': 3,
            }
            try:
                return table[_suit]
            except:
                return -1

        def _short_str_rank_to_serial(_rank):
            table = {
                'A': 1,
                'K': 13,
                'Q': 12,
                'J': 11,
                'T': 10,
            }
            try:
                return int(_rank)
            except:
                return table[_rank]
        def _split_card_serial(_card):
            _t = _card - 1
            return (_t % 13) + 1, floor(_t / 13)

        def _get_info(_rank, _suit):
            table_rank = {
                1: 'A',
                13: 'K',
                12: 'Q',
                11: 'J',
                10: 'T',
            }
            
            table_suit = {
                0: 'S',
                1: 'H',
                2: 'D',
                3: 'C',
            }

            s_rank = ''

            if _rank == 1 or _rank in range(10,14):
                s_rank = table_rank[_rank]
            else:
                s_rank = str(_rank)

            return s_rank + table_suit[_suit]
        
        def _get_image():
            table = {
                0: '♠',
                1: '♥',
                2: '♦',
                3: '♣',
            }

            _suit = self.suitSerial
            _image = table[self.suitSerial]
            if _suit == 0:
                if self.rankSerial == 12:
                    return '\033[4;44m[{}{}]\x1b[0m'.format(self.rank, _image)
                else:
                    return '\033[1;44m[{}{}]\x1b[0m'.format(self.rank, _image)
            elif _suit == 1:
                return '\033[1;41m[{}{}]\x1b[0m'.format(self.rank, _image)
            elif _suit == 2:
                return '\033[1;45m[{}{}]\x1b[0m'.format(self.rank, _image)
            else:
                return '\033[1;46m[{}{}]\x1b[0m'.format(self.rank, _image)


        def _get_rank():
            table = {
                1: 'A',
                13: 'K',
                12: 'Q',
                11: 'J',
                10: 'T',
            }

            if self.rankSerial == 1 or self.rankSerial in range(10, 14):
                return table[self.rankSerial]
            else:
                return str(self.rankSerial)

        def _get_suit():
            table = {
                0: 'spade',
                1: 'heart',
                2: 'diamond',
                3: 'club',
            }

            return table[self.suitSerial]
            
        try:
            if type(card) == str:
                self.info = card
                self.rankSerial = _short_str_rank_to_serial(card[0])
                self.suitSerial = _short_str_suit_to_serial(card[1])
                self.serial = self.rankSerial + 13 * self.suitSerial
            else:
                self.serial = card
                self.rankSerial, self.suitSerial = _split_card_serial(card)
                self.info = _get_info(self.rankSerial, self.suitSerial)
        except:
            logger('ERROR', 'Cannot set card info in SimpleCard')
            #logger('ERROR', sys.exec_info()[0])
            raise

        self.suit = _get_suit()
        self.rank = _get_rank() # all string
        self.image = _get_image()
