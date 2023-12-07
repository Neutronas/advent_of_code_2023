from enum import Enum

class HandTypes(Enum):
    FiveOfAKind = 7
    FourofAKind = 6
    FullHouse = 5
    ThreeofAKind = 4
    TwoPair = 3
    OnePair = 2
    HighCard = 1

mappingOfStrength = {'A' : 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

class CardObject:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.hand = {}
        self.handType = 0
        self.findHandType()

    def findHandType(self):
        for card in self.cards:
            if card in self.hand:
                self.hand[card] += 1
            else:
                self.hand[card] = 1
        self.hand = sorted(self.hand.items(), key=lambda x:x[1], reverse=True)
        if(len(self.hand) == 5):
            self.handType = HandTypes.HighCard
        elif(len(self.hand) == 1):
            self.handType = HandTypes.FiveOfAKind
        elif(self.hand[0][1] == 4):
            self.handType = HandTypes.FourofAKind
        elif(self.hand[0][1] == 3 and self.hand[1][1] == 2):
            self.handType = HandTypes.FullHouse
        elif(self.hand[0][1] == 3):
            self.handType = HandTypes.ThreeofAKind
        elif(self.hand[0][1] == 2 and self.hand[1][1] == 2):
            self.handType = HandTypes.TwoPair
        else:
            self.handType = HandTypes.OnePair
                    


def read_input_file(file_path):
    objects_array = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split()
            cards = [line[0][i:i + 1] for i in range(0, len(line[0]), 1)]  # Split symbols into a list
            bid = int(line[1])
            card_object = CardObject(cards, bid)
            objects_array.append(card_object)

    return objects_array


input_file_path = "input.txt"
cards = read_input_file(input_file_path)
sortedByRank = []



def sortArrayByGivenIndex(array, idx):
    sortedArray = []
    for str in mappingOfStrength:
        strCardArray = []
        for card in array:
            if (str == card.cards[idx]):
                strCardArray.append(card)
        if len(strCardArray) == 1:
            sortedArray.append(strCardArray[0])
        elif len(strCardArray) > 1 and idx < 4:
            sortedArray += sortArrayByGivenIndex(strCardArray, idx + 1)
        elif(idx > 4):
            sortedArray = strCardArray
    return sortedArray
            



for s in HandTypes:
    cardsOfOneKind = []
    for card in cards:
        if card.handType == s:
            cardsOfOneKind.append(card)
    if len(cardsOfOneKind) > 1:
        cardsOfOneKind = sortArrayByGivenIndex(cardsOfOneKind, 0)
    if len(cardsOfOneKind) > 0:
        if(len(cardsOfOneKind) == 1):
            sortedByRank.append(cardsOfOneKind[0])
        else:
            sortedByRank += cardsOfOneKind


sum = 0
for i, card in enumerate(reversed(sortedByRank)):
    if sum == 0:
        sum = card.bid*(i+1)
    else:
        sum += card.bid*(i+1)
print(sum)

