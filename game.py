
class Ship:
    def __init__(self,length,direction,lable): # lable added to differenctiate between players 1 and 2
        try:
            if direction != 'V' or direction != 'H':
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
        for ship in Ship:
            location+=ship.actual_location
        for actual_boat in location:
            print(actual_boat)
            if the_point==actual_boat:
                self.battlefield[Ycoordinate][Xcoordinate]='x'
                break
        if the_point not in location:
            self.battlefield[Ycoordinate][Xcoordinate]=' '

    def check_coordinate(self,Xcoordinate,Ycoordinate):
        if self.battlefield[Ycoordinate][Xcoordinate]='x':
            return False
        elif self.battlefield[Ycoordinate][Xcoordinate]=' ':
            return False
        else:
            return True

    def init_my_battlefield(self,Ship):
        location=[]
        for ship in Ship:
            location+=ship.actual_location
        for actual_boat in location:
            self.battlefield[actual_boat[1]][actual_boat[0]]='@'

    def win_game(self):
        count=0
        for i in range(self.length):
            for j in range(self.width):
                if self.battlefield[i][j]=='x':
                    count=count+1
        if count==9:
            return True
        else:
            return False
