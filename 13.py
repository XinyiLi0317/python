# #第13章


# #カプセル化


# #パブリック変数
# class PublicPrivateExample:
#     def _init_(self):
#         self.public="safe"
#         self._unsafe="unsafe"

#         def public_method(self):
#             pass

#         def _unsafe_method(self):
#             pass


# #ポリモーフィズム

# shapes=[tr1,sw1,cr1]
# for a_shape in shapes:
#     a_shape.draw()


# #継承

# class Shape:
#     def _init_(self,w,l):
#         self.width=w
#         self.len=l

#     def print_size(self):
#         print("{}by{}".format(self.width, self.lem))


# class Square(Shape):
#     def area(self):
#         return self.width*self.len
    
#     def print_size(self):
#         print("I am {} by {}". format(self.width, self.len))

# a_square=Square(20,20)
# a_square.print_size()

#
#チャレンジ

# class Rectangle:
#     def __init__(self,w,l):
#         self.width=w
#         self.len=l
    
#     def calculate_perimeter(self):
#         return (self.width+self.len)*2
    
# rectangle=Rectangle(1,2)
# print(rectangle.calculate_perimeter())
    

# class Square:
#     def __init__(self,s):
#         self.side=s
    
#     def calculate_perimeter(self):
#         return self.side*4
    
# square=Square(1)
# print(square.calculate_perimeter())
    
# #2

# class Square:
#     def __init__(self,s):
#         self.side=s
    
#     def calculate_perimeter(self):
#         return self.side*4
    
#     def change_size(self,s1):
#         self.side += s1

# square=Square(10)
# print(square.side)

# square.change_size(-2)
# print(square.side)

#3
# class Shape:
#     def what_am_i(self):
#         print("I am a shape")


# class Rectangle(Shape):
#     def __init__(self,w,l):
#         self.width=w
#         self.len=l
    
#     def calculate_perimeter(self):
#         return (self.width+self.len)*2

# class Square(Shape):
#     def __init__(self,s):
#         self.side=s
    
#     def calculate_perimeter(self):
#         return self.side*4

# rectangle=Rectangle(1,2)
# square=Square(1)
# rectangle.what_am_i()
# square.what_am_i()
#3

# class Horse:
#     def __init__(self,name,owner):
#         self.name=name
#         self.owner=owner

# class Rider:
#     def __init__(self,name):
#         self.name=name

# b=Rider("B")
# a=Horse("A",b)


# print(a.owner.name)

# #第14章

# #チャレンジ
# #1

class Square:
    square_list=[]

    def __init__(self,s):
        self.side=s
        self.square_list.append((self.side))

square1=Square(1)
square2=Square(2)
square3=Square(3)
square4=Square(4)

print(Square.square_list)

#2


class Square:
    square_list=[]
    def __init__(self,s):
        self.side=s

    def print_size(self):
        print("{} by {} by {} by {}".format(self.side,self.side,self.side,self.side))

square=Square(10)
square.print_size()

#3

def compare(obj1,obj2):
    return obj1 is obj2
print(compare("1","a"))


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
#
#
