# python has got datetime module to handle date and time.
import datetime
print(dir(datetime))
# with dir or help built-in commands it is possible to know the available functions in a certain module.

### Getting datetime information
from datetime import datetime
now = datetime.now()
print(now) # current date and time
day = now.day # current day
month = now.month # current month
year = now.year # current year
hour = now.hour # current hour
minute = now.minute # current minute
second = now.second # current second
timestamp = now.timestamp() # current timestamp
print(day, month, year, hour, minute, second)
print('timestamp:', timestamp)
#Timestamp or unix timestamp is the number of seconds elapsed from January 1, 1970, 00:00:00 (UTC). It is used to track date and time in computing.

## Formatting Date Output using strftime
new_year = datetime(2020, 1, 1) # year, month, day
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute, second)
print(f'{day}/{month}/{year}, {hour}:{minute}:{second}') 
# By default, hour, minute, second are zero

from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime('%H:%M:%S')
print('time:', t) 
time_one = now.strftime('%m/%d/%Y, %H:%M:%S') 
# mm/dd/yyyy H:M:S format
print('timeone:', time_one)
time_two = now.strftime('%d/%m/%Y, %H:%M:%S')
# dd/mm/yyyy H:M:S format
print('timetwo:', time_two) 

## string to time using strptime
date_string = '21 June, 2018'
print('date_string:', date_string)
date_object = datetime.strptime(date_string, '%d %B, %Y')
print('date_object =', date_object) 

## using date from datetime
from datetime import date
d = date(2020, 1, 1)
print(d)
print('current date:', d.today()) # current date
# date object of today's date
today = date.today()
print('current year:', today.year) 
print('current month:', today.month)
print('current day:', today.day)

## Time Objects to represent time
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time() # time object
print('a =', a)
# time(hour, minute and second)
b = time(10, 30, 50) 
print('b =', b) 
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print('c =', c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555) 
print('d =', d) 

##difference between two points in time using date and datetime
today = date(year=2023, month=10, day=17) # current date
new_year = date(year=2024, month=1, day=1) # new year date
time_left_for_newyear = new_year - today
print('time left for new year:', time_left_for_newyear) 

t1 = datetime(year = 2023, month = 10, day = 17, hour = 12, minute = 0, second = 0)
t2 = datetime(year = 2024, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('time left for new year:', diff) 

## difference between two points in time using timedelta
from datetime import timedelta
t1 = timedelta(weeks=2, days=6, hours=7, minutes=30)
t2 = timedelta(days=4, hours=3, minutes=10)
t3 = t1 - t2
print('t3 =', t3)