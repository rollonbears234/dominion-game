"""
This is the interface used to play a game

This takes a board game and players and


print game state after every move
redraw a hand so a user has 5 and reshuffle after every move, but they don't play until after


This is the mother of the game, it makes sure people are deducted gold, deducted buys, it ends turns, etc.
Makes sure the player has enough money to buy the card by comparing gold to card cost
"""

import player
import game_board
import random
import strategies


class Play():

    def __init__(self, mode = "users"):
            if mode == "users":
                self.game_board = game_board.Game_Board()
                self.curr_turn = random.randint(0, self.game_board.num_players() - 1)
                self.play()
            elif mode == "sim":
                self.game_board = game_board.Game_Board(True)
                print("Here are the strategies: ", strategies.strategies)
                raw_strategies = raw_input("CSV of strategies you want: ")
                self.simulate(raw_strategies.split(","))

    def print_board(self):
        """
        prints current board, so piles available, etc.
        put it here so they can see board state as they play
        """
        for card in self.game_board.stock_piles.keys():
            if len(self.game_board.stock_piles[card]) > 0:
                print("Stockpile", card, "cost " +  str(game_board.CARD_INFO[card]["cost"]))
        print("Golds", len(self.game_board.golds))
        print("Silvers", len(self.game_board.silvers))
        print("Coppers", len(self.game_board.coppers))
        print("Victory Cards", self.game_board.victory.keys()) #DUCHY or another might be 0

    def next_player(self):
        """
        rotates to the next player, use mod
        """
        self.curr_turn = (1 + self.curr_turn) % self.game_board.num_players()

    def select(self, player):
        # I like abstracting this to the player, it makes more sense for them to just return the card they want
        #but how do you say, 1) discrd, 2) draw 3) discard?
        # ugh
        """
        maybe use this for dialogue with the current user
        """
        print("Make your move, here is your hand " + player.player_name)
        print("Commands (the space is important): \n end: ends your turn \n play #: will play the #th card in your hand \n buy CARD_NAME: will buy the CARD_NAME from the game board, this can be money, a stockpile, or a victory card\n")
        player.print_hand()
        move_choice = raw_input("Command: ")
        move_choice = move_choice.split(" ")
        if move_choice[0] == "end":
            return False
        elif len(move_choice) == 2:

            print(move_choice)
            if move_choice[0] == "play":
                #get the card and pass in game_board and player
                if player.actions > 0:
                    try:
                        hand_num = int(move_choice[1])
                        selected_card = player.hand[hand_num]
                        print("playing " + selected_card.name)
                        selected_card.do_action(self.game_board, player)
                        #need to move card from player_hand to player played
                        player.hand.pop(hand_num) #only pop if it was played successfully
                        player.played.append(selected_card)
                        player.actions -= 1
                        player.recalc()
                    except Exception as e:
                        print("Invalid Input for play, try again")
                        print(e)
                else:
                    print("You do not have actions to play")
            elif move_choice[0] == "buy":
                #get the card and pass in game_board and player
                try:
                    choice_cap = move_choice[1].upper()
                    if not self.game_board.buy(choice_cap, player):
                        print("Unable to buy that card, here is the game board again: \n")
                        self.print_board()
                except:
                    print("Invalid Input for buy, try again, caps matter")
            else:
                print("Invalid Command, try again")
        elif move_choice[0] == "finish":
            self.game_board.victory["PROVINCE"] = []
        else:
            print("Invalid Input, try again, caps matter")

        print("\n")

    def play_turn(self):
        curr_player = self.game_board.players[self.curr_turn]
        print("Starting " + curr_player.player_name + "'s turn \n")
        self.print_board()

        end_turn = False
        while not end_turn:
            if self.select(curr_player) == False:
                end_turn = True

        print("\n")
        curr_player.end_turn()

    def winner(self):
        """
        I do not check for Ties
        """
        max_player = self.game_board.players[self.curr_turn] #current player
        max_score = 0
        for player in self.game_board.players:
            curr_score = 0
            num_gardens = 0
            player.deck_all()
            for card in player.deck:
                if card.name == "GARDENS":
                    num_gardens += 1
                elif card.name in game_board.VICTORY_CARDS:
                    curr_score += game_board.CARD_INFO[card.name]["points"]
            curr_score += num_gardens*(len(player.deck)/ 10)

            if curr_score > max_score:
                max_score = curr_score
                max_player = player
            elif curr_score == max_score:
                print("There was a tie, first player counter wins!")
        return max_player

    def play(self):
        while not self.game_board.game_over():
            #player makes a move
            self.next_player()
            self.play_turn()
        print("GAME OVER!")
        win_player  = self.game_board.players[self.curr_turn]
        print("The winner is " + win_player.player_name)

    def simulate(self, strategy_list):
        """
        similar to play but this puts the strategies against each other

        strategy_list: string of strategies
        """
        game_strategies = []
        sim_name = 0
        for str_strat in strategy_list:
            game_strategies.append(strategies.Strategy(str_strat, str(sim_name)))
            sim_name += 1

        #need to initialize game board players
        game_board.players = [strat.my_player for strat in game_strategies]

        #simulation loop
        curr_strat_index = random.randint(0, len(game_strategies) - 1)
        while not self.game_board.game_over(): #rotate through strategy objects until game ends
            #player makes a move
            curr_strat_index = (1 + self.curr_strat_index) % len(game_strategies)
            curr_sim = game_strategies[curr_strat_index]
            sim_ended = False
            while not sim_ended: #simulation plays until it ends (this should always happen)
                sim_move = curr_sim.make_decision(self.game_board)
                if sim_move== "end":
                    sim_ended == True

        print("GAME OVER!")
        win_sim  = game_strategies[curr_strat_index].strategy_name
        print("The winner is " + win_sim)


if __name__ == '__main__':
    print("Beginning a game")
    mode = raw_input("Select a mode (users, sim): ")
    game = Play(mode)
