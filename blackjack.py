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

 

class Player(Deck, Card):
    def __init__(self, balance):
        self.balance = balance
        self.my_cards = []
        self.values = []


    def __str__(self):
        return f"You have ${self.balance}."

    def player_hit(self, new_card):
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
    
   
                       
class Dealer(Deck):
    def __init__(self):
        self.dealer_cards = []
        self.dealer_values = []

    def dealer_hit(self, new_card):
        self.dealer_cards.append(new_card)
        self.dealer_values.append(new_card.value)




mydeck = Deck()
myplayer = Player(balance = 100)
mydealer = Dealer()


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


mydeck.shuffle()

top_card = mydeck.remove_card()

myplayer.player_hit(top_card)

def game_play():
    while game_on == True:
        myplayer.make_a_bet()
        break

    
    

    print(f"Your card is {myplayer.my_cards[0]}")
    players_turn = True
    while players_turn == True:
        try:
            hit_choice = int(input("Would you like to hit? Enter 1 for Yes, 2 for No: "))
        except: 
            print('invalid answer')
        else:
            if hit_choice == 1:
                top_card = mydeck.remove_card()
                myplayer.player_hit(top_card)
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
                player_current_value = sum(myplayer.values)
                print('your current hand value is ' + str(player_current_value))
                print('It is now the dealers turn')
                
                top_card = mydeck.remove_card()
                mydealer.dealer_hit(top_card)
                print(f"The dealer's card is {mydealer.dealer_cards[0]}")
                dealer_wins = False
                while dealer_wins == False:
                    top_card = mydeck.remove_card()
                    mydealer.dealer_hit(top_card)
                    print(f"The dealer's card is {mydealer.dealer_cards[-1]}")
                    dealer_current_value = sum(mydealer.dealer_values) 
                    print('Dealers current hand value is ' + str(dealer_current_value))

                    if dealer_current_value > 21:
                        print('Dealer went over 21, you win!')
                        dealer_wins = True
                        players_turn = False
                    elif dealer_current_value > player_current_value and dealer_current_value <= 21:
                        print('dealer has higher hand, you lose.')
                        dealer_wins = True
                        players_turn = False
                    else: 
                        pass
                        
                        
                        

game_play()

    
            






