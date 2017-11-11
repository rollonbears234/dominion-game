"""
Each player takes in a strategy string

If not strategy is given, they will ask for the move for that player each time.
"""
import random

#Strategies
GOLDSTRAT = "goldstrategy"
ACTIONSTRAT = "actionstrategy"

class Player():

    def __init__(self, strategy = None, player_name):

        self.strategy = strategy
        self.extra_cards = 0 #TODO what is this for?
        self.buys = 1
        self.actions = 1
        self.money = 0
        self.deck = []
        self.discard = []
        self.hand = []
        self.played = []
        self.player_name = player_name


        #initializing our first two cards
        for i in range(0,7):
            self.deck.append("gold") #the gold should be an object too that increases current money
        for i in range(0, 3):
            self.deck.append("estate")

        def start_hand(self):
            """
            used to count our money and make sure we have 5 cards in our hand
            only end turn calls this so we should have an empty hand
            """
            self.draw() for _ in range(5)
            for card in self.hand:
                if card.type = "MONEY":
                    self.money += card.value #TODO is this right

        def print_hand(self):
            """
            used for interacting with the user so he/she know which cards they can play
            """
            hand_names = [card.name for card in self.hand]
            print("Your hand:" + hand_names)


        def randomize_deck(self, deck):
            random.shuffle(deck)

        def discard(self, card):
            self.discard.append(card)

        def draw(self):

            if len(self.deck) > 0:
                self.hand.append(self.deck.pop(0))
            else:
                self.deck = self.discard
                self.discard = []
                self.randomize_deck(self.deck)
                self.draw()

        def add(self, card):
            """
            Given a card from another player or the board, we can add it to our hand
            """
            self.hand.append(card)

        def discard_to(self, num):
            #call self choose to use an interface that lets someone choose
            choose_string = "Player" + self.player_name + ", please discard down to" + str(num)

        def take(self):
            card = self.deck.pop(0)
            return card

        def contains(self, card_type):
            """
            should be true and false
            """

            for card in self.deck:
                if card.type == card_type:
                    return True
            return False

        def buy(self, card):

            if card.cost <= self.money:
                self.money -= card.cost
                self.hand.append(card)
                return True
            else:
                return False

        def choose(self, choose_string, num_choices, action):
            """
            Modularizing all choices for a player

            action is a player function on a single card
            """
            #TODO a try and except block might be useful

            print(choose_string)
            card_choices = raw_input("Please enter something: ")
            print("Your current cards are" + player.cards)
            print("Please type in the card numbers and comma seperate them with no space")

            if " " in card_choices:
                print("remember, no spaces and numbers seperated by commas, try again")

            list_choices = card_choices.split(",")

            if len(list_choices) != num_choices or " " in card_choices:
                print("try again, you made a mistake")
                self.choose(choose_string, num_choices, action)

            cards = []

            for choice_num in list_choices:
                cards.append(self.deck[int(choice_num)])

            if action is not None:
                for card in cards:
                    #TODO need to consider the card might still be in the deck
                    #TODO do I need to remove the card from the deck?
                    #TODO also need to figure out how to call the player.action when action is a function? or a string?
                    self.action(card)
            else:
                return cards

        def select_from(self):
            """
            let the player handle picking a card
            not sure if this is different than choose
            """
            pass

        def end_turn(self):
            for card in self.played:
                self.discard.append(card)
            for card in self.hand:
                self.discard.append(card)
            self.money = 0
            self.actions = 1
            self.buys = 1
            self.start_hand()
