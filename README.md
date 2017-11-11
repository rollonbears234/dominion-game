# How to win playing Dominion
_The Base Set_

### Game Setup
You are a monarch, like your parents before you, a ruler of a small pleasant kingdom of rivers and evergreens. Unlike your parents, however, you have hopes and dreams! You want a bigger and more pleasant kingdom, with more rivers and a wider variety of trees. You want a Dominion! In all directions lie fiefs, freeholds, and feodums. All are small bits of land, controlled by petty lords and verging on anarchy. You will bring civilization to these people, uniting them under your banner.

#### Motivation
My roommate introduced me to the game dominion and as of this point, we both have won an equal amount of times. I am a competitive person and want to make sure I end up on top of the leaderboard by the end of the semester. So I decided to use my Statistics 157 final project as an excuse to figure out the best strategy possible.

What makes this game interesting is not only can the game change every time you play due to the different 10 starting cards, but you also change your hand every time your deck runs out. As you build your deck, the probability of getting action cards and money cards changes.

#### General Approach
** First I am testing with a given 10 starting cards and can try how the strategies perform on multiple combinations later.

1. Build a playable version of the game in python
2. Implement multiple different strategies and put them against each other
  * My initial thoughts are we are basically going to choose between buying money every hand, or the best action. The actions should lead us to more actions down the line or more money. We are trying to optimize the money we get every hand.
3. Based on the best strategies, build an assistant that tells you what to play so you can ask it what to play during a real game against friends.
  * This could be based on number of provinces left and whether or not you should take an action card or buy money.  
4. Using the best strategies, simulate data of many moves and game results and use machine learning to train models to beat the game.


### Steps to play

> download and in the downloaded file directory, run play.py

### Report

Download report here for details

### Future Work

Use the python sockets API to let the players play against each other on their own machines, that way you can keep their hand private when decision making.
