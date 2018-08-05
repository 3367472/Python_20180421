# encoding: utf-8
from pprint import pprint
from random import shuffle

values = list(range(1, 11)) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v, s) for v in values for s in suits]

pprint(deck[:12])
shuffle(deck)
pprint(deck[:12])

while deck:
    input(deck.pop())
