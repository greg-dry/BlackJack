import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Ace','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank, suit))
                
    def shuffle(self):
        random.shuffle(self.all_cards)

    def remove_card(self):
        return self.all_cards.pop(0)   

class Player(Deck):
    def __init__(self, name, balance = 100):
        self.name = name
        self.balance = balance
        self.my_cards = []

    def __str__(self):
        return f"{self.name} has ${self.balance}."

    def hit(self, new_card):
        self.my_cards.append(new_card)


mydeck = Deck()
myplayer = Player('Greg')
mydeck.shuffle()
#should be 52
print(len(mydeck.all_cards))
#Display top card of the deck
print(mydeck.all_cards[0])
#Take off top card from deck and assign to variable
top_card = mydeck.remove_card()
#check the next top card of deck
print(mydeck.all_cards[0])
#new number should be 51
print(len(mydeck.all_cards))
#add card from deck to player deck
myplayer.hit(top_card)
#this card should == the top card of deck
print(myplayer.my_cards[0])
#check length of my deck, should be 1
print(len(myplayer.my_cards))





