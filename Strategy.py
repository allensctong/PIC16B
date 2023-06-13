# -*- coding: utf-8 -*-
"""
Created on Mon May  8 20:07:51 2023

@author: huang
"""
# this is an implementation based on “https://www.vegashowto.com/blackjack-basic-strategy”
# no splitting pairs

basic_strategy = {
         
    # sum 4-8 hit no matter what
    (4, 1, False, False): 1,
    (5, 1, False, False): 1,
    (6, 1, False, False): 1,
    (7, 1, False, False): 1,
    (8, 1, False, False): 1,
    (4, 2, False, False): 1,
    (5, 2, False, False): 1,
    (6, 2, False, False): 1,
    (7, 2, False, False): 1,
    (8, 2, False, False): 1,
    (4, 3, False, False): 1,
    (5, 3, False, False): 1,
    (6, 3, False, False): 1,
    (7, 3, False, False): 1,
    (8, 3, False, False): 1,
    (4, 4, False, False): 1,
    (5, 4, False, False): 1,
    (6, 4, False, False): 1,
    (7, 4, False, False): 1,
    (8, 4, False, False): 1,
    (4, 5, False, False): 1,
    (5, 5, False, False): 1,
    (6, 5, False, False): 1,
    (7, 5, False, False): 1,
    (8, 5, False, False): 1,
    (4, 6, False, False): 1,
    (5, 6, False, False): 1,
    (6, 6, False, False): 1,
    (7, 6, False, False): 1,
    (8, 6, False, False): 1,
    (4, 7, False, False): 1,
    (5, 7, False, False): 1,
    (6, 7, False, False): 1,
    (7, 7, False, False): 1,
    (8, 7, False, False): 1,
    (4, 8, False, False): 1,
    (5, 8, False, False): 1,
    (6, 8, False, False): 1,
    (7, 8, False, False): 1,
    (8, 8, False, False): 1,
    (4, 9, False, False): 1,
    (5, 9, False, False): 1,
    (6, 9, False, False): 1,
    (7, 9, False, False): 1,
    (8, 9, False, False): 1,
    (4, 10, False, False): 1,
    (5, 10, False, False): 1,
    (6, 10, False, False): 1,
    (7, 10, False, False): 1,
    (8, 10, False, False): 1,
    
    # player sum == 9
    (9, 2, False, False): 1,
    (9, 3, False, False): 2,
    (9, 4, False, False): 2,
    (9, 5, False, False): 2,
    (9, 6, False, False): 2,
    (9, 7, False, False): 1,
    (9, 8, False, False): 1,
    (9, 9, False, False): 1,
    (9, 10, False, False): 1,
    (9, 1, False, False): 1,
    
    # player sum == 10
    (10, 2, False, False): 2,
    (10, 3, False, False): 2,
    (10, 4, False, False): 2,
    (10, 5, False, False): 2,
    (10, 6, False, False): 2,
    (10, 7, False, False): 2,
    (10, 8, False, False): 2,
    (10, 9, False, False): 2,
    (10, 10, False, False): 1,
    (10, 1, False, False): 1,
    
    # player sum == 11
    (11, 2, False, False): 2,
    (11, 3, False, False): 2,
    (11, 4, False, False): 2,
    (11, 5, False, False): 2,
    (11, 6, False, False): 2,
    (11, 7, False, False): 2,
    (11, 8, False, False): 2,
    (11, 9, False, False): 2,
    (11, 10, False, False): 2,
    (11, 1, False, False): 2,
    
    # player sum == 12
    (12, 2, False, False): 1,
    (12, 3, False, False): 1,
    (12, 4, False, False): 0,
    (12, 5, False, False): 0,
    (12, 6, False, False): 0,
    (12, 7, False, False): 1,
    (12, 8, False, False): 1,
    (12, 9, False, False): 1,
    (12, 10, False, False): 1,
    (12, 1, False, False): 1,
    
    # player sum == 13
    (13, 2, False, False): 0,
    (13, 3, False, False): 0,
    (13, 4, False, False): 0,
    (13, 5, False, False): 0,
    (13, 6, False, False): 0,
    (13, 7, False, False): 1,
    (13, 8, False, False): 1,
    (13, 9, False, False): 1,
    (13, 10, False, False): 1,
    (13, 1, False, False): 1,
    
    # player sum == 14
    (14, 2, False, False): 0,
    (14, 3, False, False): 0,
    (14, 4, False, False): 0,
    (14, 5, False, False): 0,
    (14, 6, False, False): 0,
    (14, 7, False, False): 1,
    (14, 8, False, False): 1,
    (14, 9, False, False): 1,
    (14, 10, False, False): 1,
    (14, 1, False, False): 1,
    
    # player sum == 15
    (15, 2, False, False): 0,
    (15, 3, False, False): 0,
    (15, 4, False, False): 0,
    (15, 5, False, False): 0,
    (15, 6, False, False): 0,
    (15, 7, False, False): 1,
    (15, 8, False, False): 1,
    (15, 9, False, False): 1,
    (15, 10, False, False): 1,
    (15, 1, False, False): 1,
    
    # player sum == 16
    (16, 2, False, False): 0,
    (16, 3, False, False): 0,
    (16, 4, False, False): 0,
    (16, 5, False, False): 0,
    (16, 6, False, False): 0,
    (16, 7, False, False): 1,
    (16, 8, False, False): 1,
    (16, 9, False, False): 1,
    (16, 10, False, False): 1,
    (16, 1, False, False): 1,
    
    # player sum == 17
    (17, 2, False, False): 0,
    (17, 3, False, False): 0,
    (17, 4, False, False): 0,
    (17, 5, False, False): 0,
    (17, 6, False, False): 0,
    (17, 7, False, False): 0,
    (17, 8, False, False): 0,
    (17, 9, False, False): 0,
    (17, 10, False, False): 0,
    (17, 1, False, False): 0,
    
    # player sum == 18
    (18, 2, False, False): 0,
    (18, 3, False, False): 0,
    (18, 4, False, False): 0,
    (18, 5, False, False): 0,
    (18, 6, False, False): 0,
    (18, 7, False, False): 0,
    (18, 8, False, False): 0,
    (18, 9, False, False): 0,
    (18, 10, False, False): 0,
    (18, 1, False, False): 0,
    
    # player sum == 19
    (19, 2, False, False): 0,
    (19, 3, False, False): 0,
    (19, 4, False, False): 0,
    (19, 5, False, False): 0,
    (19, 6, False, False): 0,
    (19, 7, False, False): 0,
    (19, 8, False, False): 0,
    (19, 9, False, False): 0,
    (19, 10, False, False): 0,
    (19, 1, False, False): 0,
    
    # player sum == 20
    (20, 2, False, False): 0,
    (20, 3, False, False): 0,
    (20, 4, False, False): 0,
    (20, 5, False, False): 0,
    (20, 6, False, False): 0,
    (20, 7, False, False): 0,
    (20, 8, False, False): 0,
    (20, 9, False, False): 0,
    (20, 10, False, False): 0,
    (20, 1, False, False): 0,
    
    # player sum == 21
    (21, 2, False, False): 0,
    (21, 3, False, False): 0,
    (21, 4, False, False): 0,
    (21, 5, False, False): 0,
    (21, 6, False, False): 0,
    (21, 7, False, False): 0,
    (21, 8, False, False): 0,
    (21, 9, False, False): 0,
    (21, 10, False, False): 0,
    (21, 1, False, False): 0,
   
    ## usable ace == True
    # player sum == 13
    (13, 2, True, False): 1,
    (13, 3, True, False): 1,
    (13, 4, True, False): 1,
    (13, 5, True, False): 2,
    (13, 6, True, False): 2,
    (13, 7, True, False): 1,
    (13, 8, True, False): 1,
    (13, 9, True, False): 1,
    (13, 10, True, False): 1,
    (13, 1, True, False): 1,
    
    # player sum == 14
    (14, 2, True, False): 1,
    (14, 3, True, False): 1,
    (14, 4, True, False): 1,
    (14, 5, True, False): 2,
    (14, 6, True, False): 2,
    (14, 7, True, False): 1,
    (14, 8, True, False): 1,
    (14, 9, True, False): 1,
    (14, 10, True, False): 1,
    (14, 1, True, False): 1,
    
    # player sum == 15
    (15, 2, True, False): 1,
    (15, 3, True, False): 1,
    (15, 4, True, False): 2,
    (15, 5, True, False): 2,
    (15, 6, True, False): 2,
    (15, 7, True, False): 1,
    (15, 8, True, False): 1,
    (15, 9, True, False): 1,
    (15, 10, True, False): 1,
    (15, 1, True, False): 1,
    
    # player sum == 16
    (16, 2, True, False): 1,
    (16, 3, True, False): 1,
    (16, 4, True, False): 2,
    (16, 5, True, False): 2,
    (16, 6, True, False): 2,
    (16, 7, True, False): 1,
    (16, 8, True, False): 1,
    (16, 9, True, False): 1,
    (16, 10, True, False): 1,
    (16, 1, True, False): 1,
    
    # player sum == 17
    (17, 2, True, False): 1,
    (17, 3, True, False): 2,
    (17, 4, True, False): 2,
    (17, 5, True, False): 2,
    (17, 6, True, False): 2,
    (17, 7, True, False): 1,
    (17, 8, True, False): 1,
    (17, 9, True, False): 1,
    (17, 10, True, False): 1,
    (17, 1, True, False): 1,
    
    # player sum == 18
    (18, 2, True, False): 0,
    (18, 3, True, False): 2,
    (18, 4, True, False): 2,
    (18, 5, True, False): 2,
    (18, 6, True, False): 2,
    (18, 7, True, False): 0,
    (18, 8, True, False): 0,
    (18, 9, True, False): 1,
    (18, 10, True, False): 1,
    (18, 1, True, False): 1,
    
    # player sum == 19
    (19, 2, True, False): 0,
    (19, 3, True, False): 0,
    (19, 4, True, False): 0,
    (19, 5, True, False): 0,
    (19, 6, True, False): 0,
    (19, 7, True, False): 0,
    (19, 8, True, False): 0,
    (19, 9, True, False): 0,
    (19, 10, True, False): 0,
    (19, 1, True, False): 0,
    
    # player sum == 20
    (20, 2, True, False): 0,
    (20, 3, True, False): 0,
    (20, 4, True, False): 0,
    (20, 5, True, False): 0,
    (20, 6, True, False): 0,
    (20, 7, True, False): 0,
    (20, 8, True, False): 0,
    (20, 9, True, False): 0,
    (20, 10, True, False): 0,
    (20, 1, True, False): 0,
    
    # player sum == 21
    (21, 2, True, False): 0,
    (21, 3, True, False): 0,
    (21, 4, True, False): 0,
    (21, 5, True, False): 0,
    (21, 6, True, False): 0,
    (21, 7, True, False): 0,
    (21, 8, True, False): 0,
    (21, 9, True, False): 0,
    (21, 10, True, False): 0,
    (21, 1, True, False): 0,
   
    ## usable split == True
    # 2-2
    (4, 2, False, True): 1,
    (4, 3, False, True): 1,
    (4, 4, False, True): 3,
    (4, 5, False, True): 3,
    (4, 6, False, True): 3,
    (4, 7, False, True): 3,
    (4, 8, False, True): 1,
    (4, 9, False, True): 1,
    (4, 10, False, True): 1,
    (4, 1, False, True): 1,
    
    # 3-3
    (6, 2, False, True): 1,
    (6, 3, False, True): 1,
    (6, 4, False, True): 3,
    (6, 5, False, True): 3,
    (6, 6, False, True): 3,
    (6, 7, False, True): 3,
    (6, 8, False, True): 1,
    (6, 9, False, True): 1,
    (6, 10, False, True): 1,
    (6, 1, False, True): 1,
    
    # 4-4
    (8, 2, False, True): 1,
    (8, 3, False, True): 1,
    (8, 4, False, True): 1,
    (8, 5, False, True): 1,
    (8, 6, False, True): 1,
    (8, 7, False, True): 1,
    (8, 8, False, True): 1,
    (8, 9, False, True): 1,
    (8, 10, False, True): 1,
    (8, 1, False, True): 1,
    
    # 5-5
    (10, 2, False, True): 2,
    (10, 3, False, True): 2,
    (10, 4, False, True): 2,
    (10, 5, False, True): 2,
    (10, 6, False, True): 2,
    (10, 7, False, True): 2,
    (10, 8, False, True): 2,
    (10, 9, False, True): 2,
    (10, 10, False, True): 1,
    (10, 1, False, True): 1,
    
    # 6-6
    (12, 2, False, True): 1,
    (12, 3, False, True): 3,
    (12, 4, False, True): 3,
    (12, 5, False, True): 3,
    (12, 6, False, True): 3,
    (12, 7, False, True): 1,
    (12, 8, False, True): 1,
    (12, 9, False, True): 1,
    (12, 10, False, True): 1,
    (12, 1, False, True): 1,
    
    # 7-7
    (14, 2, False, True): 3,
    (14, 3, False, True): 3,
    (14, 4, False, True): 3,
    (14, 5, False, True): 3,
    (14, 6, False, True): 3,
    (14, 7, False, True): 3,
    (14, 8, False, True): 1,
    (14, 9, False, True): 1,
    (14, 10, False, True): 1,
    (14, 1, False, True): 1,
    
    # 8-8
    (16, 2, False, True): 3,
    (16, 3, False, True): 3,
    (16, 4, False, True): 3,
    (16, 5, False, True): 3,
    (16, 6, False, True): 3,
    (16, 7, False, True): 3,
    (16, 8, False, True): 3,
    (16, 9, False, True): 3,
    (16, 10, False, True): 3,
    (16, 1, False, True): 3,
    
    # 9-9
    (18, 2, False, True): 3,
    (18, 3, False, True): 3,
    (18, 4, False, True): 3,
    (18, 5, False, True): 3,
    (18, 6, False, True): 3,
    (18, 7, False, True): 0,
    (18, 8, False, True): 3,
    (18, 9, False, True): 3,
    (18, 10, False, True): 0,
    (18, 1, False, True): 0,
    
    # 10-10
    (20, 2, False, True): 0,
    (20, 3, False, True): 0,
    (20, 4, False, True): 0,
    (20, 5, False, True): 0,
    (20, 6, False, True): 0,
    (20, 7, False, True): 0,
    (20, 8, False, True): 0,
    (20, 9, False, True): 0,
    (20, 10, False, True): 0,
    (20, 1, False, True): 0,
    
    # A-A
    (12, 2, True, True): 3,
    (12, 3, True, True): 3,
    (12, 4, True, True): 3,
    (12, 5, True, True): 3,
    (12, 6, True, True): 3,
    (12, 7, True, True): 3,
    (12, 8, True, True): 3,
    (12, 9, True, True): 3,
    (12, 10, True, True): 3,
    (12, 1, True, True): 3
}