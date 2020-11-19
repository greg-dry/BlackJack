values = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

class Card:
    def __init__(self, rank, face):
        self.rank = rank
        self.face = face
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.face}'

mycard = Card(5, 'Hearts')

print(mycard)

print('hello')

