# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_cards.ipynb.

# %% auto 0
__all__ = ['suits', 'ranks', 'Card']

# %% ../nbs/00_cards.ipynb 3
from fastcore.utils import * 

# %% ../nbs/00_cards.ipynb 4
suits = ["\u2663", "\u2666", "\u2665", "\u2660"]
ranks = [None, "A"] + [str(i) for i in range(2, 11)] + ["J", "Q", "K"]

# %% ../nbs/00_cards.ipynb 13
class Card:
    "A playing card"
    def __init__(self, 
                 suit:int,  # An index into `suits`
                 rank:int): # Am index into `ranks`
        self.suit, self.rank = suit, rank
    def __str__(self): return f"{ranks[self.rank]}{suits[self.suit]}"
    __repr__ = __str__

# %% ../nbs/00_cards.ipynb 19
@patch
def __eq__(self:Card, a:Card): return (self.suit, self.rank) == (a.suit, a.rank)
@patch
def __lt__(self:Card, a:Card): return (self.suit, self.rank) < (a.suit, a.rank)
@patch 
def __gt__(self:Card, a:Card): return (self.suit, self.rank) > (a.suit, a.rank)
