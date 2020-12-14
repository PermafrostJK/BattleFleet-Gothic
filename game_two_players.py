import os

class Ship:
    def __init__(self, length, direction):  
        self.length = length
        self.direction = direction
        self.actual_location = []
        

    def set_ship(self, locationX, locationY):
        if self.direction == 'V': #vertical
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
            attack(self, battlefield)
            return
        elif self.check_coordinate(Xcoordinate,Ycoordinate)==1:
            battlefield.battlefield[Ycoordinate][Xcoordinate] = '  '
            self.battlefield[Ycoordinate][Xcoordinate] = '  '
            print("\nSorry, you didn't hit an enemy ship!")
        elif self.check_coordinate(Xcoordinate, Ycoordinate)==2:
            battlefield.battlefield[Ycoordinate][Xcoordinate] = 'x '
            self.battlefield[Ycoordinate][Xcoordinate] = 'x '
            print("\nGood job, you hit an enemy ship!") 
        
        print("Enemy battlefield:")
        print(battlefield)
         #used to grant a player a second chance if player chooses to fire on a tile that has already been hit
    
    def __str__(self): 
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
          "You need to input the ORIENTATION and LOCATION of your boat following the sequence above\n"
          "         For orientation, you need to enter 'V' for vertical and 'H' for horizontal\n"
          "         For location, you need to enter x and y coordinate for the first block of your current boat\n"
          "             *Please make sure all of your vessels are placed entirely within the battlefield*\n"
          "         The objective of the game is to hit as many of the opponent's ships as possible before the alloted turns run out\n"
          "         Each player can shoot n times per turn, where n = the number of ships in the player's roster\n"
          "         This number decreases by one every time the player has one of his/her ships destroyed by the opponent"
          )
    l_length=[]
    l_width=[]
    
    d_roster={'Battleship':[5],'Cruiser':[4],'Destroyer':[3],'Corvette':[2]}
    
    for i in range(1, b.length+1):
        l_length.append(i)
    for i in range(1, b.width+1):
        l_width.append(i)
    
    length = 5
    for i in range(4):
        direction = input('Please enter the orientation of your ' + roster[i]+'\n')
        while direction != 'V' and direction != 'H':
            print('Please enter a valid orientation for your ship')
            direction = input('Please enter the orientation of your ' + roster[i]+'\n')
        try:
            x = int(input("Please set up the x coordinate of your " + roster[i]+'\n')) 
            y = int(input("Please set up the y coordinate of your " + roster[i]+'\n'))
        except ValueError:
            continue
        while x not in l_length or (direction == "H" and x + length-1 > b.length) \
                or y not in l_width or (direction=="V" and y+length-1> b.width):
            print('Please enter a valid orientation and x/y coordinate to make sure it is not out of scope')
            direction = input('Please enter the orientation of your ' + roster[i])
            try:
                x = int(input("Please set up the x coordinate of your " + roster[i]+'\n'))
                y = int(input("Please set up the y coordinate of your " + roster[i]+'\n'))
            except ValueError:
                continue
        while b.battlefield[y][x] == "@ ":
            print("Please enter a valid orientation and x/y coordinate to make sure it is not the same as one of the previous boats")
            try:
                    direction = input('Please enter the orientation of your ' + roster[i]+'\n')
                    x = int(input("Please set up the x coordinate of your " + roster[i]+'\n'))
                    y = int(input("Please set up the y coordinate of your " + roster[i]+'\n'))
            except ValueError:
                    continue
        a_ship = Ship(length, direction)
        a_ship.set_ship(x, y)
        for j in a_ship.actual_location:
            d_roster[roster[i]].append(j)
        b.init_my_battlefield(a_ship)
        os.system('clear') #clears previous output so that the player sees what appears to be a rapid update of the 
                           #battlefield without repetition
        print(b)
        length -= 1
    return b, d_roster # d_roster is used to check whether a ship is sunk

#==================================================================================================================================#
def attack(actual_battlefield,displayed_battlefield): 
    l_length=[]
    l_width=[]
    for i in range(1, actual_battlefield.length+1):
        l_length.append(i)
    for i in range(1, actual_battlefield.width+1):
        l_width.append(i)
    
    x = int(input("Guess one x coordinate of your opponent's ship "))
    y = int(input("Guess one y coordinate of your opponent's ship "))
    while x not in l_length or y not in l_width:
        print('Please enter a valid x/y coordinate to make sure it is in the enemy field')
        x = int(input("Guess one x coordinate of your opponent's ship "))
        y = int(input("Guess one y coordinate of your opponent's ship "))
 
    actual_battlefield.update_battlefield(x,y,displayed_battlefield)
    
#==================================================================================================================================#
def main():
    print("*************Welcome, Player 1! The game has started! Enjoy and try to win!*************\n")
    b1, d_player1_roster = set_battlefield()
    a=input('Press enter to continue.\n')
    os.system('clear')
    print("*************Welcome, Player 2! The game has started! Enjoy and try to win!*************\n")
    b2, d_player2_roster= set_battlefield()
    a=input('Press enter to continue.\n')
    b1_for_player2 = Battlefield()
    b2_for_player1 = Battlefield()
    
    l_player1_destroyed=[]
    l_player2_destroyed=[]
#==================================================================================================================================#
    for i in range(5):                    
        shots_player1=4-len(l_player1_destroyed)
        shots_player2=4-len(l_player2_destroyed)
        
        os.system('clear')
        print("Player1's turn:\n")
        print('Enemy battlefield:')
        print(b2_for_player1)#displays the current state of the opponent's battlefield for player to consult while planning attacks
        print('Your battlefield:')
        print(b1)
        
        print('Casualties:',l_player1_destroyed)
        print('Kills:',l_player2_destroyed)
        print('Number of shots: %s'%shots_player1)
        
        for i in range(shots_player1):
            print('shot number %s' %(i+1))
            
            attack(b2,b2_for_player1)
            for k, v in d_player2_roster.items():
                HP=v[0]
                for j in v:
                    if type(j)==list:
                        if b2.battlefield[j[1]][j[0]]=='x ':
                            HP-=1
                if HP==0:
                    
                    l_player2_destroyed.append(k)
                                        
            for i in l_player2_destroyed:
                d_player2_roster.pop(i,None)
            
            if len(l_player2_destroyed)==4:
                print ('Player 1 has won through eliminating Player 2\'s fleet.')
                return
        a=input('Press enter to finish your turn') #allows the player to have a glimpse of the battlefield after their final shot
        #======================================================#
        os.system('clear')
        print("Player2's turn:\n")
        print('Enemy battlefield:')
        print(b1_for_player2)
        print('Your battlefield:')
        print(b2)
        
        print('Casualties:',l_player2_destroyed)
        print('Kills:',l_player1_destroyed)
        print('Number of shots: %s'%shots_player2)
        
        for i in range(shots_player2):
            print('shot number %s' %(i+1))
            
            attack(b1,b1_for_player2)
            for k, v in d_player1_roster.items():
                HP=v[0]
                for j in v:
                    if type(j)==list:
                        if b1.battlefield[j[1]][j[0]]=='x ':
                            HP-=1
                    if HP==0:             
                        
                        l_player1_destroyed.append(k)
                
            for i in l_player1_destroyed:    
                d_player1_roster.pop(i,None)
            if len(l_player1_destroyed)==4:
                print ('Player 2 has won through eliminating Player 1\'s fleet.')
                return
        a=input('Press enter to finish your turn')
        
        
    p1=b2.points_calculator()
    p2=b1.points_calculator()
    if p1>p2:
        print("Player 1 wins!")
    elif p1<p2:
        print("Player 2 wins!")
    else:
        print("You two got the same score! Slug it out next time!")
main()
