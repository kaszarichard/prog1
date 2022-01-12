import random


wheel = set(range(0,37))
odd = set(range(1,37,2))
even = wheel - odd
red = set( [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36] )
black = wheel - red
small = set(range(0,19))
large = wheel - small
wheel.add('00')

money = int(input("Dollars in game: "))

predictions = {'odd':odd, 'even':even, 'red':red, \
               'black': black, 'small': small,\
               'large': large, '00':set()}

while True:
    bet = input("Give a bet: ")
    if bet == "end game":
        break
    bet = int(bet)
    pred = input("Next prediction: ")
    win = False
    num = random.choice(list(wheel))
    if num == '00':
        print("The number is {}".format(num))
        if pred == '00':
            win = True
    else:
        for k,v in predictions.items():
            if num in v:
                print("The {} is {}".\
                      format(num,k))
                if pred == k:
                    win = True

    if win:
        money += bet
        print("You won!, current money: {}".\
              format(money))
    else:
        money -= bet
        print("You lost!, current money: {}". \
              format(money))

    if money == 0:
        print("You lost all your money! End of game...")
        break