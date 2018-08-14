from lib.SimplePlayer import SimplePlayer
import random

class SimpleDeck(object):
    def __init__(self):
        self.playerList = []
        for i in range(4):
            self.playerList.append(SimplePlayer(i))
        self.roundNumber = 0
        self.setNumber =0
        self.playingOrder = list(range(4))

    def deal(self):
        arr =  list(range(1,53))
        random.shuffle(arr)
        self.playerList[0].receive_cards(arr[0:13])
        self.playerList[1].receive_cards(arr[13:26])
        self.playerList[2].receive_cards(arr[26:39])
        self.playerList[3].receive_cards(arr[39:52])
        
    def run(self):
        for i in range(4):
            card = self.playerList[self.playingOrder[i]].play()
            print(card.image)
