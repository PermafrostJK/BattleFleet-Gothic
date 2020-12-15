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


    def attack(self):
        x=int(input('x coordinate: '))
        y=int(input('y coordinate: '))
        if [y,x] in self.location:
            print('You hit and win!')
            return True

print('There are four gold sites to search among the sixteen sites')
print('Please enter the coordinate in order to find the gold')
p=Battlefield(4,4,[])
p.update_battlefield()
for i in range(5):
    print('Next one!')
    if p.attack()==True:
        print('The player is champion!')
        break
else:
    print('Nobody found!')
print('This is the true map!')
print('x is gold site and o is empty!')
for each in p.battlefield:
    print(each)

            
