# nbdev_cards

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

A deck of cards demo of [nbdev](https://nbdev.fast.ai) based on ideas
from [Think Python 2nd
Edition](https://greenteapress.com/wp/think-python-2e/) by Allen B.
Downey.

## Install

Install using:

``` sh
pip install nbdev-cards
```

or

``` sh
conda install -c fastai nbdev-cards
```

## How to use

This lib provides a
[`Card`](https://JohnRomanelis.github.io/nbdev_cards/cards.html#card)
class you can use to create, display, and compare playing cards:

``` python
Card(1,3)
```

    3♦

Suits are numbered according to this list:

``` python
suits
```

    ['♣', '♦', '♥', '♠']
