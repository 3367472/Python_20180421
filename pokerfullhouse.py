# encoding: utf-8

import random


def is_full_house(cards):
    cards.sort()
    print(cards, end='\t')
    cards_group = list(set(cards))
    if 0 not in cards:
        if len(cards_group) == 2:
            if cards.count(cards_group[0]) in (2, 3):
                print('It\'s full house!')
    elif cards.count(0) == 1:
        if len(cards_group) == 3:
            if cards.count(cards_group[1]) in (1, 2, 3):
                print('It\'s full house!')
    elif cards.count(0) == 2:
        if len(cards_group) == 3:
            if cards.count(cards_group[1]) in (1, 2):
                print('It\'s full house!')
        elif len(cards_group) == 2:
            print('It\'s full house!')
    print('Not a full house.')


def random_cards():
    poker = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
        0, 0]
    b = []
    cards = []
    while len(b) < 5:
        a = random.randint(1, 52)
        if a not in b:
            b.append(a)
    for i in b:
        cards.append(poker[i])
    return cards


for i in range(5000):
    cards = random_cards()
    is_full_house(cards)
