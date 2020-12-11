import random


class Ship:
    def __init__(self, length, direction, lable):  # lable added to differenctiate between players 1 and 2
        if direction != 'V' and direction != 'H':
            raise Exception
        self.length = length
        self.direction = direction
        self.actual_location = []
        self.lable = lable

    def set_ship(self, locationX, locationY):
        if self.direction == 'V':  # verticle
            for i in range(self.length):
                the_boat = [locationX, locationY + i]
                self.actual_location.append(the_boat)
        elif self.direction == 'H':  # horizontal
            for i in range(self.length):
                the_boat = [locationX + i, locationY]
                self.actual_location.append(the_boat)


# ==================================================================================================================================#
class Battlefield:
    def __init__(self, width=8, length=8):
        self.battlefield = [['o ' for i in range(length + 1)] for j in range(width + 1)]
        for i in range(length + 1):
            self.battlefield[0][i] = str(i) + " "
        for j in range(width + 1):
            self.battlefield[j][0] = str(j) + " "
        self.width = width
        self.length = length
        self.strbattlefield = ''

    def init_my_battlefield(self, ship):
        for actual_boat in ship.actual_location:
            self.battlefield[actual_boat[1]][actual_boat[0]] = '@ '

    def check_coordinate(self, Xcoordinate, Ycoordinate):
        check = 0
        if self.battlefield[Ycoordinate][Xcoordinate] == 'x ' or self.battlefield[Ycoordinate][Xcoordinate] == '  ':
            check += 0
        elif self.battlefield[Ycoordinate][Xcoordinate] == 'o ':
            check += 1
        else:
            check += 2
        return check

    def update_battlefield(self, Xcoordinate, Ycoordinate, battlefield):
        if battlefield.check_coordinate(Xcoordinate, Ycoordinate) == 0:
            print("\nThis point has already been hit, try another one next time!")
        elif battlefield.check_coordinate(Xcoordinate, Ycoordinate) == 1:
            self.battlefield[Ycoordinate][Xcoordinate] = '  '
            print("\nSorry, you didn't hit an enemy ship!")
        else:
            self.battlefield[Ycoordinate][Xcoordinate] = 'x '
            print("\nGood job, you hit an enemy ship!")
        print("Now, the battlefield looks like this")
    def update_battlefield_for_computer(self,Xcoordinate, Ycoordinate,battlefield):
        if battlefield.check_coordinate(Xcoordinate, Ycoordinate) == 0:
            print("A previous point was hit by the computer again, it wasted its chance to win!")
        elif battlefield.check_coordinate(Xcoordinate, Ycoordinate) == 1:
            self.battlefield[Ycoordinate][Xcoordinate] = '  '
            print("Great, the computer didn't hit you!")
        else:
            self.battlefield[Ycoordinate][Xcoordinate] = 'x '
            print("Sorry, you were hit by the computer!")
    def __str__(self):
        str = ""
        for i in range(self.width + 1):
            for j in range(self.length + 1):
                str += self.battlefield[i][j]
            str += "\n"
        return str

    def points_for_1(self):
        count = 0
        for i in range((int(self.length / 2)) + 1, self.length + 1):
            for j in range(1, self.width + 1):
                if self.battlefield[j][i] == 'x ':
                    count += 1
        return count

    def points_for_2(self):
        count = 0
        for i in range(1, (int(self.length / 2)) + 1):
            for j in range(1, self.width + 1):
                if self.battlefield[j][i] == 'x ':
                    count += 1
        return count


# ==================================================================================================================================#
def set_for_1():
    # for the player#
    roster = ['Battleship', 'Cruizer', 'Destroyer', 'Corvette']
    b1 = Battlefield()
    print("*************Welcome, Player! The game has started! Enjoy and try to win!*************\n")
    print("The original battlefield looks like this")
    print(b1)
    print('The left is your field and the right is enemy field!')
    print("You have the following 4 ships:\n"
          "'Battleship' with length of 5\n"
          "'Cruizer' with length of 4\n"
          "'Destroyer' with length of 3\n"
          "'Corvette' with length of 2\n\n"
          "You need to put the ORIENTATION and LOCATION of your boat following the sequence above\n"
          "         For orientation, you need to enter 'V' for vertical and 'H' for horizontal\n"
          "         For location, you need to enter x and y coordinate for the fore of your current boat\n"
          "*Please make sure all of your vessles are placed entirely within your half of the battlefield*\n")
    length = 5
    for i in range(4):
        direction = input('Please enter the orientation of your ' + roster[i])
        while direction != 'V' and direction != 'H':
            print('Please enter a valid orientation for your ship')
            direction = input('Please enter the orientation of your ' + roster[i])
        try:
            x = int(input("Please set up the x (ranging from 1-4) of your " + roster[i]))  # 如果输入的不是整数，也会报错，那这个漏洞还要改吗？
            y = int(input("Please set up the y (ranging from 1-8) of your " + roster[i]))
        except ValueError:
            continue
        while x not in [1, 2, 3, 4] or (direction == "H" and x + length - 1 > 4) \
                or y not in [1, 2, 3, 4, 5, 6, 7, 8] or (direction == "V" and y + length - 1 > 8):
            print('Please enter a valid orientation and x/y coordinate to make sure it is not out of scope')
            direction = input('Please enter the orientation of your ' + roster[i])
            try:
                x = int(input("Please set up the x (ranging from 1-4) of your " + roster[i]))
                y = int(input("Please set up the y (ranging from 1-8) of your " + roster[i]))
            except ValueError:
                continue
        while b1.battlefield[y][x] == "@ ":
            print(
                "Please enter a valid orientation and x/y coordinate to make sure it is not the same as one of the previous boats")
            try:
                direction = input('Please enter the orientation of your ' + roster[i])
                x = int(input("Please set up the x (ranging from 1-4) of your " + roster[i]))
                y = int(input("Please set up the y (ranging from 1-8) of your " + roster[i]))
            except ValueError:
                continue
        a_ship = Ship(length, direction, 1)
        a_ship.set_ship(x, y)
        b1.init_my_battlefield(a_ship)
        print("After this round of setting, now your battlefield looks like this")
        print(b1)
        length -= 1
    return b1


def set_for_2():
    # for computer
    roster = ['Battleship', 'Cruizer', 'Destroyer', 'Corvette']
    b2 = Battlefield()
    length = 5
    for i in range(4):
        k = random.randint(0, 1)
        list0 = ['H', 'V']
        direction = list0[k]
        x = random.randint(5, 8)
        y = random.randint(1, 8)
        while (direction == "H" and x + length - 1 > 8) or (direction == "V" and y + length - 1 > 8):
            m = random.randint(0, 1)
            list1 = ['H', 'V']
            direction = list1[m]
            x = random.randint(5, 8)
            y = random.randint(1, 8)
        while b2.battlefield[y][x] == "@ ":
            n = random.randint(0, 1)
            list2 = ['H', 'V']
            direction = list2[n]
            x = random.randint(5, 8)
            y = random.randint(1, 8)
        a_ship = Ship(length, direction, 2)
        a_ship.set_ship(x, y)
        b2.init_my_battlefield(a_ship)
        length -= 1
    return b2


# ==================================================================================================================================#
def attack_for_1(b1, b2):  # for the player#
    try:
        x = int(input("\nPlayer, guess one x coordinate (ranging from 5 to 8)of computer's ship "))
        y = int(input("Player, guess one y coordinate (ranging from 1 to 8)of computer's ship "))
        while x not in [5, 6, 7, 8] or y not in [1, 2, 3, 4, 5, 6, 7, 8]:
            print('Please enter a valid x/y coordinate to make sure it is in the enemy field')
            x = int(input("Player, guess one x coordinate (ranging from 5 to 8)of your computer's ship "))
            y = int(input("Player, guess one y coordinate (ranging from 1 to 8)of your computer's ship "))
    except ValueError:
        print("Please enter a valid integer for x/y")
        x = int(input("Player, guess one x coordinate (ranging from 5 to 8)of your computer's ship "))
        y = int(input("Player, guess one y coordinate (ranging from 1 to 8)of your computer's ship "))
    b1.update_battlefield(x, y, b2)
    print(b1)
    print("Now, it is the computer's turn to attack you")
    print("After the attack of the computer...")


def attack_for_2(b1, b2):  # for the computer#

    x = random.randint(1, 4)
    y = random.randint(1, 8)
    b2.update_battlefield_for_computer(x,y,b1)


# ==================================================================================================================================#
def main():
    b1 = set_for_1()
    b2 = set_for_2()
    for i in range(10):
        attack_for_1(b1, b2)
        attack_for_2(b1, b2)
    p1 = b1.points_for_1()
    p2 = b2.points_for_2()
    print("You have finished the game!")
    print("After calculating the points for you and the computer")
    if p1 > p2:
        print("Congratulations! You win!")
    elif p1 < p2:
        print("Sorry, the computer wins! Try it next time!")
    else:
        print("You and the computer got the same score! Slug it out next time!")


main()
