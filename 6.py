# 5/18
# 第6章　文字列操作

#三重クォート文字列: 文字列を複数行書きたい場合場合””” ”””

""" I
    Love
    you
"""

#インデックス：文字列中のどの文字でも、インデックスを指定して取り出せます

author="Holly"
author[0]
author[1]
author[2]
author[3]
author[4]
author[5]

author[-1]
author[-2]
author[-3]

#文字列はイミュータブル（変更不可）
#文字列は、その一部を別の文字に入れ替えられません
#文字を入れ替えたい時は、新しい文字列を作らなければなりません

ff="Xiao Yuchen"
ff="Da shabi"
ff

#文字列の足し算

"cat"+"in"+"hat"

"cat "+"in "+"the "+"hat "


#文字列の掛け算

"xyc"*3

#大文字小文字変換

"i love you".upper()

"I LOVE YOU".lower()

"i love you".capitalize()

#書式化:文字列の一部をあとで穴埋めして新しい文字列を返せます

"こんにちは、{}".format("Li")

name="Li"
"こんにちは、{}".format(name)

author="Li Xinyi"
"こんにちは、{}".format(author)

#チャレンジ

#1

moji="カミュ"

moji[0]
moji[1]

#2


"私は昨日()を書いて、()に送った".format("python, Onishi")

#3

"aldous Huxley was born in 1894".capitalize()

#4

"どこで？だれが？いつ？".split("？")

#5???

list="The","fox","jumped","over","the","fence","."
result=" ".join(list)
result=result[0:-2]+"."
result

#6

equ="A screaming comes across the sky"
equ=equ.replace("s","$")
print(equ)

#7

"Hemingway".index("m")

#8

"彼は\"大好きだ\"と言った"

#9

print("three "+"three "+"three ")

print("three "*3)


#10
fict="四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
fict[0:10]






#
#
#