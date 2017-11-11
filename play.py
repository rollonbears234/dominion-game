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
            self.game_board = game_board()
            self.curr_turn = random.randint(0, self.game_board.num_players() - 1)
            self.play()

    def print_board(self):
        """
        prints current board, so piles available, etc.
        put it here so they can see board state as they play
        """
        for card in self.game_board.stock_piles.keys():
            if len(self.game_board.stock_piles[card]) > 0:
                print("Stockpile", self.game_board.stock_piles)
        print("Golds", len(self.game_board.golds))
        print("Silvers", len(self.game_board.silvers))
        print("Coppers", len(self.game_board.coppers))
        print("Victory Cards", self.game_board.victory)

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
        player.print_hand()
        card_choices = raw_input("Please enter something: ")

    def play_turn(self):
        self.print_board()
        curr_player = self.game_board.players[self.curr_turn]
        end_turn = False
        while not end_turn:
            self.select(curr_player)
        curr_player.end_turn()
        self.next_player()

    def play(self):
        while not game_board.game_over():
            #player makes a move
            self.play_turn()
