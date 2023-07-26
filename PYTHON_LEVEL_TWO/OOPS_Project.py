from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class CardDeck():

    def __init__(self):
        print('Creating New Card Deck....')
        self.my_cards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print('SHUFFLING CARDS')
        shuffle(self.my_cards)

    def split_half(self):
        return (self.my_cards[:26],self.my_cards[26:])

class Hand():

    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add_card(self,new_card):
        self.cards.extend(new_card)

    def remove_card(self):
        return self.cards.pop()


class Player():

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def player_card(self):
        withdrawn_card = self.hand.remove_card()
        print("{} has placed {} ".format(self.name,withdrawn_card))
        print("\n")
        return withdrawn_card

    def remove_war_card(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for i in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def has_cards(self):
        # Returns true if the player has cards else return false.
        return len(self.hand.cards) != 0


print("Welcome to the Card War.....")
deck = CardDeck()
deck.shuffle()
half1,half2 = deck.split_half()

computer = Player('Computer',Hand(half1))

player_name = input('What is your name ? ')
player = Player(player_name,Hand(half2))

total_round = 0
war_count = 0

while player.has_cards() and computer.has_cards():
    total_round += 1
    print('Time for New round')
    print('here are the current standing')
    print(player.name+" has the count: "+str(len(player.hand.cards)))
    print(computer.name+" has the count: "+str(len(computer.hand.cards)))
    print('Play Card')

    table_cards = []

    c_card = computer.player_card()
    p_card = player.player_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print('War!')
        table_cards.extend(player.remove_war_card())
        table_cards.extend(computer.remove_war_card())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            player.hand.add_card(table_cards)
        else:
            computer.hand.add_card(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            player.hand.add_card(table_cards)
        else:
            computer.hand.add_card(table_cards)

print('Game Over !')
print('Number Of round : ',total_round)
print('War Count : ',war_count)
print('User has card : ',str(player.has_cards()))
print('Computer has card : ',str(computer.has_cards()))