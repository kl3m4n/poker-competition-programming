# Small competitve programming side project

It's a school project and my goal with this project is to test the `unittest` library, in addition to passing the main topic which is to compare 2 poker hands

# How to launch

Simply with this command : `python3 -m unittest test.py` (no librairies needed)

# Some technical indications

The `who_is_the_winner_my_boyyy` method of the game class returns -1 for a draw, 0 if player/hand 1 won and 1 if player/hand 2 won

And the `how_he_won` method, again for the game class, returns :
- -1 for highest card
- 0 for a pair
- 1 for double pair
- 2 for a brelan
- 3 for a suite
- 4 for a color
- 5 for a full
- 6 for a square
- 7 for a flush
