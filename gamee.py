import random


counts =3
answer =random.randint(1,10)

while counts > 0:
    temp=input("猜我想的是什么:")
    guess=int(temp)

    if guess == answer:
            print("6")
            print("牛啊牛啊")
            break
    else:
        if guess <answer:
            print("小了")
        else:
            print("大了")
        counts = counts - 1

print("不玩了") 
