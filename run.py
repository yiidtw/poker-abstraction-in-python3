from lib.SimpleCardSet import SimpleCardSet
from lib.SimpleCard import SimpleCard
from lib.SimpleLogger import logger
from lib.SimpleDeck import SimpleDeck
from lib.SimpleLogger import logger

if __name__ == '__main__':
    deck = SimpleDeck()
    deck.deal()
    for player in deck.playerList:
        logger('INFO', 'Player @ Position %d received' % player.position)
        print(' %s' % player.hands.images)
        print('')

#    for i in range(1, 53):
#        card = SimpleCard(i)
#        print(('%d %s %s') % (card.serial, card.info, card.image))
