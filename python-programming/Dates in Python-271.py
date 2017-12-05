## 1. The Time Module ##

import time
current_time = time.time()
print(current_time)

## 2. Converting Timestamps ##

import time
current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour

## 3. UTC ##

from datetime import datetime

current_datetime = datetime.utcnow()
current_month = current_datetime.month
current_year = current_datetime.year

## 4. Timedelta ##

import datetime

kirks_birthday = datetime.datetime(year = 2233, month = 3, day = 22)
diff = datetime.timedelta(weeks = 15)
before_kirk = kirks_birthday - diff

## 5. Formatting Dates ##

from datetime import datetime

mystery_date_formatted_string=mystery_date.strftime("%I:%M%p on %A %B %d, %Y")

## 6. Parsing Dates ##

from datetime import datetime
mystery_date_2 = datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")

## 8. Reformatting Our Data ##

from datetime import datetime

for post in posts:
    post[2] = float(post[2])
    post[2] = datetime.fromtimestamp(post[2])

## 9. Counting Posts from March ##

march_count = 0

for post in posts:
    if post[2].month == 3:
        march_count += 1

## 10. Counting Posts from Any Month ##

march_count = 0

for row in posts:
    if row[2].month == 3:
        march_count += 1
        
def num_post_month(lst, month):
    count = 0
    for post in lst:
        if post[2].month == month:
            count += 1
    return count

aug_count = num_post_month(posts, 8)
feb_count = num_post_month(posts, 2)