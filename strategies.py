"""
Used to make my strategies testing in the play

Beginning strategies should default to buying a province if they have money -> get some convergence
"""
import player
import game_board


strategies = ["random", "max_actions", "max_money", "balance"]

working_cards = ["MOAT", "MERCHANT", "VASSAL", "VILLAGE",
            "GARDENS", "MILITIA", "MONEYLENDER", "SMITHY",
            "COUNCIL ROOM", "FESTIVAL", "LABORATORY", "MARKET"]


class Strategy():


    """
    will have an interface for decision making (buy or play or end)
    will differ those decisions based on the strategy name
    """

    def __init__(self, strategy_name , sim_name):
        self.strategy_name = strategy_name
        self.sim_name = sim_name
        self.my_player = player.Player("simulation " + sim_name, strategy = strategy_name)


    def get_playable_cards(self, board):
        """
        returns list of cards my player can play from the hand
        that is, money >= card cost and buy >= 0

        this is just like console so the answer is an index
        """
        can_play =


    def get_buyable_cards(self):
        """
        returns a list of cards I can possibly buy
        """
        if player.buys >= 0:
            available = []
            for card_name in self.board.stock_piles.keys():
                if len(self.board.stock_piles[card_name]) > 0 and self.board.stock_piles[card_name][0].cost <= player.money:
                    available.append(card_name)
            return available
        else:
            return []

    def make_decision(self, board):
        """
        this simply just needs to do a buy or play decision
        Generally we play actions until those are 0 or 1, then buy depending on our strategy
        After that end turn if no buys or actions
        if they have >= 8  coins, will buy a province

        doing an action:

        hand_num = int(move_choice[1])
        selected_card = player.hand[hand_num]
        print("playing " + selected_card.name)
        selected_card.do_action(self.game_board, player)
        #need to move card from player_hand to player played
        player.hand.pop(hand_num) #only pop if it was played successfully
        player.played.append(selected_card)
        player.actions -= 1
        player.recalc()

        buying a card:

        choice_cap = move_choice[1].upper()
        if not self.game_board.buy(choice_cap, player):
            print("Unable to buy that card, here is the game board again: \n")
            self.print_board()


        basically the simulations either choose an action or a buy

        """
        buy_phase = False
        if self.my_player.buys == 0:
            return "end"
        if self.my_player.actions == 0:
            buy_phase = True

        if self.strategy_name == "random":
            pass
        if self.strategy_name == "max_actions":
            pass
        if self.strategy_name == "max_money":
            pass
        if self.strategy_name == "balance":
            pass
        else:
            print("Invalid Strategy Name")
