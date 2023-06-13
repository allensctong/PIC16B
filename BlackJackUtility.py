# -*- coding: utf-8 -*-
"""
Created on Mon May 22 17:56:12 2023

@author: huang
"""

import numpy as np
import matplotlib.pyplot as plt


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


def plot_value_function(V):
    '''
    plot the estimated value function for blackjack 
    Args:
      V: a dictionary of estimated values for blackjack 
    Returns:  N/A 
    '''
    # range of sum in player's hand 
    player = [state[0]  for state in V.keys()]
    max_player = max(player)
    min_player = min(player)
    player_range = np.arange(min_player, 22, 1) 

    # range of sum in dealer's hand
    # based on the set up of the environment, prob can assume >= 17 in the end (?)
    dealer = [state[1]  for state in V.keys()]
    max_dealer = max(dealer)
    min_dealer = min(dealer)
    dealer_range = np.arange(min_dealer, 11, 1) # the environment starts at 11 (?)

    # empty array for the value function 
      # first access in the players score 
      # second is the dealer, 
      # third is if there is an ace (i.e. soft)
    V_plot = np.zeros((21-min_player + 1, max_dealer - min_dealer + 1, 2))

    # mesh grid for plotting 
    X,Y = np.meshgrid(dealer_range, player_range)

    # populate an array of values for different scores not including losing scores 
    for (player,dealer,ace),v in V.items():
        if player<=21 and dealer<=21: # so if both didn't bust
            V_plot[player-min_player, dealer-min_dealer, (1*ace)] = V[(player, dealer, ace)]

    # plot surface        
    fig, ax = plt.subplots(nrows=1, ncols=2, subplot_kw={'projection': '3d'})
    ax[0].plot_wireframe(X,Y, V_plot[:,:,0])
    ax[0].set_title('no ace')
    ax[0].set_xlabel('dealer')
    ax[0].set_ylabel('player ')
    ax[0].set_zlabel('value function')
    ax[1].plot_wireframe(X,Y, V_plot[:,:,1])
    ax[1].set_title('no ace')
    ax[1].set_xlabel('dealer')
    ax[1].set_ylabel('player ')
    ax[1].set_zlabel('value function')
    ax[1].set_title(' ace')
    fig.tight_layout()
    plt.show()

    # plot top view of the surface     
    fig, ax = plt.subplots(nrows=1, ncols=2)
    ax[0].imshow((V_plot[:,:,0]),extent =[1,10,21,4])
    ax[0].set_title('no ace')
    ax[0].set_xlabel('dealer')
    ax[0].set_ylabel('player ')   
    im=ax[1].imshow(V_plot[:,:,1],extent =[1,10,21,4])
    ax[1].set_title('ace')
    ax[1].set_xlabel('dealer')
    fig.colorbar(im, ax=ax[1])
    
    
def plot_policy_blackjack(policy):
    '''
    plot the policy for blackjack 
    Args:
      policy: a dictionary of estimated values for blackjack 
    Returns:  N/A 
    '''  
    # range of player score 
    player = [state[0] for state in policy.keys()]
    max_player = max(player)
    min_player = min(player)

    player_range = np.arange(min_player, 22, 1) # min_player=12 based on the environment set up

    # range of dealer score      
    dealer = [state[1]  for state in policy.keys()]
    max_dealer = max(dealer)
    min_dealer = min(dealer)
    dealer_range = np.arange(min_dealer, 11, 1)

    # empty array for the value function
      # first access in the players score 
      # second is the dealer, 
      # third is if there is an ace    
    policy_plot = np.zeros((21-min_player+1, max_dealer-min_dealer+1, 2))

    # create a mesh grid for plotting 
    X,Y = np.meshgrid(dealer_range,player_range)
    
    
    # populate an array  of values for different  policy not including losing states above 21 
    for (player,dealer,ace),v in policy.items():
        if player<=21 and dealer<=10 and player>=min_player:
            policy_plot[player-min_player,dealer-min_dealer,(1*ace)] = policy[(player, dealer, ace)]

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(5, 5))   
    ax[0].imshow((policy_plot[:,:,0]),cmap=plt.get_cmap('inferno', 2),extent =[1,10,21,4])
    ax[0].set_title('no ace (hard)')
    ax[0].set_xlabel('dealer')
    ax[0].set_ylabel('player')    
    ax[0].invert_yaxis()

    ax[1].set_title('with ace (soft)')
    ax[1].set_xlabel('dealer')
    ax[1].imshow(policy_plot[:,:,1],cmap=plt.get_cmap('inferno', 2), extent =[1,10,21,4])
    # fig.colorbar(im, ax=ax[1], ticks=[0 , 1])
    # plt.gca().invert_yaxis()  
    ax[1].invert_yaxis() 
    

def average_wins(environment, policy=None, episodes=10):
    '''
    This function calculates the average number of wins for a game of blackjack given a policy.
    If no policy is provided a random policy is selected.
    Args:
      environment:AI gym balckjack envorment object 
      policy:policy for blackjack if none a random  action will be selected 
      episodes: number of episodes 
    Returns: 
      average_wins: the average number of wins 
      std_wins: the average number of wins 
    '''
    win_loss = np.zeros(episodes)

    for episode in range(episodes):
        state = environment.reset()
        done = False

        while not done:
            if policy and isinstance(policy[state],np.int64):
                action = policy[state]
                
            else:
                action = environment.action_space.sample() # check back later (!!)

            state, reward, done, info = environment.step(action)
        result = game_result(environment, state, show=False)
        if reward == 1:
            win_loss[episode] = 1 # win
        else:
            win_loss[episode] = 0 # lose

    # compute the average wins and the standard deviation
    average_wins = win_loss.mean()
    std_win = win_loss.std()/np.sqrt(episodes)

    return average_wins ,std_win