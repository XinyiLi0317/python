#第12章

#手続き型プログラミング

pop=[]
jpop=[]

def collect_songs():
    song="曲名を入力してください:"
    ask="pかjのどちらかを入力してください。qで終わります:"

    while True:
        genre=input(ask)
        if genre=="q":
            break

        if genre=="p":
            p=input(song)
            pop.append(p)

        elif genre=="j":
            j=input(song)
            jpop.append(j)

        else:
            print("不正な値です")
            print("pop songs: ",pop)
            print("jpop songs: ",jpop)

collect_songs()

#副作用を起こす関数のわかりやすい例

a=0

def increment():
    global a
    a+=1


#副作用のない関数の例

def increment():
    return a+1

#
#

class Apple:
    def __init__(self,w,c,t,p): #wは重さ、tは味、cは色、pはplace
        self.weight=w
        self.color=c
        self.place=p
        self.taste=t
        print("created!")

#

import math
class Circle:
    def __init__(self,r):
        self.radius=r

    def area(self):
        return math.pi*self.radius**2
    
circle= Circle(2)
print(circle.area())
    
#

class Triangle:
    def __init__(self,b,h):
        self.base=b
        self.height=h

    def area(self):
        return self.base*self.height*1/2
    
triangle=Triangle(1,2)
print(triangle.area())

#

class Hexagon:
    def __init__(self,s1,s2,s3,s4,s5,s6):
        self.side1=s1
        self.side2=s2
        self.side3=s3
        self.side4=s4
        self.side5=s5
        self.side6=s6

    def perimeter(self):
        return self.side1+self.side2+self.side3+self.side4+self.side5+self.side6
    
hexagon=Hexagon(1,2,3,4,5,6)
print(hexagon.perimeter())





#
#
#
#
#
#
#
#
#
#