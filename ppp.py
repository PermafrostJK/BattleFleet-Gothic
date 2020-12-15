import random


class Battlefield:
    def __init__(self, width, length, location):
        self.battlefield = [['o ' for i in range(length+1)] for j in range(width+1)]
        self.width = width
        self.length = length
        self.location=[]

    def update_battlefield(self):
        i=3
        while i>=0:
            row=random.randint(0,2)
            column=random.randint(0,2)
            if [row,column] not in self.location:
                self.location.append([row,column])
                self.battlefield[column][row]='x '
                i=i-1
        print(self.location)
        return self.battlefield


    def attack(self,list0):
        if list0 in self.location:
            print('You hit and win!')
            return True

            
