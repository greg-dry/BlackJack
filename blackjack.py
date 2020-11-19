import random
import math
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

class Deck(Card):
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank, suit))
                
    def shuffle(self):
        random.shuffle(self.all_cards)

    def remove_card(self):
        return self.all_cards.pop(0) 

    #def add_hand(self, deck):
        #return sum(deck)

 

class Player(Deck, Card):
    def __init__(self, balance):
        self.balance = balance
        self.my_cards = []
        self.values = []


    def __str__(self):
        return f"You have ${self.balance}."

    def hit(self, new_card):
        self.my_cards.append(new_card)
        self.values.append(new_card.value)
        

    def make_a_bet(self):
        print(myplayer)
        while True:
            try:
                bet = int(input('Make a bet: '))
            except:
                print('invalid input')
            else:
                if bet > self.balance:
                    print('You do not have the funds in your balance to make that bet')
                else:
                    new_balance = self.balance - bet
                    print(f"You now have ${new_balance}")
                    break
    
   
                
        
        

'''
class Dealer(Deck):
    def __init__(self)

'''


mydeck = Deck()
myplayer = Player(balance = 100)


print('Welcome to BlackJack')
while True:
    try:
        play_choice = int(input("do you want to play? Enter 1 for Yes, 2 for No: "))
    except:
        print('Invalid answer')
    else:
        break

if play_choice == 1:
    print("Ok let's play!")
    game_on = True
else:
    print("Goodbye")
    game_on = False


def game_play():
    while game_on == True:
        myplayer.make_a_bet()
        break

    mydeck.shuffle()

    top_card = mydeck.remove_card()

    myplayer.hit(top_card)

    

    print(f"Your card is {myplayer.my_cards[0]}")
    #current_value = myplayer.my_cards[0].value
    #print(current_value)
    while True:
        try:
            hit_choice = int(input("Would you like to hit? Enter 1 for Yes, 2 for No: "))
        except: 
            print('invalid answer')
        else:
            if hit_choice == 1:
                top_card = mydeck.remove_card()
                myplayer.hit(top_card)
                print(f"Your card is {myplayer.my_cards[-1]}") 
                player_current_value = sum(myplayer.values)
                print('your current hand value is ' + str(player_current_value))   

                if  player_current_value > 21:
                    print('You went over 21, game over')
                    break
                elif player_current_value == 21:
                    print('you won!')
                    break
                else:
                    pass
                 
            else:
                print('It is now the dealers turn')
                return player_current_value
    
        
            




game_play()

