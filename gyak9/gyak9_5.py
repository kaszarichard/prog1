import datetime

napok = lambda y1, m1, d1, y2, m2, d2 : \
    str((datetime.date(y2,m2,d2) - datetime.date(y1,m1,d1))\
    .days) + ' nap'

print(napok(2012,11,2,2014,7,11))