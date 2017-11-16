"""
This is the global board, each player will join this board in the initializer and it will be turn based.

#TODO how are you going to model card games, should I make a card class? each one has an action and an effect on the game board for the player?
- you need a turn method that keeps track of the buy's and the actions left.


I think the cards might need to be some mapping from number to the card type. Would be nice to have this mapping universal everywhere.
I am not fond of the just list of names, have to manually count for everything
* * Maybe even have a string of what the card does so the user can ask if needed, they won't just know!!

program a help function?? - should tell you cost, and name and action details

"""
import player

#use for printing out the options when setting up the game
#TODO change this to action names?
#TODO GArdens could cause problems-> but it is a stock pile card and a victory card, it should be here, just need to handle dubplicate
CARD_NAMES = ["CELLAR", "CHAPEL", "MOAT", "HARBINGER", "MERCHANT", "VASSAL", "VILLAGE", "WORKSHOP",
            "BUREAUCRAT", "GARDENS", "MILITIA", "MONEYLENDER", "POACHER", "REMODEL", "SMITHY", "THRONE ROOM",
            "BANDIT", "COUNCIL ROOM", "FESTIVAL", "LABORATORY", "LIBRARY", "MARKET", "MINE", "SENTRY", "WITCH",
            "ARTISAN"]
MONEY_CARDS = ["GOLD", "COPPER", "SILVER"]
VICTORY_CARDS = ["GARDENS", "ESTATE", "DUCHY", "PROVINCE"]
CARD_INFO = {
CARD_NAMES[0]: {"cost": 2}, #CELLAR
CARD_NAMES[1]: {"cost": 2}, #CHAPEL
CARD_NAMES[2]: {"cost": 2}, #MOAT
CARD_NAMES[3]: {"cost": 3}, #HARBINGER
CARD_NAMES[4]: {"cost": 3}, #MERCHANT
CARD_NAMES[5]: {"cost": 3}, #VASSAL
CARD_NAMES[6]: {"cost": 3}, #VILLAGE
CARD_NAMES[7]: {"cost": 3}, #WORKSHOP
CARD_NAMES[8]: {"cost": 4}, #BUREAUCRAT
CARD_NAMES[9]: {"cost": 4}, #GARDENS
CARD_NAMES[10]: {"cost": 4}, #MILITIA
CARD_NAMES[11]: {"cost": 4}, #MONEYLENDER
CARD_NAMES[12]: {"cost": 4}, #POACHER
CARD_NAMES[13]: {"cost": 4}, #REMODEL
CARD_NAMES[14]: {"cost": 4}, #SMITHY
CARD_NAMES[15]: {"cost": 4}, #THRONE ROOM
CARD_NAMES[16]: {"cost": 5}, #BANDIT
CARD_NAMES[17]: {"cost": 5}, #COUNCIL ROOM
CARD_NAMES[18]: {"cost": 5}, #FESTIVAL
CARD_NAMES[19]: {"cost": 5}, #LABORATORY
CARD_NAMES[20]: {"cost": 5}, #LIBRARY
CARD_NAMES[21]: {"cost": 5}, #MARKET
CARD_NAMES[22]: {"cost": 5}, #MINE
CARD_NAMES[23]: {"cost": 5}, #SENTRY
CARD_NAMES[24]: {"cost": 5}, #WITCH
CARD_NAMES[25]: {"cost": 6}, #ARTISAN
MONEY_CARDS[0]: {"cost": 6, "value": 3}, #GOLD
MONEY_CARDS[1]: {"cost": 0, "value": 1}, #COPPER
MONEY_CARDS[2]: {"cost": 3, "value": 2}, #SILVER
VICTORY_CARDS[0]: {"cost": 4}, #GARDENS
VICTORY_CARDS[1]: {"cost": 2, "points": 1}, #ESTATE
VICTORY_CARDS[2]: {"cost": 5, "points": 3}, #DUCHY
VICTORY_CARDS[3]: {"cost": 8, "points": 6} #PROVINCE
}
num_cards_per_pile = 11
num_gold = 30
num_silver = 40
num_copper = 60
num_estate = 24
num_duchy = 12
num_province = 12

#TODO
#Curse Cards???

class Game_Board():

    def __init__(self, sim_mode = False):
        self.golds = []
        self.silvers = []
        self.coppers = []
        self.victory = {}
        self.players = []
        self.stock_piles = {}
        self.sim_mode = sim_mode

        #initializing the board
        self.select_stock_cards()
        self.setup_players()
        self.init_money()
        self.init_victory()

    def select_stock_cards(self):
        """
        used to set up the initial 10 stockpiles
        """
        selected_cards = 0
        previous_nums = []
        self.print_all_info()
        while selected_cards != 10:
            #try:
            card_choice = raw_input("Please enter a number: ")
            try:
                card_num = int(card_choice)
            except:
                print("You need to input a number!")
                continue
            if not self.sim_mode and (0 <= int(card_choice) <= 25) and (int(card_choice) not in previous_nums):
                card_name = CARD_NAMES[int(card_choice)]
                print("Selected " + card_name)
                self.stock_piles[card_name] = [card(card_name) for _ in range(num_cards_per_pile)]
                previous_nums.append(int(card_choice))
                selected_cards += 1
            elif self.sim_mode and (0 <= int(card_choice) <= 11) and (int(card_choice) not in previous_nums):
                card_name = strategies.working_cards[int(card_choice)]
                print("Selected " + card_name)
                self.stock_piles[card_name] = [card(card_name) for _ in range(num_cards_per_pile)]
                previous_nums.append(int(card_choice))
                selected_cards += 1
            else:
                print("The number has to be a action card, so between 0-25 and one you haven't selected before")
                print("Previously selected = ", previous_nums)
            #except:
                #print("please just type in the number you want to choose")
        print("Selected Cards: ", self.stock_piles.keys())

    def setup_players(self):
        """
        initializes the player objects
        """
        #first, how many players do you want?
        if self.sim_mode:
            return

        num_players = 0
        while num_players == 0:
            try:
                card_choice = raw_input("How many players are playing?:  ")
                if 0 < int(card_choice) <= 8:
                    num_players = int(card_choice)
            except:
                print("please just type in a number between 0 and 8")

        players_left = num_players
        while players_left > 0:
            card_choice = raw_input("Setting up player" + str(num_players - players_left) + ", what is your player name?: ")
            self.players.append(player.Player(player_name = card_choice))
            players_left -= 1

    def init_money(self):
        self.golds = [card(MONEY_CARDS[0]) for _ in range(num_gold)]
        self.coppers = [card(MONEY_CARDS[1]) for _ in range(num_copper)]
        self.silvers = [card(MONEY_CARDS[2]) for _ in range(num_silver)]

    def init_victory(self):
        self.victory[VICTORY_CARDS[1]] = [card(VICTORY_CARDS[1]) for _ in range(num_estate)]
        self.victory[VICTORY_CARDS[2]] = [card(VICTORY_CARDS[2]) for _ in range(num_duchy)]
        self.victory[VICTORY_CARDS[3]] = [card(VICTORY_CARDS[3]) for _ in range(num_province)]

    def print_all_info(self):
        """
        used to print stockpiles
        """
        i = 0
        if not self.sim_mode:
            for card in CARD_NAMES:
                if card not in self.stock_piles.keys():
                    print(card, "costs " + str(CARD_INFO[card]["cost"]), "and its number is " + str(i))
                i += 1
        else:
            for card in strategies.working_cards:
                if card not in self.stock_piles.keys():
                    print(card, "costs " + str(CARD_INFO[card]["cost"]), "and its number is " + str(i))
                i += 1

    def game_over(self):
        """
        checks if game is at a terminal state

        check if three stockpiles empty or the provinces are gone
        """
        empty_stockpile_count = 0
        num_province = len(self.victory["PROVINCE"])
        for stock in self.stock_piles.keys():
            if len(self.stock_piles[stock]) == 0:
                empty_stockpile_count += 1
        if empty_stockpile_count >= 3 or num_province == 0:
            return True
        else:
            return False

    def buy(self, card_name, player):
        """
        once we select a card, this will either buy it or return false saying we can't afford it
        """
        potential_card = self.take(card_name)
        if potential_card is None:
            print("That card is not available")
            return False
        elif player.buys > 0 and potential_card.cost <= player.money:
            print("Buying " + potential_card.name)
            player.money -= potential_card.cost
            player.buys -= 1
            player.played.append(potential_card)
            return True
        else:
            self.put_back(potential_card)
            return False

    def take(self, card_name):
        """
        lets a player take a card off the board into their hand
        """
        #TODO need to handle when one of the piles is empty, but can we check earlier to make this so we know the card is there?
        try:
            if card_name in self.stock_piles.keys():
                return self.stock_piles[card_name].pop()
            elif card_name in self.victory.keys():
                return self.victory[card_name].pop()
            elif card_name == "GOLD":
                return self.golds.pop()
            elif card_name in "SILVER":
                return self.silvers.pop()
            elif card_name == "COPPER":
                return self.coppers.pop()
            else:
                print("Card name doesn't exist")
                return None
        except:
            print("that card might be empty")
            return None #maybe a pile is empty

    def put_back(self, card):
        try:
            if card.name in self.stock_piles.keys():
                self.stock_piles[card_name].append(card)
            elif card.name in self.victory.keys():
                self.victory[card_name].append(card)
            elif card.name == "GOLD":
                self.golds.append(card)
            elif card.name in "SILVER":
                self.silvers.append(card)
            elif card.name == "COPPER":
                self.coppers.append(card)
        except:
            return None

    def num_players(self):
        return len(self.players)

    def players(self, my_player):
        """
        returns a list of players that are not myself
        """
        player_list = []
        for player in self.players:
            if my_player != player:
                player_list.append(player)
        return player_list


class card():

    def __init__(self, card_name):
        self.name = card_name
        self.cost = CARD_INFO[self.name]["cost"]
        self.type = ""

        if self.name in CARD_NAMES:
            self.type = "action"
        elif self.name in VICTORY_CARDS :
            self.type = "victory"
        else:
            self.type = "money" #TODO could cause problems if not right


    def do_action(self, board, player):
        """
        this does what it is told, it plays the card on the board played by player
        """

        if self.name == CARD_NAMES[0]: #CELLAR
            """
            +1 action
            discard any number of cards from your hand (not this card) and draw that number of discarded cards
            """
            player.actions += 1
            print("Please type in which cards you would like to discard.")
            print("Input: comma seperated numbers starting at 0 from your hand \n")

            card_choices = raw_input("Please enter something: ")

            if " " in card_choices:
                print("remember, no spaces and numbers seperated by commas, try again")
                self.do_action(board, player) #self is me!
            else:
                try:
                    list_choices = card_choices.split(",")
                    player.hand_to_discard(list_choices)
                    player.draw(len(list_choices)) #if it gets here, will already have discarded correctly and draw should never error
                except Exception as e:
                    print(e)
                    print("Please try again, that was an invalid command \n")
                    self.do_action(board, player)


        elif self.name == CARD_NAMES[1]: #CHAPEL
            """
            Trash up to four cards
            """
            print("Please type in which cards you would like to trash.")
            print("Your current cards are" + player.cards) # I think we should print cards by 1) NAME and they select the numbers
            print("Please type in the card numbers and comma seperate them with no space \n")
            card_choices = raw_input("Please enter something: ")

            if " " in card_choices:
                print("remember, no spaces and numbers seperated by commas, try again")
                self.do_action(board, player)
            else:
                list_choices = card_choices.split(",")
                try:
                    player.trash(list_choices)
                except Exception as e:
                    print(e)
                    self.do_action(board, player)

        elif self.name == CARD_NAMES[2]: #MOAT
            """
            Draw two cards and protects you from action cards if it is in your hand
            """
            player.draw(2)

        elif self.name == CARD_NAMES[3]: #HARBINGER
            """
            +1 card
            +1 action
            Look into discard pile, you can put something from there onto your deck
            """
            player.draw(1)
            player.action += 1

            print("Your discard pile: type in the number to place that card on the top of your current deck")
            for i in range(len(player.discard)):
                print(str(i) + ") " + player.discard[i].name)

            card_choice = raw_input("Please enter the card number: ")

            try:
                card = player.discard[str(card_choice)]
                player.discard.remove(card)
                player.deck = [card] + player.deck
            except Exception as e:
                print("Incorrect card input, try again")
                self.do_action(board, player)

        elif self.name == CARD_NAMES[4]: #MERCHANT
            """
            +1 card
            +1 action
            first time play a silver this turn, +1 gold
            """
            player.draw(1)
            player.action += 1

            #TODO why would you play a silver then get gold, I don't get it
            played_names = [player.played[i].name for i in range(len(player.played))]
            if "SILVER" in played_names:
                player.gold += 1

        elif self.name == CARD_NAMES[5]: #VASSAL
            """
            +2 gold
            discard top card of deck, if action card, play it
            """

            player.money += 2
            top_card = player.take()
            if top_card.name in game_board.CARD_NAMES:
                top_card.do_action(board, player)
                player.played.append(top_card)
            else:
                player.discard(top_card)


        elif self.name == CARD_NAMES[6]: #VILLAGE
            """
            +1 card
            +2 actions
            """
            player.draw(1)
            player.actions += 2

        elif self.name == CARD_NAMES[7]: #WORKSHOP
            """
            gain any card costing up to 4
            """
            print("Please select one of the cards to add to your hand costing up to 4")
            print("Select the card you want by typing the name:")

            card_choice = raw_input("Please enter the card name: ")

            try:
                selected = self.game_board.stock_piles[card_choice.upper()].pop() #will
                player.add(selected)
            except Exception as e:
                print(e) #maybe that card is out
                print("Incorrect card input, try again")
                self.do_action(board, player)

        elif self.name == CARD_NAMES[8]: #BUREAUCRAT
            """
            gain a silver onto your deck
            each other player reveals a victory card from their hand and puts it onto their deck (or revals a hand with no Victory cards!)
            """
            #TODO - how can a ML program or a strategy use this??
            silver_card = self.game_board.silvers.pop()
            player.add(silver_card)

            for other_players in self.game_board.players(player): #don't want to return myself???
                other_hand = other_players.hand() #IMPORTANT this is why you always make their hand full after they end the turn and they don't play it until it is their turn
                victory_list = []
                for card in other_hand:
                    if card.type == "vicotry": #TODO how can I do this in gameplay? Let them choose?
                        victory_list.append(card)

                if victory_list.empty():
                    print("Player " + player.name + "'s hand is:")
                    print other_hand
                else:
                    print("Player" + player.name + "choose a victory card to get rid of from your hand")
                    #TODO can I hide this from other people??
                    for i in range(len(victory_list)):
                        print(str(i) + ") " + victory_list[i].name)

                    card_choice = raw_input("Please enter the card number: ")

                    other_players.deck = [victory_list[int(card_choice)]] + other_players.deck #Putting it on deck, #TODO make a method for this, kinda common action


        elif self.name == CARD_NAMES[8]: #GARDENS
            """
            this is a victory card, only counts at game end
            """
            pass

        elif self.name == CARD_NAMES[9]: #MILITIA
            """
            +2 gold
            attack
            each other player discards down to 3 cards in their hand
            """

            #TODO for attach, each bot needs a strategy to handle this
            player.gold += 2
            for other_player in self.game_board.players(player): #don't want to return myself???
                other_player.discard_to(3)

        elif self.name == CARD_NAMES[10]: #MONEYLENDER
            """
            You can trash a copper for +3 gold
            """
            contains_copper = False
            index = 0
            card_types = [card.type for card in player.hand]
            for card in card_types:
                if card.name == "copper":
                    contains_copper = True
                    break
                index += 1

            if contains_copper:
                #assume if they are playing it they want to
                player.trash(index)

        elif self.name == CARD_NAMES[12]: #POACHER
            """
            +1 card
            +1 action
            +1 gold
            discard a card per empty stock pile
            """

            player.draw(1)
            player.actions += 1
            player.gold += 1

            empty_piles = 0
            for stock in self.game_board.stock_piles.values():
                if len(stock) == 0:
                    empty_piles += 1

            player.discard_to(len(player.hand) - empty_piles)

        elif self.name == CARD_NAMES[13]: #REMODEL
            """
            trash a card from your hand and
            gain a card costing up to 2 more than it
            """

            #two approaches here, let the player do the choosing, or ask them out in the open

            print("Please select a card from your hand to trash") #can keep anonymous by not printing everything #Abstract the seleting thing, can generalize
            player_hand = player.hand()
            selected_card = player.select_from(player_hand) #TODO I am trying this instead of iterating and asking for a number, let the player handle it!
            purchasing_power = selected_card.cost + 2

            player.buy(purchasing_power, oneTime = True) #TODO this is a method we use in play time, after actions run out, they would buy, but this is a one time buy
            #could get confusing because what if they try to use multiple buys and shit,

            player.trash(selected_card) #End


        elif self.name == CARD_NAMES[14]: #SMITHY
            """
            +3 cards
            """
            player.draw(3)

        elif self.name == CARD_NAMES[15]: #THRONE ROOM
            """
            play an action card from your hand twice
            """
            throne = player.select_from(player.hand()) #pick an action card!

            throne.do_action(board, player)
            throne.do_action(board, player)


        elif self.name == CARD_NAMES[16]: #BANDIT
            """
            gain a gold
            each player reveals top 2 cards of deck, trash a revealed treasure card other than copper, discard the rest
            """
            gold = board.get("gold")
            player.add(gold) #TODO add it in my current hand, so not discard or deck yet

            for other_players in board.players(player):
                rest = other_players.deck[2:] #TODO what if they have less than two, need to shuffle!!!
                top_two = other_players.deck[0:2]#but this adds two to their hand, it doesn't return them!
                players.deck = rest
                trashed = False
                for top in top_two: #at this point, it is like the player doesn't own the card, we need to either discard or put in hand or put in deck.
                    if top.type in ["gold", "silver"] and not trashed:
                        print(other_players.name + "lost a " + top.type)
                        player.trash(top) #TODO need to give them a choice if they happen to have two
                        trashed = True
                    else:
                        player.discard(top)

        elif self.name == CARD_NAMES[17]: #COUNCIL ROOM
            """
            +4 cards
            +1 buy
            each other player draws a card
            """
            player.draw(4)
            player.buys += 1

            for other_player in self.game_board.players(player):
                other_players.draw(1)

        elif self.name == CARD_NAMES[18]: #FESTIVAL
            """
            +2 actions
            +1 buy
            +2 gold
            """
            player.actions += 2
            player.buys += 1
            player.gold += 2

        elif self.name == CARD_NAMES[19]: #LABORATORY
            """
            +2 cards
            +1 action
            """
            player.draw(2)
            player.actions += 1

        elif self.name == CARD_NAMES[20]: #LIBRARY
            """

            """
            discarded_pile = []
            while len(player.hand()) < 7:
                curr_card = player.take(1)
                print("card is " + curr_card.name)
                if curr_card.type is "action":
                    print("1) keep")
                    print("2) discard")
                    card_decision = raw_input("select move for action card:")
                    if card_decision == "1":
                        player.add(curr_card)
                    else:
                        discarded_pile.append(curr_card)
                else:
                    player.add(curr_card)

            for card in discarded_pile:
                player.discard(card)


        elif self.name == CARD_NAMES[21]: #MARKET
            """
            +1 card
            +1 action
            +1 buy
            +1 gold
            """
            player.draw(1)
            player.actions += 1
            player.buys += 1
            player.gold += 1

        elif self.name == CARD_NAMES[22]: #MINE
            """
            can trash a treasure from your hand and gain a treasure costing up to 3 more than it -> trash and upgrade
            """
            player_hand = player.hand()
            money_cards = []
            for card in player_hand:
                if card.name in MONEY_CARDS:
                    money_cards.append(card)

            print("choose a card to upgrade by selecting the number") #privacy isn't important here, it is your turn
            for i in range(len(money_cards)):
                print(str(i) + ") " + money_cards[i].name)

            card_choice = raw_input("Please enter the card number: ")
            seleted_money = money_cards[int(card_choice)] #TODO what if they don't have money!!

            upgrade = "" #don't let gold upgrades, just stupid
            if seleted_money.type == "silver":
                upgrade = "gold"
            else:
                upgrade = "silver" #TODO might need more cases here just in case users are stupid

            new_gold = board.get(update)
            player.add(new_gold)
            player.trash(seleted_money)

        elif self.name == CARD_NAMES[23]: #SENTRY
            """
            +1 card
            +1 action
            look at top 2 cards
            trash/discard any number of them, put the rest back on top in any order
            """
            player.draw(1)
            player.actions += 1

            top_two = player.take(2) #TODO I like this for taking from the top, can also use this abstraction to implement .draw()
            #can also take care of shuffling here if needed! It should always work, if not it will say, no more cards to draw, use a try and catch to cath this error
            print("here is the first card:")
            print(top_two[0].name)
            print("type in 1) trash 2) discard 4) put back on top") #TODO they should be able to put on top in any order
            choice_1 = raw_input("Please enter the numer: ")
            if choice_1 == "1":
                print("Card is out of the game")
            if choice_1 == "2":
                player.discard(top_two[0])
            else:
                player.deck = [top_two[0]] + player.deck #use add? or a different method #TODO
            print("type in 1) trash 2) discard 4) put back on top") #TODO they should be able to put on top in any order
            print(top_two[1].name)
            choice_2 = raw_input("Please enter the numer: ")
            if choice_2 == "1":
                print("card is out of the game")
                #do nothing, the card is out of the game now
            if choice_2 == "2":
                player.discard(top_two[0])
            else:
                player.deck = [top_two[0]] + player.deck

        elif self.name == CARD_NAMES[24]: #WITCH
            """
            +2 cards
            each other player gets a curse (unless moat!)
            """

            player.draw(2)

            for other_players in board.players(player): #don't want to return myself???
                if not other_players.contain("MOAT"): #contains is an abstracted method!
                    player.add(board.get("curse"))


        elif self.name == CARD_NAMES[25]: #ARTISAN
            """
            gain a card costing up to 5
            put a card from your hand onto your deck
            -- similar to REMODEL
            """

            purchasing_power = 5

            player.buy(purchasing_power, oneTime = True) #TODO this is a method we use in play time, after actions run out, they would buy, but this is a one time buy
            #could get confusing because what if they try to use multiple buys and shit,

            print("select a card from your hand to put on top of your deck")
            for i in range(len(player.hand())):
                print(str(i) + ") " + player.hand()[i].name)

            selected_num = raw_input("Please enter the numer: ")
            selected_card = player.hand[int(selected_num)]

            player.hand.remove(selected_card) #TODO, do I need another custom method here? it would be an @override right?, I need something to just take cards from my deck
            #the abstracted method would help move cards from hand to discard anyway when a turn ends

            player.deck = [selected_card] +player.deck
