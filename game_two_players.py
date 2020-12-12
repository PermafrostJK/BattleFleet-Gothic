class Ship:
    def __init__(self, length, direction, lable):  # lable added to differenctiate between players 1 and 2
        if direction != 'V' and direction != 'H':
            raise Exception
        self.length = length
        self.direction = direction
        self.actual_location = []
        self.lable = lable

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
        self.battlefield = [['o ' for i in range(length + 1)] for j in range(width+ 1)]
        for i in range(length + 1):
            self.battlefield[0][i] = str(i)+" "
        for j in range(width + 1):
            self.battlefield[j][0] = str(j)+" "
        self.width = width
        self.length = length
        self.strbattlefield = ''

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
def set_for_1():
    #for player 1#
    roster = ['Battleship', 'Cruizer', 'Destroyer', 'Corvette']
    b1 = Battlefield()
    print("*************Welcome, Player 1! The game has started! Enjoy and try to win!*************\n")
    print("The original battlefield looks like this")
    print(b1)
    print('You need to place your ships on a 8x8 battlefield!')
    print("You have the following 4 ships:\n"
          "'Battleship' with length of 5\n"
          "'Cruizer' with length of 4\n"
          "'Destroyer' with length of 3\n"
          "'Corvette' with length of 2\n\n"
          "You need to put the ORIENTATION and LOCATION of your boat following the sequence above\n"
          "         For orientation, you need to enter 'V' for vertical and 'H' for horizontal\n"
          "         For location, you need to enter x and y coordinate for the fore of your current boat\n"
          "*Please make sure all of your vessles are placed entirely within your half of the battlefield*\n")
    l_length=[]
    l_width=[]
    for i in range(1, b1.length+1):
        l_length.append(i)
    for i in range(1, b1.width+1):
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
        while x not in l_length or (direction == "H" and x + length-1 > b1.length) \
                or y not in l_width or (direction=="V" and y+length-1> b1.width):
            print('Please enter a valid orientation and x/y coordinate to make sure it is not out of scope')
            direction = input('Please enter the orientation of your ' + roster[i])
            try:
                x = int(input("Please set up the x coordinate of your " + roster[i]))
                y = int(input("Please set up the y coordinate of your " + roster[i]))
            except ValueError:
                continue
        while b1.battlefield[y][x] == "@ ":
            print("Please enter a valid orientation and x/y coordinate to make sure it is not the same as one of the previous boats")
            try:
                    direction = input('Please enter the orientation of your ' + roster[i])
                    x = int(input("Please set up the x coordinate of your " + roster[i]))
                    y = int(input("Please set up the y coordinate of your " + roster[i]))
            except ValueError:
                    continue
        a_ship = Ship(length, direction, 1)
        a_ship.set_ship(x, y)
        b1.init_my_battlefield(a_ship)
        print(b1)
        length -= 1
    return b1
def set_for_2():
    # for player 2
    roster = ['Battleship', 'Cruizer', 'Destroyer', 'Corvette']
    b2 = Battlefield()
    print("*************Welcome, Player 2! The game has started! Enjoy and try to win!*************\n")
    print("The original battlefield looks like this")
    print(b2)
    print('You need to place your ships on a 8x8 battlefield!')
    print("You have the following 4 ships:\n"
          "'Battleship' with length of 5\n"
          "'Cruizer' with length of 4\n"
          "'Destroyer' with length of 3\n"
          "'Corvette' with length of 2\n\n"
          "You need to put the ORIENTATION and LOCATION of your boat following the sequence above\n"
          "         For orientation, you need to enter 'V' for vertical and 'H' for horizontal\n"
          "         For location, you need to enter x and y coordinate for the fore of your current boat\n"
          "*Please make sure all of your vessles are placed entirely within your half of the battlefield*\n")
    l_length=[]
    l_width=[]
    for i in range(1, b2.length+1):
        l_length.append(i)
    for i in range(1, b2.width+1):
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
        while x not in l_length or (direction == "H" and x + length-1 > b1.length) \
                or y not in l_width or (direction=="V" and y+length-1> b1.width):
            print('Please enter a valid orientation and x/y coordinate to make sure it is not out of scope')
            direction = input('Please enter the orientation of your ' + roster[i])
            try:
                x = int(input("Please set up the x coordinate of your " + roster[i]))
                y = int(input("Please set up the y coordinate of your " + roster[i]))
            except ValueError:
                continue
        while b1.battlefield[y][x] == "@ ":
            print("Please enter a valid orientation and x/y coordinate to make sure it is not the same as one of the previous boats")
            try:
                    direction = input('Please enter the orientation of your ' + roster[i])
                    x = int(input("Please set up the x coordinate of your " + roster[i]))
                    y = int(input("Please set up the y coordinate of your " + roster[i]))
            except ValueError:
                    continue
        a_ship = Ship(length, direction, 2)
        a_ship.set_ship(x, y)
        b1.init_my_battlefield(a_ship)
        print(b2)
        length -= 1
    return b2
#==================================================================================================================================#
def attack(b1,b2): # for either player 1 or player 1#
    l_length=[]
    l_width=[]
    for i in range(1, b2.length+1):
        l_length.append(i)
    for i in range(1, b2.width+1):
        l_width.append(i)
#==================================================================================================================================#
    for i in len(player.roster):#implement loop that allows player to fire a certain number of shots equal to his remaining ship number   
        pass
#==================================================================================================================================#
    try:
        x = int(input("Player 1, guess one x coordinate of your opponent's ship "))
        y = int(input("Player 1, guess one y coordinate of your opponent's ship "))
        while x not in l_length or y not in l_width:
            print('Please enter a valid x/y coordinate to make sure it is in the enemy field')
            x = int(input("Player 1, guess one x coordinate of your opponent's ship "))
            y = int(input("Player 1, guess one y coordinate of your opponent's ship "))
        while 
    except ValueError:
        print("Please enter a valid integer for x/y")
        x = int(input("Player 1, guess one x coordinate (ranging from 5 to 8)of your opponent's ship "))
        y = int(input("Player 1, guess one y coordinate (ranging from 1 to 8)of your opponent's ship "))
    b1.update_battlefield(x,y,b2)
    
#==================================================================================================================================#
def main():
    b1 = set_for_1()
    b2 = set_for_2()
    for i in range(10):
        attack(b1, b2)
        attack(b2, b1)
    p1=b1.points_for_1()
    p2=b2.points_for_2()
    if p1>p2:
        print("Player 1 wins!")
    elif p1<p2:
        print("Player 2 wins!")
    else:
        print("You two got the same score! Slug it out next time!")
main()
