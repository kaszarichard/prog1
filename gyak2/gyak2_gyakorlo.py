while True:
    try:
        x = int(input("Adj meg egy számot: "))
        y = int(input("Adj meg egy számot: "))
        if ((x+y)//2)>60:
            break

    except ValueError:
        print("Nem megfelelő szám!")