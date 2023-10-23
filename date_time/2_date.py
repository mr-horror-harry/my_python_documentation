import datetime as dt
from datetime import date as d

t3 = dt.date.today()
print(t3)
print("Day:", t3.day, " Month:", t3.month, " Year:", t3.year)
print(t3.ctime()) #change time timestamp

#diff between two days
date1 = d(2003,3,13)
date2 = d.today()
print(date2-date1)