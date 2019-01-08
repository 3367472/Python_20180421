# encoding: utf-8

import random
from collections import Counter


def is_full_house(cards):
    total = len(cards)
    cnt = Counter(cards)
    cards.sort()
    # print(cards, end='\t')
    nums = len(cnt)
    if cnt[0] == 0 and nums == 2:
        if cnt.most_common(1)[0][1] == round(total / 2):
            print(cards, end='\t')
            print('It\'s full house!')
    elif cnt[0] == 1 and nums == 3:
        print(cards, end='\t')
        print('It\'s full house!')
    elif cnt[0] == 2 and nums in (2, 3):
        print(cards, end='\t')
        print('It\'s full house!')
    # print('Not a full house.')


poker = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    0, 0]


for i in range(10000):
    cards = random.sample(poker, 5)
    is_full_house(cards)
