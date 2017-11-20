"""
Each player takes in a strategy string

If not strategy is given, they will ask for the move for that player each time.
"""
import random
import game_board

#Strategies
GOLDSTRAT = "goldstrategy"
ACTIONSTRAT = "actionstrategy"

class Player():

    def __init__(self, player_name, strategy = None):

        self.strategy = strategy
        self.buys = 1
        self.actions = 1
        self.money = 0
        self.deck = []
        self.discard = []
        self.hand = []
        self.played = []
        self.player_name = player_name

        #initializing our initial deck 3 estates and 7 coppers
        for i in range(0,7):
            self.deck.append(game_board.card("COPPER"))
        for i in range(0, 3):
            self.deck.append(game_board.card("ESTATE"))
        self.randomize_deck()
        self.start_hand()

    def start_hand(self):
        """
        used to count our money and make sure we have 5 cards in our hand
        only end turn calls this so we should have an empty hand
        """
        [self.draw() for _ in range(5)] #initially draw 5

    def print_hand(self):
        """
        used for interacting with the user so he/she know which cards they can play
        """
        hand_names = [card.name for card in self.hand]

        played_names = [card.name for card in self.played]
        print("Played:", played_names)
        print("Total Money left", self.money)
        print("Total Actions Left", self.actions)
        print("Total Buys Left", self.buys)
        print("Your hand:", hand_names)

    def randomize_deck(self, deck=None):
        if deck == None:
            random.shuffle(self.deck)
        else:
            random.shuffle(deck)

    def discard_func(self, card):
        """
        does not remove from hand or anything, just appends the card
        """
        self.discard.append(card)

    def draw(self, amount = 1):

        for _ in range(amount):
            if len(self.deck) > 0:
                new_card = self.deck.pop(0)
                if new_card.type == "money":
                    self.money += game_board.CARD_INFO[new_card.name]["value"]
                self.hand.append(new_card) #Should be using self.add
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
        """
        num is the number of cards the player needs to discard to
        """
        #call self choose to use an interface that lets someone choose
        choose_string = "Player" + self.player_name + ", please discard down to" + str(num)
        #TODO

    def take(self):
        if len(self.deck) == 0:
            self.deck = self.discard
            self.discard = []
            self.randomize_deck()
        card = self.deck.pop(0)
        return card

    def contains(self, card_type):
        """
        should be true and false

        need to do this for the hand though right?
        """
        for card in self.deck:
            if card.type == card_type:
                return True
        return False

    def hand_to_discard(self, list_indices):
        """
        used to take user input and discard selected cards from the hand
        list_indeces might need to be converted to integers
        """
        [self.hand[int(i)] for i in list_indeces]
        for card in self.hand:
            self.discard(card)
            self.hand.remove(card)

    def trash(self, list_indeces):
        [self.hand[int(i)] for i in list_indeces]
        for card in self.hand:
            self.hand.remove(card)


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
            self.choose(choose_string, num_choices, action)
            print("remember, no spaces and numbers seperated by commas, try again")
        else:
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

    def end_turn(self):
        for card in self.played:
            self.discard.append(card)
        for card in self.hand:
            self.discard.append(card)
        self.played = []
        self.hand = []
        self.money = 0
        self.actions = 1
        self.buys = 1
        self.start_hand()

    def deck_all(self):
        for card in self.hand:
            self.deck.append(card)
        for card in self.played:
            self.deck.append(card)
        for card in self.discard:
            self.deck.append(card)
