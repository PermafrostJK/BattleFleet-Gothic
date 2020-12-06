
class Ship:
    def __init__(self,length,direction,lable): # lable added to differenctiate between players 1 and 2
        try:
            if direction != 'V' and direction != 'H':
                raise Exception
            self.length=length
            self.direction=direction
            self.actual_location=[]
            self.lable=lable
             
        except Exception:
            print('Please enter a valid orientation for your ship')

    def set_ship(self,locationX,locationY):
        if self.direction=='V':#vertical
            for i in range(self.length):
                the_boat=[locationX,locationY+i]
                if 1+(self.lable-1)*4<=locationX<=4+(self.lable-1)*4 and 0<=locationY<=8:
                    self.actual_location.append(the_boat)
                 else:
                    return False
        elif self.direction=='H':#horizontal
            for i in range(self.length):
                the_boat=[locationX+i,locationY]
                if 1+(self.lable-1)*4<=locationX<=4+(self.lable-1)*4 and 0<=locationY<=8:
                    self.actual_location.append(the_boat)
                 else:
                    return False
            

class Battlefield:
    def __init__(self,width=8,length=8):
        self.battlefield=[['o'for i in range(width+1)] for j in range(length+1)]
        for i in range(width+1):
            self.battlefield[0][i]=str(i)
        for j in range(length+1):
            self.battlefield[j][0]=str(j)
        self.width=width
        self.length=length
        self.strbattlefield=''
    def update_battlefield(self,Xcoordinate,Ycoordinate):
        the_point=[Xcoordinate,Ycoordinate]
        location=[]
        for ship in Ship: #这个应该会有traceback, 因为Ship是个class
            location+=ship.actual_location
        for actual_boat in location:
            print(actual_boat)
            if the_point==actual_boat:
                self.battlefield[Ycoordinate][Xcoordinate]='x '  ##困惑1，为什么要倒过来写x,y## hmm 我也在想
                print("Good job, you hit an enemy ship!")
                break
        if the_point not in location:
            self.battlefield[Ycoordinate][Xcoordinate]='  '
            print("Sorry, you didn't hit an enemy ship!")

    def check_coordinate(self,Xcoordinate,Ycoordinate): ##困惑2，这个function是做什么的##->原作者说是为了避免重复选择轰炸点
        if self.battlefield[Ycoordinate][Xcoordinate]=='x ':
            return False
        elif self.battlefield[Ycoordinate][Xcoordinate]=='  ':
            return False
        else:
            return True

    def init_my_battlefield(self,Ship):
        location=[]
        for ship in Ship:
            location+=ship.actual_location
        for actual_boat in location:
            self.battlefield[actual_boat[1]][actual_boat[0]]='@ '

    def win_game(self): 
        count_1=0
        count_2=0
        for ship in Ship:
            if ship.lable==1:
                for i in range(ship.length/2+1,self.length+1):
                    for j in range(ship.width):
                        if self.battlefield[i][j]=='x ':
                            count_1+=1
            if ship.lable==2:
                for i  in range(1,ship.length/2+1):
                    for j in range(ship.width):
                        if self.battlefield[i][j]=='x ':
                            count_2+=1
        if count_1<count_2:
            print("the winner is player 2")
        elif count_1>count_2:
            print("the winner is player 1")
        else:
            print("You two got the same score! Slug it out next time!")
    
def __main__():
    roster = ['Battleship', 'Cruizer', 'Destroyer', 'Corvette']
    #for player 1，因为我们没有加入chat system，只能写两遍input
    print("*************Welcome, Player 1! The game has started! Enjoy and try to win!*************\n")
    print("You have the following 4 ships:\n"
          "         'Battleship' with length of 5\n"
          "         'Cruizer' with length of 4\n"
          "         'Destroyer' with length of 3\n"
          "         'Corvette' with length of 2\n\n"
          "You need to put the ORIENTATION and LOCATION of your boat following the sequence above\n"
          "         For orientation, you need to enter 'V' for vertical and 'H' for horizontal\n"
          "         For location, you need to enter x and y coordinate for the fore of your current boat\n"
          "         *Please make sure all of your vessles are placed entirely within your half of the battlefield*\n")
    length = 5
    for i in range(4):
        direction = input('Please enter the orientation of your ' + roster[i])
        x = input("Please set up the x (ranging from 1-4) of your " + roster[i])
        y = input("Please set up the y (ranging from 1-8) of your " + roster[i])
        roster[i] = Ship(length, direction, 1)
        roster[i].set_ship(x,y)
        length -= 1
    Battlefield.init_my_battlefield(Ship)
    # for player 2
    print("*************Welcome, Player 2! The game has started! Enjoy and try to win!*************\n")
    print("You have the following 4 ships:\n"
          "         'Battleship' with length of 5\n"
          "         'Cruizer' with length of 4\n"
          "         'Destroyer' with length of 3\n"
          "         'Corvette' with length of 2\n\n"
          "You need to put the ORIENTATION and LOCATION of your boat following the sequence above\n"
          "         For orientation, you need to enter 'V' for vertical and 'H' for horizontal\n"
          "         For location, you need to enter x and y coordinate for the fore of your current boat\n"
          "         *Please make sure all of your vessles are placed entirely within your half of the battlefield*\n")
    length = 5
    for i in range(4):
        direction = input('Please enter the orientation of your ' + roster[i])
        x = input("Please set up the x (ranging from 5-8) of your " + roster[i])
        y = input("Please set up the y (ranging from 1-8) of your " + roster[i])
        roster[i] = Ship(length, direction, 2)
        roster[i].set_ship(x, y)
        length -= 1
    Battlefield.init_my_battlefield(Ship)
    #以上为分别set两个player
    
    #困惑3#
    #我不确定下面所有有关battlefield的function是不是应该这么写#
    #现在我们的ship class是针对每一艘船的，而不是一个player的所有的船的，所有就会有一些难做的事情#
    #我不知道这里的parameter Ship 是不是我们刚刚pass过的player 2的ship instance,还是包括player 1在内的所有ship instance#
    #如果是后者，解决方法可能是要用在写所有东西之前按lable分类，建立两个class，再分别对他们进行操作#
    #实际上lable是更高一级的分类，四艘船都应该属于这个lable#

    while i in range(10): #由于时间限制模式要和chat system结合，目前只写限定攻击次数的模式，这里面先用10来计算，其实也可以让用户自选回合数#
        x = input("Guess one x coordinate of your opponent's ship ")
        y = input("Guess one y coordinate of your opponent's ship ")
        Battlefield.update_battlefield(x,y)
    Battlefield.win_game()

__main__()    
