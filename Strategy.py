# -*- coding: utf-8 -*-
"""
Created on Mon May  8 20:07:51 2023

@author: huang
"""
# this is an implementation based on “https://www.vegashowto.com/blackjack-basic-strategy”
# no splitting pairs

def basic_strategy(player_total, dealer_value, soft):

    if 4 <= player_total <= 8:
        return 'hit'
    if player_total == 9:
        if dealer_value in [1,2,7,8,9,10]:
            return 'hit'
        return 'double'
    if player_total == 10:
        if dealer_value in [1, 10]:
            return 'hit'
        return 'double'
    if player_total == 11:
        if dealer_value == 1:
            return 'hit'
        return 'double'
    if soft: #soft total above 11
        #we only double soft 12 because there's no splitting
        if player_total in [12, 13, 14]:
            if dealer_value in [5, 6]:
                return 'double'
            return 'hit'
        if player_total in [15, 16]:
            if dealer_value in [4, 5, 6]:
                return 'double'
            return 'hit'
        if player_total == 17:
            if dealer_value in [3, 4, 5, 6]:
                return 'double'
            return 'hit'
        if player_total == 18:
            if dealer_value in [3, 4, 5, 6]:
                return 'double'
            if dealer_value in [2, 7, 8]:
                return 'stand'
            return 'hit'
        if player_total >= 19:
            return 'stand'

    else: # hand total above 11
        if player_total == 12:
            if dealer_value in [1, 2, 3, 7, 8, 9, 10]:
                return 'hit'
            return 'stand'
        if player_total in [13, 14, 15, 16]:
            if dealer_value in [2, 3, 4, 5, 6]:
                return 'stand'
            return 'hit'

        if player_total >= 17:
            return 'stand'
