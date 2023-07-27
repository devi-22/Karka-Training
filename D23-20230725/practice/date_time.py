#date&time

"""from datetime import date
curr_date=date(2023,7,25)
print(curr_date)
today_date=date.today().year
print(today_date)
print("\n")

from datetime import time
curr_time=time(12,17,25)
print(curr_time)
today_time=curr_time.hour
print(today_time)
curr_time=curr_time.second
print(curr_time)"""
print("\n")

from datetime import datetime
"""curr_datetime=datetime(2023,7,25,12,17,25)   
print(curr_datetime)
today_datetime=datetime.now()
print(today_datetime)
new_time=today_datetime.strftime("%Y")
print(new_time)"""
time=datetime(2023,7,26,12,45,23)
curr_time=time.strftime("%Y")
print(curr_time)
date_str="26 july 2023"
new_str=datetime.strptime(date_str,"%d %B %Y")
print(new_str)
from datetime import timedelta
end_date=new_str+timedelta(days=5)
print(end_date)

#print("\n")

"""import pytz
curr_time=pytz.timezone("Asia/Kolkata")
curr_datetime=datetime.now(curr_time)
print(curr_datetime)"""


