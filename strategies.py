"""
Used to make my strategies testing in the play

Beginning strategies should default to buying a province if they have money -> get some convergence
"""
import player
import game_board
import random


strategies = ["random", "max_actions", "max_money", "balance"]

working_cards = ["MOAT", "MERCHANT", "VASSAL", "VILLAGE",
            "GARDENS", "MONEYLENDER", "SMITHY",
            "COUNCIL ROOM", "FESTIVAL", "LABORATORY", "MARKET"]
# removed MILITIA until discard_to is random


class Strategy():


    """
    will have an interface for decision making (buy or play or end)
    will differ those decisions based on the strategy name
    """

    def __init__(self, strategy_name , sim_name):
        self.strategy_name = strategy_name
        self.sim_name = sim_name
        self.my_player = player.Player("simulation " + sim_name, strategy = strategy_name)


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

        #now strategy specific
        if self.strategy_name == "random":
            if not buy_phase:
                #time to play actions
                actionable_cards = self.get_playable_cards()
                if len(actionable_cards) == 0:
                    self.my_player.actions = 0
                else:
                    if len(actionable_cards) == 1:
                        hand_num = actionable_cards[0]
                    else:
                        hand_num = actionable_cards[random.randint(0,len(actionable_cards) - 1)]
                    selected_card = self.my_player.hand[hand_num]
                    #print("playing " + selected_card.name)
                    selected_card.do_action(board, self.my_player)
                    self.my_player.hand.pop(hand_num) #TODO only pop if it was played successfully
                    self.my_player.played.append(selected_card)
                    self.my_player.actions -= 1
            else:
                buyable = self.get_can_buy(board)
                if len(buyable) == 0:
                    #no money to buy
                    self.my_player.buys = 0
                    return
                elif len(buyable) == 1:
                    buy_num = 0
                else:
                    buy_num = random.randint(0,len(buyable) - 1)
                choice = buyable[buy_num]
                if not board.buy(choice, self.my_player):
                    print("Unable to buy that card")


        elif self.strategy_name == "max_actions":
            if not buy_phase:
                #time to play actions
                actionable_cards = self.get_playable_cards()
                if len(actionable_cards) == 0:
                    self.my_player.actions = 0
                else:
                    if len(actionable_cards) == 1:
                        hand_num = actionable_cards[0]
                    else:
                        hand_num = actionable_cards[random.randint(0,len(actionable_cards) - 1)]
                    selected_card = self.my_player.hand[hand_num]
                    #print("playing " + selected_card.name)
                    selected_card.do_action(board, self.my_player)
                    self.my_player.hand.pop(hand_num) #TODO only pop if it was played successfully
                    self.my_player.played.append(selected_card)
                    self.my_player.actions -= 1
            else:
                buyable = self.get_can_buy(board)
                if len(buyable) == 0:
                    #no money to buy
                    self.my_player.buys = 0
                    return
                elif len(buyable) == 1:
                    buy_num = 0
                else:
                    buy_num = random.randint(0,len(buyable) - 1)
                choice = buyable[buy_num]
                if not board.buy(choice, self.my_player):
                    print("Unable to buy that card")
        elif self.strategy_name == "max_money":
            pass
        elif self.strategy_name == "balance":
            pass
        else:
            print("Invalid Strategy Name", self.strategy_name)
