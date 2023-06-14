#第7章　ループ

#

name="Ted"
for character in name:
    print(character)



shows=["GOT","Narcos","Vice"]
for show in shows:
    print(show)


coms=("A.","B.","C")
for show in coms:
    print(show)


people={"a":"A",
        "b":"B",
        "c":"C",
        }

for character in people:
    print(character)


tv=["GOT","Narcos","Vice"]
i=0
for show in tv:
    new=tv[i]
    new=new.upper()
    tv[i]=new
    i += 1

print(tv)



tv=["GOT","Narcos","Vice"]
for i, new in enumerate(tv):
    new=tv[i]
    new=new.upper()
    tv[i]=new

print(tv)


#

tv=["Got","Narcos","Vice"]
coms=["Arrested development","friends","always sunny"]
all_shows=[]

for show in tv:
    show=show.upper()
    all_shows.append(show)

for show in coms:
    show=show.upper()
    all_shows.append(show)

print(all_shows)


#range


for i in range(1,11):
    print(i)


#while

x=10
while x>0:
    print('{}'.format(x))
    x-=1
print("I Love you")


while True:
    print("I Love You")


#break

for i in range(1,100):
    print(i)
    break


qs=["what is your name?",
    "what is your fav. color"
    "what is your quest"]

n=0
while True:
    print("Type q to quit")
    a=input(qs[n])
    if a =="q":
        break
    n=(n+1)%3

#continue

for i in range(1,6):
    if i == 3:
        continue
    print(i)


i=1
while i<=5:
    if i==3:
        i +=1
        continue
    print(i)
    i += 1


#入れ子のループ

for i in range(1,3):
    print(i)
    for letter in ["a","b","c"]:
        print(letter)


list1=[1,2,3,4]
list2=[5,6,7,8]
added=[]
for i in list1:
    for j in list2:
        added.append(i+j)

print(added)




#

while input('y or n')!='n':
    for i in range(1,6):
        print(i)

#
#チャレンジ

#1



list1=["waking","andrew","sa","vipa"]
for name in list1:
    print(name)


#2

for i in range(25,50):
    print(i)


#3

#enumerate
#pythonのenumerate()関数を使うと、
#forループの中でリストやタプルなどのイテラブルオブジェクトの要素と同時にインデックス番号（カウント、順番）を取得できる。
#インデックスは任意の値から開始可能


list1=["waking","andrew","sa","vipa"]
for i, new in enumerate(list1):
    new=list1[i]
    new=new.upper()
    list1[i]=new

print(list1)

#


#


#


#


#
