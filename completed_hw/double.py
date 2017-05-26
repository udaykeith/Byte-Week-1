import datetime
from datetime import date

def double_day(b1, b2):
	delta = b1 - b2

    double_day = b1 + delta 
    return double_day
b1 = date(2006, 12, 26)
b2 = date(2003, 10, 11)
print (double_day(b1,b2))

