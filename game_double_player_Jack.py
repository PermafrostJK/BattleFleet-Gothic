#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:06:05 2020

@author: jackfrostljx
"""
import os

class Ship:
    def __init__(self, length, direction, label):  # label added to differenctiate between players 1 and 2
        if direction != 'V' and direction != 'H':
            raise Exception
        self.length = length
        self.direction = direction
        self.actual_location = []
        self.label = label

    def set_ship(self, locationX, locationY):
        if self.direction == 'V': #verticle
            for i in range(self.length):
                the_boat = [locationX, locationY + i]
                self.actual_location.append(the_boat)
        elif self.direction == 'H':  # horizontal
            for i in range(self.length):
                the_boat = [locationX + i, locationY]
                self.actual_location.append(the_boat)
#==================================================================================================================================#
class Battlefield:
    def __init__(self, width=8, length=8):
        self.battlefield = [['o ' for i in range(length + 1)] for j in range(width + 1)]
        for i in range(length + 1):
            self.battlefield[0][i] = str(i)+" "
        for j in range(width + 1):
            self.battlefield[j][0] = str(j)+" "
        self.width = width
        self.length = length
        self.strbattlefield = '' #Unused attribute

    def init_my_battlefield(self,ship):
        for actual_boat in ship.actual_location:
            self.battlefield[actual_boat[1]][actual_boat[0]] = '@ '
    
    def check_coordinate(self,Xcoordinate,Ycoordinate):
        check=0
        if self.battlefield[Ycoordinate][Xcoordinate]=='x ' or self.battlefield[Ycoordinate][Xcoordinate]=='  ':
            check+=0
        elif self.battlefield[Ycoordinate][Xcoordinate]=='o ':
            check+=1
        else:
            check+=2
        return check
    
    def update_battlefield(self, Xcoordinate, Ycoordinate,battlefield):
        if battlefield.check_coordinate(Xcoordinate,Ycoordinate)==0:
            print("\nThis point has already been hit, try another one next time!")
            repeat = 1
            return repeat
        elif battlefield.check_coordinate(Xcoordinate,Ycoordinate)==1:
            self.battlefield[Ycoordinate][Xcoordinate] = '  '
            print("\nSorry, you didn't hit an enemy ship!")
        else:
            self.battlefield[Ycoordinate][Xcoordinate] = 'x '
            print("\nGood job, you hit an enemy ship!")           
        print("Now, the battlefield looks like this")
        print(self)
        

    def __str__(self): #Unused method
        str=""
        for i in range(self.width+1):
            for j in range(self.length+1):
                str+=self.battlefield[i][j]
            str+="\n"
        return str
    
    def points_calculator(self):
        count = 0
        for i in range(1,self.length+1):
            for j in range(1,self.width+1):
                if self.battlefield[j][i] == 'x ':
                    count += 1
        return count
#==================================================================================================================================#
def set_battlefield():
    #for player 1#
    roster = ['Battleship', 'Cruiser', 'Destroyer', 'Corvette']
    b = Battlefield()
    
    print("The original battlefield looks like this")
    print(b)
    print('You need to place your ships on a 8x8 battlefield!')
    print("You have the following 4 ships:\n"
          "'Battleship' with length of 5\n"
          "'Cruiser' with length of 4\n"
          "'Destroyer' with length of 3\n"
          "'Corvette' with length of 2\n\n"
          "You need to put the ORIENTATION and LOCATION of your boat following the sequence above\n"
          "         For orientation, you need to enter 'V' for vertical and 'H' for horizontal\n"
          "         For location, you need to enter x and y coordinate for the first block of your current boat\n"
          "*Please make sure all of your vessels are placed entirely within your half of the battlefield*\n")
    l_length=[]
    l_width=[]
    
    d_roster={'Battleship':[5],'Cruiser':[4],'Destroyer':[3],'Corvette':[2]}
    l_ships=[]
    
    for i in range(1, b.length+1):
        l_length.append(i)
    for i in range(1, b.width+1):
        l_width.append(i)
    
    length = 5
    for i in range(4):
        direction = input('Please enter the orientation of your ' + roster[i])
        while direction != 'V' and direction != 'H':
            print('Please enter a valid orientation for your ship')
            direction = input('Please enter the orientation of your ' + roster[i])
        try:
            x = int(input("Please set up the x coordinate of your " + roster[i])) #如果输入的不是整数，也会报错，那这个漏洞还要改吗？
            y = int(input("Please set up the y coordinate of your " + roster[i]))
        except ValueError:
            continue
        while x not in l_length or (direction == "H" and x + length-1 > b.length) \
                or y not in l_width or (direction=="V" and y+length-1> b.width):
            print('Please enter a valid orientation and x/y coordinate to make sure it is not out of scope')
            direction = input('Please enter the orientation of your ' + roster[i])
            try:
                x = int(input("Please set up the x coordinate of your " + roster[i]))
                y = int(input("Please set up the y coordinate of your " + roster[i]))
            except ValueError:
                continue
        while b.battlefield[y][x] == "@ ":
            print("Please enter a valid orientation and x/y coordinate to make sure it is not the same as one of the previous boats")
            try:
                    direction = input('Please enter the orientation of your ' + roster[i])
                    x = int(input("Please set up the x coordinate of your " + roster[i]))
                    y = int(input("Please set up the y coordinate of your " + roster[i]))
            except ValueError:
                    continue
        a_ship = Ship(length, direction, 1)
        l_ships.append(a_ship)
        a_ship.set_ship(x, y)
        for j in a_ship.actual_location:
            d_roster[roster[i]].append(j)
        b.init_my_battlefield(a_ship)
        os.system('clear') #clears previous output so that the player sees what appears to be a rapid update of the 
                           #battlefield without repitition 
        print(b)
        length -= 1
    return b, d_roster, l_ships # d_roster is used to check whether a ship is sunk

#==================================================================================================================================#
def attack(b1,b2): # for either player 1 or player 1#
    l_length=[]
    l_width=[]
    for i in range(1, b2.length+1):
        l_length.append(i)
    for i in range(1, b2.width+1):
        l_width.append(i)
    try:
        x = int(input("Guess one x coordinate of your opponent's ship "))
        y = int(input("Guess one y coordinate of your opponent's ship "))
        while x not in l_length or y not in l_width:
            print('Please enter a valid x/y coordinate to make sure it is in the enemy field')
            x = int(input("Guess one x coordinate of your opponent's ship "))
            y = int(input("Guess one y coordinate of your opponent's ship "))

    except ValueError:
        print("Please enter a valid integer for x/y")
        x = int(input("Guess one x coordinate of your opponent's ship "))
        y = int(input("Guess one y coordinate of your opponent's ship "))
    b1.update_battlefield(x,y,b2)
    
#==================================================================================================================================#
def main():
    print("*************Welcome, Player 1! The game has started! Enjoy and try to win!*************\n")
    b1, d_player1_roster, player1_ships = set_battlefield()
    if input('Are you finished placing your ships?\n')=='done':
        print("*************Welcome, Player 2! The game has started! Enjoy and try to win!*************\n")
        b2, d_player2_roster, player2_ships = set_battlefield()
    else: #loop back to a function that allows player to change on of the ship's location
        pass
    player1_attacks, player2_attacks=4,4
#==================================================================================================================================#
    for i in range(3):
        for k, v in d_player1_roster.items():
            HP=v[0]
            for j in v:
                if type(j)==list:
                    if b1.battlefield[j[1]][j[0]]=='x ':
                        HP-=1
            if HP==0:
                player1_attacks-=1
        
        for k, v in d_player2_roster.items():
            HP=v[0]
            for j in v:
                if type(j)==list:
                    if b2.battlefield[j[1]][j[0]]=='x ':
                        HP-=1
            if HP==0:
                player2_attacks-=1
#==================================================================================================================================#                
        print("Player1's turn:\n")
        for i in range(player1_attacks):
            print('shot number %s' %(i+1))
            attack(b1, b2)
        print("Player2's turn:\n")        
        for i in range(player2_attacks):
            print('shot number %s' %(i+1))
            attack(b2, b1)
        # if ships of one player is all sunk:
            # print victory message for the other player
            # break
    p1=b1.points_calculator()
    p2=b2.points_calculator()
    if p1>p2:
        print("Player 1 wins!")
    elif p1<p2:
        print("Player 2 wins!")
    else:
        print("You two got the same score! Slug it out next time!")
main()
