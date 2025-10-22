## exercises: day 16

#1. get the current day, month, year, hour, minute, and timestamp from datetime module
import datetime
now = datetime.datetime.now() # current date and time
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp:', timestamp)

#2. format the current date using this format: '%m/%d/%Y, %H:%M:%S'
formatted_date = now.strftime('%m/%d/%Y, %H:%M:%S')
print('formatted date:', formatted_date) 

#3. today is 5 december, 2019. change this time string to time.
date_string = '5 December, 2019'
date_object = datetime.datetime.strptime(date_string, '%d %B, %Y') 
print('date_object=', date_object) 

#4. calculate the time difference between now and new year.
today = datetime.date.today() # current date
new_year = datetime.date(year=2026, month=1, day=1) # new year date
time_left_for_newyear = new_year - today
print('time left for new year:', time_left_for_newyear) 

#5. calculate the time difference between 1 january 1970 and now.
epoch = datetime.datetime(year=1970, month=1, day=1)
now = datetime.datetime.now() 
diff = now - epoch
print('time difference between 1 jan 1970 and now:', diff)

