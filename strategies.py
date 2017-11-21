"""
Used to make my strategies testing in the play

Beginning strategies should default to buying a province if they have money -> get some convergence
"""
import player
import game_board
import random


strategies = ["random", "max_actions", "max_money", "balance", "festival", "market"]

working_cards = ["MOAT", "MERCHANT", "VASSAL", "VILLAGE",
            "GARDENS", "MONEYLENDER", "SMITHY",
            "COUNCIL ROOM", "FESTIVAL", "LABORATORY", "MARKET"]

#These work for buy and play
#will use this to get more actions!
max_action_cards = ["LABORATORY", "FESTIVAL", "MARKET", "VILLAGE", "SMITHY", "VASSAL", "MOAT"] #draw is also really good, I

#max_money_cards
max_money_cards = ["GOLD", "SILVER", "MONEYLENDER", "FESTIVAL", "MARKET", "COPPER"]


class Strategy():


    """
    will have an interface for decision making (buy or play or end)
    will differ those decisions based on the strategy name
    """

    def __init__(self, strategy_name , sim_name):
        self.strategy_name = strategy_name
        self.sim_name = sim_name
        self.my_player = player.Player("sim-" + strategy_name+ "-" + sim_name, strategy = strategy_name)


    def get_playable_cards(self):
        """
        returns list of cards my player can play from the hand
        that is, money >= card cost and buy >= 0

        this is just like console so the answer is an index
        """
        can_play = []
        player_hand = self.my_player.hand
        for i in range(len(player_hand)):
            if player_hand[i].name in game_board.CARD_NAMES:
                can_play.append(i)
        return can_play

    def get_can_buy(self, board):
        options = board.get_buyable()
        can_list = []
        for card_name in options:
            if game_board.CARD_INFO[card_name]["cost"] <= self.my_player.money:
                can_list.append(card_name)

        return can_list


    # def print_board(self, board):
    #     """
    #     prints current board, so piles available, etc.
    #     put it here so they can see board state as they play
    #     """
    #     for card in board.stock_piles.keys():
    #         if len(board.stock_piles[card]) > 0:
    #             print("Stockpile", card, "cost " +  str(game_board.CARD_INFO[card]["cost"]), "remaining", len(board.stock_piles[card]) )
    #     print("Golds", len(board.golds))
    #     print("Silvers", len(board.silvers))
    #     print("Coppers", len(board.coppers))
    #     print("Victory Cards", board.victory.keys(), [len(vic) for vic in board.victory.values()]) #DUCHY or another might be 0

    def select_action(self, action_list, strategy):
        """
        if it is a buy or action strategy, will select the card accordingly

        Balance will alternate which strategy is uses depending on the current balance

        action_list is already the index in my hand

        returns the index in the hand of the card
        """
        best_index = float("inf")
        hand_index = action_list[random.randint(0,len(action_list) - 1)]
        if strategy == "max_actions":
            for i in action_list:
                if self.my_player.hand[i].name in max_action_cards:
                    curr_index = max_action_cards.index(self.my_player.hand[i].name)
                    if curr_index <= best_index:
                        best_index = curr_index
                        hand_index = i
            return hand_index
        elif strategy == "max_money":
            for i in action_list:
                if self.my_player.hand[i].name in max_money_cards:
                    curr_index = max_money_cards.index(self.my_player.hand[i].name)
                    if curr_index <= best_index:
                        best_index = curr_index
                        hand_index = i
            return hand_index


    def select_buy(self, buy_list, strategy):
        """
        if it is a buy or action strategy, will select the card accordingly

        Balance will alternate which strategy is uses depending on the current balance


        """
        best_index = float("inf")
        card_name = buy_list[random.randint(0,len(buy_list) - 1)]
        if strategy == "max_actions":
            for card in buy_list:
                if card in max_action_cards:
                    curr_index = max_action_cards.index(card)
                    if curr_index <= best_index:
                        best_index = curr_index
                        card_name = card
            return buy_list.index(card_name)
        elif strategy == "max_money":
            for card in buy_list:
                if card in max_money_cards:
                    curr_index = max_money_cards.index(card)
                    if curr_index <= best_index:
                        best_index = curr_index
                        card_name = card
            return buy_list.index(card_name)

    def balancer(self):
        """
        looks at my players' hand and determines money move, or action move
        """
        options = ["max_actions", "max_money"]
        total_money = 0
        total_action = 0
        all_cards = self.my_player.hand + self.my_player.discard + self.my_player.played + self.my_player.deck
        for card in all_cards:
            if card in max_action_cards:
                total_action += 1
            if card in max_money_cards:
                total_money += 1

        if total_money > total_action:
            return "max_actions"
        if total_action > total_money:
            return "max_money"
        else:
            pick = random.randint(0,1)
            return options[pick]

    def play_card_strat(self,buy_phase, select_list, card_name):
        """
        will buy the card and play it whenever possible

        otherwise, play with balance
        """
        upper_name = card_name.upper()
        if not buy_phase: #ACTION
            if upper_name in select_list:
                return select_list.index(upper_name)
            else:
                #balancer
                strategy = self.balancer()
                hand_num =  self.select_action(select_list, strategy)
                return hand_num
        else:
            if upper_name in select_list:
                return select_list.index(upper_name)
            else:
                #balancer
                strategy = self.balancer()
                buy_num = self.select_buy(select_list, strategy)
                return buy_num








    def make_decision(self, board):
        """
        this simply just needs to do a buy or play decision
        Generally we play actions until those are 0 or 1, then buy depending on our strategy
        After that end turn if no buys or actions
        if they have >= 8  coins, will buy a province

        basically the simulations either choose an action or a buy
        """
        #this is true for all strategies
        buy_phase = False
        if self.my_player.buys == 0:
            self.my_player.end_turn()
            return "end"
        if self.my_player.actions == 0:
            buy_phase = True

        #self.print_board(board)
        actionable_cards = self.get_playable_cards()
        buyable = self.get_can_buy(board)
        #now strategy specific
        if self.strategy_name == "random":
            if not buy_phase:
                #time to play actions
                if len(actionable_cards) == 0:
                    self.my_player.actions = 0
                else:
                    if len(actionable_cards) == 1:
                        hand_num = actionable_cards[0]
                    else:
                        hand_num = actionable_cards[random.randint(0,len(actionable_cards) - 1)]
                    selected_card = self.my_player.hand[hand_num]
                    #print("playing " + selected_card.name)
                    try:
                        selected_card.do_action(board, self.my_player)
                        self.my_player.hand.pop(hand_num) #TODO only pop if it was played successfully
                        self.my_player.played.append(selected_card)
                        self.my_player.actions -= 1
                    except Exception as e:
                        self.my_player.actions = 0
                        print(e)
                        print("cannot play that card, moving to buys instead")
            else:
                if len(buyable) == 0:
                    #no money to buy
                    self.my_player.buys = 0
                    return
                elif "PROVINCE" in buyable:
                    buy_num = buyable.index("PROVINCE")
                elif len(buyable) == 1:
                    buy_num = 0
                else:
                    buy_num = random.randint(0,len(buyable) - 1)

                choice = buyable[buy_num]
                if not board.buy(choice, self.my_player):
                    print("Unable to buy that card")


        elif self.strategy_name == "max_actions" or self.strategy_name == "max_money":
            if not buy_phase:
                #time to play actions
                if len(actionable_cards) == 0:
                    self.my_player.actions = 0
                else:
                    if len(actionable_cards) == 1:
                        hand_num = actionable_cards[0]
                    else:
                        hand_num =  self.select_action(actionable_cards, self.strategy_name)
                    selected_card = self.my_player.hand[hand_num]
                    #print("playing " + selected_card.name)
                    try:
                        selected_card.do_action(board, self.my_player)
                        self.my_player.hand.pop(hand_num) #TODO only pop if it was played successfully
                        self.my_player.played.append(selected_card)
                        self.my_player.actions -= 1
                    except Exception as e:
                        print(e)
                        self.my_player.actions = 0
                        print("cannot play that card, moving to buys instead")

            else:
                if len(buyable) == 0:
                    #no money to buy
                    self.my_player.buys = 0
                    return
                elif "PROVINCE" in buyable:
                    buy_num = buyable.index("PROVINCE")
                elif len(buyable) == 1:
                    buy_num = 0
                else:
                    buy_num = self.select_buy(buyable, self.strategy_name)
                choice = buyable[buy_num]
                if not board.buy(choice, self.my_player):
                    print("Unable to buy that card")
        elif self.strategy_name == "balance":
            if not buy_phase:
                #time to play actions
                if len(actionable_cards) == 0:
                    self.my_player.actions = 0
                else:
                    if len(actionable_cards) == 1:
                        hand_num = actionable_cards[0]
                    else:
                        strategy = self.balancer()
                        hand_num =  self.select_action(actionable_cards, strategy)
                    selected_card = self.my_player.hand[hand_num]
                    #print("playing " + selected_card.name)
                    try:
                        selected_card.do_action(board, self.my_player)
                        self.my_player.hand.pop(hand_num) #TODO only pop if it was played successfully
                        self.my_player.played.append(selected_card)
                        self.my_player.actions -= 1
                    except Exception as e:
                        print(e)
                        self.my_player.actions = 0
                        print("cannot play that card, moving to buys instead")

            else:
                if len(buyable) == 0:
                    #no money to buy
                    self.my_player.buys = 0
                    return
                elif "PROVINCE" in buyable:
                    buy_num = buyable.index("PROVINCE")
                elif len(buyable) == 1:
                    buy_num = 0
                else:
                    strategy = self.balancer()
                    buy_num = self.select_buy(buyable, strategy)
                choice = buyable[buy_num]
                if not board.buy(choice, self.my_player):
                    print("Unable to buy that card")


        #CARD STRATEGIES
        elif self.strategy_name == "festival" or self.strategy_name == "market":
            if not buy_phase:
                #time to play actions
                if len(actionable_cards) == 0:
                    self.my_player.actions = 0
                else:
                    if len(actionable_cards) == 1:
                        hand_num = actionable_cards[0]
                    else:
                        hand_num = self.play_card_strat(buy_phase, actionable_cards, self.strategy_name)

                    selected_card = self.my_player.hand[hand_num]
                    #print("playing " + selected_card.name)
                    try:
                        selected_card.do_action(board, self.my_player)
                        self.my_player.hand.pop(hand_num) #TODO only pop if it was played successfully
                        self.my_player.played.append(selected_card)
                        self.my_player.actions -= 1
                    except Exception as e:
                        print(e)
                        self.my_player.actions = 0
                        print("cannot play that card, moving to buys instead")

            else:
                if len(buyable) == 0:
                    #no money to buy
                    self.my_player.buys = 0
                    return
                elif "PROVINCE" in buyable:
                    buy_num = buyable.index("PROVINCE")
                elif len(buyable) == 1:
                    buy_num = 0
                else:
                    buy_num = self.play_card_strat(buy_phase, buyable, self.strategy_name)
                choice = buyable[buy_num]
                if not board.buy(choice, self.my_player):
                    print("Unable to buy that card")
        else:
            print("Invalid Strategy Name", self.strategy_name)
