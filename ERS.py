#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 01:58:08 2024

@author: evancarpenter
"""

import random

NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")
SUITNAME = ("clubs", "hearts", "spades", "diamonds")

DECK = 0
PLAYER1 = 1
PLAYER2 = 2
current_card = [0]
central_pile = []
player1_pile = []
player2_pile = []
power_cards = {'Ace': 4, 'King': 3, 'Queen': 2, 'Jack': 1}

def initCards():
    cardDB = []
    for rank in range(len(RANKNAME)):
        for suit in range(len(SUITNAME)):
            cardDB.append((RANKNAME[rank], SUITNAME[suit]))
    return cardDB

def dealCards(cardDB):
    random.shuffle(cardDB)
    
    player1_pile = cardDB[:NUMCARDS // 2]
    player2_pile = cardDB[NUMCARDS // 2:]
    return player1_pile, player2_pile

def challenger(player):
    if player == PLAYER1:
        opponent = PLAYER2
    elif player == PLAYER2:
        opponent = PLAYER1
    
    power_card = 0
    if current_card[0] == "Ace":
        power_card = 4
    elif current_card[0] == "King":
        power_card = 3
    elif current_card[0] == "Queen":
        power_card = 2
    elif current_card[0] == "Jack":
        power_card = 1
    
    chances = power_card
    while chances > 0:
        if player == PLAYER1:
            player_input = input(f"Player 1, press 'Q' to play a card (chances left: {chances}): ")
        elif player == PLAYER2:
            player_input = input(f"Player 2, press 'P' to play a card (chances left: {chances}): ")
        
        if player_input in ('Q', 'P'):
            if player_input == 'Q' and player == PLAYER1:
                player_card = player1_pile.pop(0)
            elif player_input == 'P' and player == PLAYER2:
                player_card = player2_pile.pop(0)
            
            print(f"{player} plays: {player_card}")
            central_pile.append(player_card)
            
            if player_card[0] in power_cards:
                challenger(opponent)
            else:
                chances -= 1
                if chances == 0:
                    print(f"{opponent} picks up the pile!")
                    if opponent == PLAYER1:
                        player2_pile.extend(central_pile)
                    elif opponent == PLAYER2:
                        player1_pile.extend(central_pile)
                    break

def slap(central_pile):
    if len(central_pile) >= 2 and central_pile[-1][0] == central_pile[-2][0]:
        return True
    return False

def main():
    cardDB = initCards()
    player1_pile, player2_pile = dealCards(cardDB)
    
    central_pile = []

    power_cards = {'Ace': 4, 'King': 3, 'Queen': 2, 'Jack': 1}

    current_player = PLAYER1
    while player1_pile and player2_pile:
        if current_player == PLAYER1:
            input("Player 1, press 'Q' to play a card: ")
            current_card = player1_pile.pop(0)
            print("Player 1 plays:", current_card)
            central_pile.append(current_card)
        else:
            input("Player 2, press 'P' to play a card: ")
            current_card = player2_pile.pop(0)
            print("Player 2 plays:", current_card)
            central_pile.append(current_card)
        
        if current_card[0] in power_cards:
            if current_player == PLAYER1:
                if current_card[0] == "Ace":
                    power_card = 4
                elif current_card[0] == "King":
                    power_card = 3
                elif current_card[0] == "Queen":
                    power_card = 2
                elif current_card[0] == "Jack":
                    power_card = 1
                chances = power_card
                while chances > 0:
                    player2_challenge_input = input(f"Player 2, press 'P' to play a card (chances left: {chances}): ")
                    if player2_challenge_input == "P":
                        player2_challenge_card = player2_pile.pop(0)
                        print(f"Player 2 plays: {player2_challenge_card}")
                        central_pile.append(player2_challenge_card)
                        if player2_challenge_card[0] in power_cards:
                            challenger(PLAYER2)
                        elif player2_challenge_card[0] not in power_cards:
                            chances -= 1
                            if chances == 0:
                                print("Player 1 picks up the pile!")
                                player1_pile.extend(central_pile)
                                central_pile = []
                                current_player = PLAYER1
                                break
                                
                        
            else:
                if current_card[0] == "Ace":
                    power_card = 4
                elif current_card[0] == "King":
                    power_card = 3
                elif current_card[0] == "Queen":
                    power_card = 2
                elif current_card[0] == "Jack":
                    power_card = 1
                chances = power_card
                while chances > 0:
                    player1_challenge_input = input(f"Player 1, press 'Q' to play a card (chances left: {chances}): ")
                    if player1_challenge_input == "Q":
                        player1_challenge_card = player1_pile.pop(0)
                        print(f"Player 1 plays: {player1_challenge_card}")
                        central_pile.append(player1_challenge_card)
                        if player1_challenge_card[0] in power_cards:
                           challenger(PLAYER1) 
                        elif player1_challenge_card[0] not in power_cards:
                            chances -= 1
                            if chances == 0:
                                print("Player 2 picks up the pile!")
                                player2_pile.extend(central_pile)
                                central_pile = []
                                current_player = PLAYER2
                                break
                                 
        
        current_player = PLAYER1 if current_player == PLAYER2 else PLAYER2
        
        
        if slap(central_pile):
            slap_input = input("Press 's' to slap (Player 1) or 'k' to slap (Player 2): ")
            if slap_input == "s":
                print("Player 1 slapped and picks up the pile!")
                player1_pile.extend(central_pile)
            elif slap_input == "k":
                print("Player 2 slapped and picks up the pile!")
                player2_pile.extend(central_pile)
            central_pile = []
                    

            
    
    if len(player2_pile) == 0:
        print("Congratulations Player 1!  You have claimed all of the cards and are therefore the winner!")
    elif len(player1_pile) == 0:
        print("Congratulations Player 2!  You have claimed all of the cards and are therefore the winner!")


if __name__ == "__main__":
    main()