from random import shuffle
import random
import sys


class Deck:
    """
    This is the Deck Class. This object creates a deck of cards to initiate
    play. Then the list of cards is split in half. It will use SUITE and RANKS to create the deck.

    """
    def __init__(self,player_a=[],player_b=[]):
         self.player_a=player_a
         self.player_b=player_b
         SUITE = ['H','D','S','C']
         RANKS= [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
         card_name=[]
         for i in range(len(SUITE)):
             for j in range(len(RANKS)):
                 card_name.append(str(SUITE[i])+" "+str(RANKS[j]))

         random.shuffle(card_name)
         self.card_name=card_name

    def assign(self):
         for q in range(len(self.card_name)):
            if q%2==0:
                self.player_a.append(self.card_name[q])
            else:
                self.player_b.append(self.card_name[q])
         return self.player_a,self.player_b




class Hand():
    '''
    This is the Hand class. All functions regarding the play of the game are stored in this class
    '''
    def __init__(self,player_a,player_b,pile=[],card_player_a=[],card_player_b=[]):
        self.pile=pile
        self.card_player_a=card_player_a
        self.card_player_b=card_player_b
        self.player_a=player_a
        self.player_b=player_b

    def warwinner(self):
        if len(self.player_a)==0:
           print("You won the game")
           sys.exit()
        elif len(self.player_b)==0:
           prnt("The computer won the game, better luck next time")
           sys.exit()


    def add(self):
        self.card_player_a=random.choice(self.player_a)
        self.pile.append(self.card_player_a)
        print("your card is {}".format(self.card_player_a))
        self.card_player_b=random.choice(self.player_b)
        self.pile.append(self.card_player_b)
        print("the computer's card is {}".format(self.card_player_b))

    def addwar(self):
        for _ in range(3):
           self.card_player_a=random.choice(self.player_a)
           self.pile.append(self.card_player_a)
           self.card_player_b=random.choice(self.player_b)
           self.pile.append(self.card_player_b)


    def battlewinner(self):

        def split_return(name_card):
            num_assigned=None
            variable=name_card.split()

            if variable[1]=='A':
                num_assigned=14
            elif variable[1]=='K':
                num_assigned=13
            elif variable[1]=='Q':
                num_assigned=12
            elif variable[1]=='J':
                num_assigned=11
            else:
                num_assigned=variable[1]

            return num_assigned

        self.add()

        num_value_a=(int(split_return(self.card_player_a)))
        num_value_b=(int(split_return(self.card_player_b)))

        if num_value_a<num_value_b:
           for i in range(len(self.pile)):
                for j in range(len(self.player_b)):
                    if self.player_b[j] != self.pile[i]:
                        self.player_b.append(self.pile[i])
           self.player_b=list(dict.fromkeys(self.player_b))


           for q in self.pile:
                for t in self.player_a:
                    if q==t:
                        self.player_a.remove(q)
           self.player_a=list(dict.fromkeys(self.player_a))


           print("computer is the winner of this battle")
           self.pile.clear()
           self.warwinner()
           print("do you wish to continue the game?(yes/no)")
           contgame=input()
           if contgame=="yes":
                begin_hand=Hand(self.player_a,self.player_b)
                begin_hand.battlewinner()
           else:
                sys.exit()

        elif num_value_a>num_value_b:
           for i in range(len(self.pile)):
                for j in range(len(self.player_a)):
                    if self.player_a[j] != self.pile[i]:
                        self.player_a.append(self.pile[i])
           self.player_a=list(dict.fromkeys(self.player_a))

           for q in self.pile:
                 for t in self.player_b:
                     if q==t:
                         self.player_b.remove(q)
           self.player_b=list(dict.fromkeys(self.player_b))


           print("a is the winner of this battle")
           self.pile.clear()
           self.warwinner()
           print("do you wish to continue the game?(yes/no)")
           contgame=input()
           if contgame=="yes":
                begin_hand=Hand(self.player_a,self.player_b)
                begin_hand.battlewinner()
           else:
                sys.exit()


        elif num_value_a==num_value_b:
           print("THIS IS WAR")
           self.addwar()
           self.battlewinner()




class Player():
    """
    This is the Player class. All functions for adding the player and starting the game are stored in here
    """


    def Begin(self):

        a=[]
        b=[]

        print("what is the name of player A")
        name_a=input()

        print("hello {}".format(name_a))

        print("Do you want to distribute the cards?(yes/no)")
        reply=input()
        if reply=="yes":
            cards= Deck()
            a,b=cards.assign()
            print("cards have been assigned")
        else:
            sys.exit()

        print("do you wish to continue the game?(yes,no)")
        startgame=input()
        if reply=="yes":
            begin_hand=Hand(a,b)
            begin_hand.battlewinner()
        else:
            sys.exit()



initiate=Player()
initiate.Begin()
