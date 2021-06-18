# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 10:38:05 2020

@author: lukek
"""

import random
import pandas as pd 
import numpy as np
import time

class Card:
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
        
    def returncard(self): #returns card as string
        return str(self.value) + str(self.suit)
        
    
    def printcard(self): #prints card to screen
        print("{} of {}".format(self.value,self.suit))
            


class Deck:
    def __init__(self): #builds deck and shuffles
        self.cards=[]
        self.build()
        self.shuffle()
        
    def build(self): #build deck
        for a in ["Spades","Clubs","Diamonds","Hearts"]:
            for b in range(2,15):
                self.cards.append(Card(b,a))
        
    def returndeck(self): #prints all cards in deck as list
        decklist=[]
        for i in self.cards:
            decklist.append([str(i.value),str(i.suit)])
        return decklist
    
    def printdeck(self):
        for i in self.cards:
            i.printcard()
    
    def shuffle(self): #shuffles deck
        for i in range(len(self.cards)-1,0,-1):
            rd = random.randint(0,i)
            self.cards[i],self.cards[rd] = self.cards[rd], self.cards[i]
            
    def draw(self): #takes one card off the top of deck
        return self.cards.pop()
    
    def hand(self,card1,card2):
        self.cards.remove(card1,card2)
    
    
    
    
    
    
    
    