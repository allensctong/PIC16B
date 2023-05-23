# -*- coding: utf-8 -*-
"""
Created on Mon May 22 17:56:12 2023

@author: huang
"""

import numpy as np

def get_total(Input):
    """
    This function will calculate the maximum total of a hand in 21. 
    It will also take into consideration if the Deck has aces.  

    Returns: 
    Maxmum value of a deck of card 
    Args:
    Input:List of numbers representing  a hand 

    """
    Input = np.array(Input) # maximum player hand under or equal to 21 
    Max = 0
    
    # check if the hand has an ace
    if 1 in set(Input):
        
        # put all aces in one array and all other cards in a second array 
        aces = Input[Input==1] 
        not_aces=Input[Input!=1]
        
        # try different posable combinations of aces as 1 or 11 
        for ace in range(len(aces)+1):
            # convert each  ace to an 11 
            aces[0:ace] = 11
            # find the total of a particular combination 
            total = aces.sum()+not_aces.sum()
            # check if the total is 21 
            if total == 21:
                Max = 21
                break
            # check if the total is larger than Max value but less than 22 

            elif total>Max and total<22:
                # if so total is new max
                Max = total

    else:
        # determine  sum if no aces in the deck 
        Max=sum(Input)

    return Max  

def game_result (environment,state,show=True):
    '''
    this function  will determine the results of  a game  of Black Jack after an episode only  tested for open AI  gym 
    Returns: 
    result:   used to debug result of a game like open AI  gym +1,drawing is 0, and losing is -1, None for error 
    Args:
    environment: open ai gym black jack environment
    state: state of open ai gym black jack environment
    '''
    if show:
        print(f"state: {state}")
        print(f"player has {environment.player}")
        print(f"the players current sum:{state[0]}, dealer's one showing card:{state[1]}, usable ace:{state[2]}")
    dealer_sum = get_total(environment.dealer)
    result = None
    if show:
        print(f"dealer cards: {environment.dealer}, dealer score: {dealer_sum}")
        print(f"your score: {state[0]}")
        
    if state[0] > 21:
        if show:
            print("Bust")
        result = -1
    elif dealer_sum > 21:
        
        if show:
            print("agent wins :)")
        result = 1  
        
    elif state[0]>dealer_sum and state[0]<22:
        if show:
            print("agent wins :)")
        result = 1
        
    elif  state[0]<dealer_sum and dealer_sum<22 : 
        if show:
            print("agent loses :(")
        result = -1
    return result 