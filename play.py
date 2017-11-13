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


class Play():

    def __init__(self):
            self.game_board = game_board.Game_Board()
            self.curr_turn = random.randint(0, self.game_board.num_players() - 1)
            self.play()

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
        print("Make your move, here is your hand")
        print("Commands (the space is important): \n end: ends your turn \n play #: will play the #th card in your hand \n buy CARD_NAME: will buy the CARD_NAME from the game board, this can be money, a stockpile, or a victory card")
        player.print_hand()
        move_choice = raw_input("Command: ")
        move_choice = move_choice.split(" ")
        if move_choice[0] == "end":
            return False
        elif len(move_choice) == 2:

            print(move_choice)
            if move_choice[0] == "play":
                #get the card and pass in game_board and player
                try:
                    selected_card = player.hand.pop(int(move_choice[1]))
                    print("playing " + selected_card.name)
                    selected_card.do_action(self.game_board, player)
                    #need to move card from player_hand to player played
                    player.played.append(selected_card)
                except:
                    player.hand.append(selected_card) #don't want to loose any cards
                    print("Invalid Input for play, try again")
            elif move_choice[0] == "buy":
                #get the card and pass in game_board and player
                try:
                    if not self.game_board.buy(move_choice[1], player):
                        print("Unable to buy that card, here is the game board again:")
                        self.print_board()
                except:
                    print("Invalid Input for buy, try again, caps matter")
            else:
                print("Invalid Command, try again")
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

    def play(self):
        while not self.game_board.game_over():
            #player makes a move
            self.next_player()
            self.play_turn()
        print("GAME OVER!")
        curr_player = self.game_board.players[self.curr_turn]
        print("The winner is " + curr_player.name)

if __name__ == '__main__':
    print("Beginning a game")
    game = Play()
