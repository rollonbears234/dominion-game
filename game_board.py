"""
This is the global board, each player will join this board in the initializer and it will be turn based.



#TODO how are you going to model card games, should I make a card class? each one has an action and an effect on the game board for the player?
- you need a turn method that keeps track of the buy's and the actions left.


I think the cards might need to be some mapping from number to the card type. Would be nice to have this mapping universal everywhere.
I am not fond of the just list of names, have to manually count for everything
* * Maybe even have a string of what the card does so the user can ask if needed, they won't just know!!

program a help function?? - should tell you cost, and name and action details

"""

#use for printing out the options when setting up the game
#TODO change this to action names?
CARD_NAMES = ["CELLAR", "CHAPEL", "MOAT", "HARBINGER", "MERCHANT", "VASSAL", "VILLAGE", "WORKSHOP",
            "BUREAUCRAT", "GARDENS", "MILITIA", "MONEYLENDER", "POACHER", "REMODEL", "SMITHY", "THRONE ROOM",
            "BANDIT", "COUNCIL ROOM", "FESTIVAL", "LABORATORY", "LIBRARY", "MARKET", "MINE", "SENTRY", "WITCH",
            "ARTISAN"]

MONEY_CARDS = ["gold", "copper", "silver"]


number_actions_per = 20 #TODO





class game_board():

    def __init__(self, players = None, cards_used):
        self.golds = num #TODO
        self.silvers = num #TODO
        self.coppers = num
        self.cards = {}

        for card_name in cards_used:
            cards{card_name} = [card(card_name) for i in range(number_actions_per)]



    def pick_cards(name):
        pass

    def game_over():
        """
        checks if game is at a terminal state
        """




class card():

    def __init__(self, card_name):
        self.name = card_name
        self.cost = 0 #TODO, use a cost dictionary
        self.type = ""

        if self.name in CARD_NAMES:
            self.type = "action" #do I need to specify attack or reaction? - Gardens if victory

        if self.name == "GARDENS" or self.name in :
            self.type = "victory"

    def do_action(board, player):
        #there must be a better way to do this
        #TODO where are you subtracting player actions by 1 to represent played? - play.py?
        #TODO also need to subtract one buy
        """
        need to subtract a buy and the money
        """
        player.gold -= self.cost
        player.buy -= 1

        #Do I need an if statement like if player.buy == 0 don't do it!
        if self.name == CARD_NAMES[0]: #CELLAR
            #TODO after you play a card, it shouldn't be in your hard as an option
            """
            +1 action
            discard any number of cards from your hand (not this card) and draw that number of discarded cards
            """
            player.actions += 1
            print("Please type in which cards you would like to discard.")
            print("Your current cards are" + player.cards) # I think we should print cards by 1) NAME and they select the numbers
            print("Please type in the card numbers and comma seperate them with no space")

            card_choices = raw_input("Please enter something: ")

            if " " in card_choices:
                print("remember, no spaces and numbers seperated by commas, try again")

            list_choices = card_choices.split(",")

            #TODO check to make sure they gave valid points
            player.discard(list_choices) #TODO try and catch!
            player.draw(len(list_choices))

        elif self.name == CARD_NAMES[1]: #CHAPEL
            """
            Trash up to four cards
            """
            print("Please type in which cards you would like to trash.")
            print("Your current cards are" + player.cards) # I think we should print cards by 1) NAME and they select the numbers
            print("Please type in the card numbers and comma seperate them with no space")
            card_choices = raw_input("Please enter something: ")

            if " " in card_choices:
                print("remember, no spaces and numbers seperated by commas, try again")

            list_choices = card_choices.split(",")

            #TODO check to make sure they gave valid points
            #TODO, maybe do a try and catch into the trash function and
            player.trash(list_choices) #TODO what are you passing in here

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
            discard_pile = player.discard_pile()
            for i in range(len(discard_pile)):
                print(str(i) + ") " + discard_pile[i].name)

            card_choice = raw_input("Please enter the card: ")

            #TODO clean this up and make it work this way, abstraction!
            player.discard_pile().remove(card_choice)
            player.deck = [card_choice] + player.deck

        elif self.name == CARD_NAMES[4]: #MERCHANT
            """
            +1 card
            +1 action
            first time play a silver this turn, +1 gold
            """
            player.draw(1)
            player.action += 1

            #TODO this is how I am interpreting the rule, but need a played section, only can do this if the card is played
            #TODO say I can't do a persistant rule for this
            if "SILVER" in player.played():
                player.gold += 1

        elif self.name == CARD_NAMES[5]: #VASSAL
            """
            +2 gold
            discard top card of deck, if action card, play it
            """

            #TODO plan better, I feel like I still don't know what any of the types of anything are,
            player.gold += 2
            top_card = player.draw(1):
            if type(top_card) == action:
                top_card.do_action(board, player)
                #TODO  since draw puts it into their hand, you need to make sure to take it out too, after playing
            else:
                player.discard(top_card) #TODO need a mechanism for discarding a card once you are done playing

                #TODO don't discard until the hand is over, then current played cards go into discard


        elif self.name == CARD_NAMES[6]: #VILLAGE
            """
            +1 card
            +2 actions
            """
            player.draw(1)
            player.action += 2

        elif self.name == CARD_NAMES[7]: #WORKSHOP
            """
            gain any card costing up to 4
            """
            available_cards =  board.get_cards() #TODO, some way to get the cards being used
            print("Please select one of the cards to add to your hand:")
            print("Select the card you want by typing in only the number")
            for i in range(len(available_cards)):
                #TODO, need to check if list empty - or it won't be because get_cards won't return something empty, or use a .top method?
                print(str(i) + ") " + available_cards[i][0].name) #but the available card might not be a card object right? Or will I just store a list of card objects - YEA!

            card_choice = raw_input("Please enter the card number: ")

            selected_card = board.get(card_choice) #TODO by the number???  - this affects how I store the card objects, numebrs are weird I think, some dictionary
            player.add(selected_card)



        elif self.name == CARD_NAMES[8]: #BUREAUCRAT
            """
            gain a silver onto your deck
            each other player reveals a victory card from their hand and puts it onto their deck (or revals a hand with no Victory cards!)
            """
            #TODO - how can a ML program or a strategy use this??
            self.player.add(board.get("silver")) #TODO make sure this works

            for other_players in board.players(player): #don't want to return myself???
                other_hand = other_players.hand() #IMPORTANT this is why you always make their hand full after they end the turn and they don't play it until it is their turn
                victory_list = []
                for card in other_hand:
                    if card.type == "vicotry": #TODO how can I do this in gameplay? Let them choose?
                        victory_list.append(card)

                if victory_list.empty():
                    print("Player " + player.name + "'s hand is:")
                    for card in other_hand:
                        print(card.name)
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
            for other_players in board.players(player): #don't want to return myself???
                other_players.discard_to(3) #TODO let this be a player specific implementation

        elif self.name == CARD_NAMES[10]: #MONEYLENDER
            """
            You can trash a copper for +3 gold
            """
            contains_copper = False
            for card in player.hand(): #TODO there must be a better way to abstract this
                if card.name == "copper":
                    contains_copper = True

            #TODO two ways to make this better, the trash method takes in a name and checks if there is a copper
            #TODO you can also implement a player.contains method for name, call it hand_contains(name)

            if contains_copper: #TODO need an easy way to check if you CAN_PLAY this card so my strategy can quickly check (can play this card)
                #assume if they are playing it they want to
                player.trash("copper")

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

            empty_piles = 10 - len(board.stock_piles()) #TODO what does get cards return, just stock piles? TODO I also wrote a get cards function but need to change it
            player.discard(empty_piles) #the discard function takes a number and makes the opponent discard that manually
            #default discard could be discard everything and end turn???

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

            for other_players in board.players(player):
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
                pass, #do nothing, the card is out of the game now
            if choice_1 == "2":
                player.discard(top_two[0])
            else:
                player.deck = [top_two[0]] + player.deck
            print("type in 1) trash 2) discard 4) put back on top") #TODO they should be able to put on top in any order
            print(top_two[1].name)
            choice_2 = raw_input("Please enter the numer: ")
            if choice_2 == "1":
                pass, #do nothing, the card is out of the game now
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
                if not other_players.contain("MOAT") #contains is an abstracted method!
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
