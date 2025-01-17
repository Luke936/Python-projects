# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:27:36 2020

@author: lukek
"""
#property of Luke Schabach

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
    
    
class player:
    def __init__(self,name): 
        self.name=name
        self.hand=[]
        
    def draw(self,deck): #adds one card object from deck and puts it in hand list
        self.hand.append(deck.draw())
    
    def createplayerlists(self): #turns list of card objects into list of lists
        playerlist=[]
        for card in self.hand:
            cval= str(card.value)
            csuit=str(card.suit)
            playerlist.append([cval,csuit])
        return playerlist


    
class poker:
    def __init__(self): #creates 5 card river 
        self.results=[]


    def run(self,deck): #Adds 5 card objects to a list
        deck.draw()
        for i in range(0,3):
            self.results.append(deck.draw())
        deck.draw()
        self.results.append(deck.draw())
        deck.draw()
        self.results.append(deck.draw())
    
    def returnriver(self,deck): #Makes a list of 5 lists for each card and returns it
        self.run(deck)
        riverlist=[]
        for card in self.results:
            riverlist.append([str(card.value),str(card.suit)])
        return riverlist
    
    def returnhands(self,players,deck): #creates list of player hand dictionarys and returns it
        listoflists=[]
        for player in players: #each seperate player draws a card one at a time 
            player.draw(deck)
        for player in players:
            player.draw(deck)
        for player in players:
            #print(i.name)
            playerlists=player.createplayerlists()
            listoflists.append(playerlists) #list of lists for each player
        return listoflists
    
    def return7card(self,players,river): #return two lists, one with all 7 card values and one with suits
        
        cardvalue7=[]
        cardsuit7=[]
        for n in range(0,len(players)):
            cardvalue7.append([players[n][0][0],players[n][1][0]]+[item[0] for item in river] )
            
            cardsuit7.append([players[n][0][1],players[n][1][1]]+[item[1] for item in river] )
        return (cardvalue7,cardsuit7)




#The following code is used to find out what hand has been drawn for each player.

def isroyalflush(frame):
    if not sum(frame['Suit'].value_counts()>=5) >=1: return('No') #check for 5 suits
    if not '14' in list(frame['Value']): return('No') #check if first card is an ace
    count=frame.Suit.value_counts() #get frequency of each suit
    suit=list(count.nlargest(1).index)[0] #return suit that makes the flush (the one with largest frequency)
                     
    valuelist=list(frame[frame['Suit']==suit]['Value'] ) #make list of values for the correct suit
    valuelist=[int(valuelist[i]) for i in range(0,len(valuelist))] #turn strings to integers
    valuelist=list(set(valuelist))
    L=len(valuelist)
    if L<5: return('No')
    
    valuelist.sort(reverse=True) #sort in decending
    if sum([valuelist[i]-valuelist[i+1] == 1 for i in range(0,4)])>=4: return ('Yes') #check for straight in first 5 cards starting with ace
    else: return('No')
        
        
y=[1,2,3,4]
sorted(y,reverse = True)

def isstraightflush(frame):
    if not sum(frame['Suit'].value_counts()>=5) >=1: return('No')
    count=frame.Suit.value_counts() #get frequency of each suit
    suit=list(count.nlargest(1).index)[0] #return suit that makes the flush (the one with largest frequency)     
    
    valuelist=list(frame[frame['Suit']==suit]['Value'] )
    valuelist=[int(valuelist[i]) for i in range(0,len(valuelist))] #make list of integer values
    
    if 14 in valuelist:
        valuelist[valuelist.index(14)]=1 #change ace to 1 because high ace would be royal flush
    valuelist=list(set(valuelist))
    L=len(valuelist)
    if L<5: return('No')
    
    if (sum(np.diff(sorted(valuelist)[0:5]) == 1) >= 4):
        return('Yes')
    elif (sum(np.diff(sorted(valuelist)[1:min(L,6)]) == 1) >= 4):
        return('Yes')
    elif (sum(np.diff(sorted(valuelist)[2:min(L,7)]) == 1) >= 4):
        return('Yes')
    elif (sum(np.diff(sorted(valuelist)[3:min(L,8)]) == 1) >= 4):
        return('Yes')
    
    else:
        return('No')



def isquads(frame):
    if sum(frame['Value'].value_counts()==4) >=1:
        return('Yes')
    else:
        return('No')



def isfullhouse(frame):
    if not sum(frame['Value'].value_counts()==3) >=1: return('No') #End function if trips are not found
    if (sum(frame['Value'].value_counts()==2) >=1) and ( sum(frame['Value'].value_counts()==3) >= 1 ) : return('Yes')
    #return yes if there is one pair and one trips
    elif sum(frame['Value'].value_counts()==3) >1: return('Yes')
    #return yes if there is two sets of trips 
    else:
        return('No')
    





def isflush(frame):
    if sum(frame['Suit'].value_counts()>=5) >=1:
        return('Yes')
    else:
        return('No')





def isstraight(frame):
    
    #sortedframe=frame.sort_values(by="Value",ascending = False )
    valuelist=list(frame['Value'])
    valuelist=[int(valuelist[i]) for i in range(0,len(valuelist))]
    #valuelist.sort(reverse=True)
    if 14 in valuelist:
        valuelist.append(1)
    valuelist=list(set(valuelist))
    L=len(valuelist)
    if L<5: return('No')
    #use numpys.diff function to find difference between each value    
    if (sum(np.diff(sorted(valuelist)[0:5]) == 1) >= 4):
        return('Yes')
    elif (sum(np.diff(sorted(valuelist)[1:min(L,6)]) == 1) >= 4):
        return('Yes')
    elif (sum(np.diff(sorted(valuelist)[2:min(L,7)]) == 1) >= 4):
        return('Yes')
    elif (sum(np.diff(sorted(valuelist)[3:min(L,8)]) == 1) >= 4):
        return('Yes')
    
    else:
        return('No')
        



      
def istrips(frame):
    if sum(frame['Value'].value_counts()==3) >=1:
        return('Yes')
    else:
        return('No')
        
        
      
      

def istwopair(frame):
    if sum(frame['Value'].value_counts()==2) >=2:
        return('Yes')
        
    else:
        return('No')
        
    
def ispair(frame):
    if sum(frame['Value'].value_counts()==2) >=1:
        
        return('Yes')
        
    else:
        return('No')



def isnopair(frame):
    if not sum(frame['Value'].value_counts()==2) > 0:
        return('Yes')
    else:
        print('ERROR')
        print(frame['Value'])
        return('No')
    

def runall(): #returns p1 which is a dataframe of player ones hand...has the ability to be ran for many players
    a=player('Luke')
    #b=player('Bob')
    #c=player('Evan')
    #d=player('Joe')
    playerlist=[a]
    deck=Deck()
    pokersim=poker() #create deck
    phands = pokersim.returnhands(playerlist,deck) #return list of player hands as lists #creates river list of card objects
    river=pokersim.returnriver(deck) #returns list of river cards as lists
    unpack=pokersim.return7card(phands,river)
    value7=unpack[0]
    suit7=unpack[1]
    dflist=[]
    for i in range(0,len(phands)):
        dflist.append(pd.DataFrame({'Value': value7[i],'Suit': suit7[i]}))
    p1=dflist[0]
    #p2=dflist[1]
    #p3=dflist[2]
    #p4=dflist[3]
    return (p1)

ranks=['Royal Flush','Straight Flush','Four of a Kind','Full House','Flush','Straight','Three of a kind','Two pair','Pair','No Pair']


def checkall(player): #checks player dataframe for each hand and populates dictionary with 0 is no 1 if yes
    hdict={}
 
    for i in range(0,len(ranks)):
       hdict.update({ranks[i]:0})
       
    h9=isroyalflush(player)
    if h9=='Yes':
        hdict.update({ranks[0]:1})
        return hdict
    h8=isstraightflush(player)
    if h8=='Yes':
        hdict.update({ranks[1]:1})
        return hdict
    h7=isquads(player)
    if h7=='Yes':
        hdict.update({ranks[2]:1})
        return hdict
    h6=isfullhouse(player)
    if h6=='Yes':
        hdict.update({ranks[3]:1})
        return hdict
    h5=isflush(player)
    if h5=='Yes':
        hdict.update({ranks[4]:1})
        return hdict
    
    
    h6=isstraight(player)
    if h6=='Yes':
        hdict.update({ranks[5]:1})
        return hdict
        
    h3=istrips(player)
    if h3=='Yes':
        hdict.update({ranks[6]:1})
        return hdict
    
    h2=istwopair(player)
    if h2=='Yes':
        hdict.update({ranks[7]:1})
        return hdict
    h1=ispair(player)
    if h1=='Yes':
        hdict.update({ranks[8]:1})
        return hdict
    h0=isnopair(player)
    if h0=='Yes':
        hdict.update({ranks[9]:1})
        return hdict
    
    return hdict






def bigresults(runtime): #does everything needed to get results 
    
    masterdict={}  #creates blank dictionary with zero for each hand
    for i in range(0,len(ranks)):
        masterdict.update({ranks[i]:0})
    start_time = time.time()
    
    #creates deck and playerhands "runtime" number of times and each time adds hand to masterdictionary
    for i in range(0,runtime):
        p1=runall()
        handdict=checkall(p1)
        
        #each player hand dictionary is added to the master dictionary to get total # of hands for each 
        for rank in ranks:
            masterdict[rank]+=handdict[rank]
            
            
    print ("My program took", round(time.time() - start_time,2), "seconds to run")
    numdict={} #turns master dictionary into percents for easy analysis 
    for i in ranks:
        numdict.update({i:str(round((masterdict[i]/runtime)*100,4))+'%'})
    return(masterdict,numdict)




#---HIGHLIGHT AND RUN EVERYTHING ABOVE THIS LINE TO SET UP SIMULATION--#

#---------USE FUNCTION BELOW TO RUN SIMULATION AND STORE RESULTS AS "quantities" and "Percents"
    
Quantities,Percents=bigresults(10000) #takes about 10 seconds for 1000 runs

#---------RUN THESE SEPERATELY TO VIEW OUTPUT OF SIMULATION--------------------------
Quantities
Percents
#-------------------------------------------------------------------------



#todo fix straight check on royal and straight flush

