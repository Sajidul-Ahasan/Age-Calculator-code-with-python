print("Sir, What is your name ?")
name= input()
print(name,'what is your birthdate?')
print("Birth Year:")
year= int(input())
count=year
print("Birth Month:")
month= input()
if month.title() == 'January':
    month=1;
elif month.title() == 'February':
    month=2;
elif month.title() == 'March' :
    month=3;
elif month.title() == 'April' :
    month=4;
elif month.title() == 'May' :
    month=5;
elif month.title() == 'June' :
    month=6;
elif month.title() == 'July' :
    month=7;
elif month.title() == 'August' :
    month=8;
elif month.title() == 'September' :
    month=9;
elif month.title() == 'October' :
    month=10;
elif month.title() == 'Nobember' :
    month=11;
elif month.title() == 'December' :
    month=12;

print("Birth Date:")
date = int(input())

print("Today's Date:")
t_year= int(input("Year:"))
t_month= input("Month:")
t_date= int(input("Date:"))
if t_month.title() == 'January':
    t_month=1;
elif t_month.title() == 'February':
    month=2;
elif t_month.title() == 'March' :
    t_month=3;
elif t_month.title() == 'April' :
    t_month=4;
elif t_month.title() == 'May' :
    t_month=5;
elif t_month.title() == 'June' :
    t_month=6;
elif t_month.title() == 'July' :
    t_month=7;
elif t_month.title() == 'August' :
    t_month=8;
elif t_month.title() == 'September' :
    t_month=9;
elif t_month.title() == 'October' :
    t_month=10;
elif t_month.title() == 'Nobember' :
    t_month=11;
elif t_month.title() == 'December' :
    t_month=12;
total_day = 0
for i in range(year , t_year-1,1):

    if count%400==0:
        total_day = total_day + 366
    elif count%100==0 :
        total_day = total_day + 365
    elif count%4==0:
        total_day = total_day + 366
    else:
        total_day = total_day + 365
    count = count + 1

if year% 400==0:
    if month == 1:
        total_day = total_day + (365 - 31 + (31 - date))
    elif month == 2:
        total_day = total_day + (365 - (29 + 31) + (29 - date))
    elif month == 3:
        total_day = total_day + (365 - (31 + 29 + 31) + (31 - date))
    elif month == 4:
        total_day = total_day + (365 - (31 + 29 + 31 + 30) + (30 - date))
    elif month == 5:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31) + (31 - date))
    elif month == 6:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30) + (30 - date))
    elif month == 7:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30 + 31) + (31 - date))
    elif month == 8:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31) + (31 - date))
    elif month == 9:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30) + (30 - date))
    elif month == 10:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31) + (31 - date))
    elif month == 11:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30) + (30 - date))
    elif month == 12:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31) + (31 - date))

elif year%100==0:
    if month == 1:
        total_day = total_day + (365 - 31 + (31 - date))
    elif month == 2:
        total_day = total_day + (365 - (28 + 31) + (28 - date))
    elif month == 3:
        total_day = total_day + (365 - (31 + 28 + 31) + (31 - date))
    elif month == 4:
        total_day = total_day + (365 - (31 + 28 + 31 + 30) + (30 - date))
    elif month == 5:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31) + (31 - date))
    elif month == 6:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30) + (30 - date))
    elif month == 7:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30 + 31) + (31 - date))
    elif month == 8:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31) + (31 - date))
    elif month == 9:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30) + (30 - date))
    elif month == 10:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31) + (31 - date))
    elif month == 11:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30) + (30 - date))
    elif month == 12:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31) + (31 - date))

elif year%4==0:
    if month == 1:
        total_day = total_day + (365 - 31 + (31 - date))
    elif month == 2:
        total_day = total_day + (365 - (29 + 31) + (29 - date))
    elif month == 3:
        total_day = total_day + (365 - (31 + 29 + 31) + (31 - date))
    elif month == 4:
        total_day = total_day + (365 - (31 + 29 + 31 + 30) + (30 - date))
    elif month == 5:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31) + (31 - date))
    elif month == 6:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30) + (30 - date))
    elif month == 7:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30 + 31) + (31 - date))
    elif month == 8:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31) + (31 - date))
    elif month == 9:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30) + (30 - date))
    elif month == 10:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31) + (31 - date))
    elif month == 11:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30) + (30 - date))
    elif month == 12:
        total_day = total_day + (365 - (31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31) + (31 - date))

else:
    if month == 1:
        total_day = total_day + (365 - 31 + (31 - date))
    elif month == 2:
        total_day = total_day + (365 - (28 + 31) + (28 - date))
    elif month == 3:
        total_day = total_day + (365 - (31 + 28 + 31) + (31 - date))
    elif month == 4:
        total_day = total_day + (365 - (31 + 28 + 31 + 30) + (30 - date))
    elif month == 5:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31) + (31 - date))
    elif month == 6:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30) + (30 - date))
    elif month == 7:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30 + 31) + (31 - date))
    elif month == 8:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31) + (31 - date))
    elif month == 9:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30) + (30 - date))
    elif month == 10:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31) + (31 - date))
    elif month == 11:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30) + (30 - date))
    elif month == 12:
        total_day = total_day + (365 - (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + 31) + (31 - date))


if t_year % 400==0:
    if t_month == 1:
        total_day = total_day + (t_date)
    elif t_month == 2:
        total_day = total_day + (31+t_date)
    elif t_month == 3:
        total_day = total_day + (31+29+t_date)
    elif t_month == 4:
        total_day = total_day + (31+29+31+t_date)
    elif t_month == 5:
        total_day = total_day + (31+29+31+30+t_date)
    elif t_month == 6:
        total_day = total_day  + (31+29+31+30+31+t_date)
    elif t_month == 7:
        total_day = total_day + (31+29+31+30+31+30+t_date)
    elif t_month == 8:
        total_day = total_day + (31+29+31+30+31+30+31+t_date)
    elif t_month == 9:
        total_day = total_day + (31+29+31+30+31+30+31+31+t_date)
    elif t_month == 10:
        total_day = total_day + (31+29+31+30+31+30+31+31+30+t_date)
    elif t_month == 11:
        total_day = total_day + (31+29+31+30+31+30+31+31+30+31+t_date)
    elif t_month == 12:
        total_day = total_day + (31+29+31+30+31+30+31+31+30+31+30+t_date)
    print(total_day, 'days')
elif t_year%100==0:
    if t_month == 1:
        total_day = total_day + (t_date)
    elif t_month == 2:
        total_day = total_day + (31+t_date)
    elif t_month == 3:
        total_day = total_day + (31+28+t_date)
    elif t_month == 4:
        total_day = total_day + (31+28+31+t_date)
    elif t_month == 5:
        total_day = total_day + (31+28+31+30+t_date)
    elif t_month == 6:
        total_day = total_day + (31+28+31+30+31+t_date)
    elif t_month == 7:
        total_day = total_day + (31+28+31+30+31+30+t_date)
    elif t_month == 8:
        total_day = total_day + (31+28+31+30+31+30+31+t_date)
    elif t_month == 9:
        total_day = total_day + (31+28+31+30+31+30+31+31+t_date)
    elif t_month == 10:
        total_day = total_day + (31+28+31+30+31+30+31+31+30+t_date)
    elif t_month == 11:
        total_day = total_day + (31+28+31+30+31+30+31+31+30+31+t_date)
    elif t_month == 12:
        total_day = total_day + (31+28+31+30+31+30+31+31+30+31+30+t_date)
    print(total_day, 'days')
elif t_year%4==0:
    if t_month == 1:
        total_day = total_day + (t_date)
    elif t_month == 2:
        total_day = total_day + (31+t_date)
    elif t_month == 3:
        total_day = total_day + (31+29+t_date)
    elif t_month == 4:
        total_day = total_day + (31+29+31+t_date)
    elif t_month == 5:
        total_day = total_day + (31+29+31+30+t_date)
    elif t_month == 6:
        total_day = total_day + (31+29+31+30+31+t_date)
    elif t_month == 7:
        total_day = total_day + (31+29+31+30+31+30+t_date)
    elif t_month == 8:
        total_day = total_day + (31+29+31+30+31+30+31+t_date)
    elif t_month == 9:
        total_day = total_day + (31+29+31+30+31+30+31+31+t_date)
    elif t_month == 10:
        total_day = total_day + (31+29+31+30+31+30+31+31+30+t_date)
    elif t_month == 11:
        total_day = total_day + (31+29+31+30+31+30+31+31+30+31+t_date)
    elif t_month == 12:
        total_day = total_day + (31+29+31+30+31+30+31+31+30+31+30+t_date)
    print(total_day, 'days')
else:
    if t_month == 1:
        total_day = total_day + (t_date)
    elif t_month == 2:
        total_day = total_day + (31 + t_date)
    elif t_month == 3:
        total_day = total_day + (31 + 28 + t_date)
    elif t_month == 4:
        total_day = total_day + (31 + 28 + 31 + t_date)
    elif t_month == 5:
        total_day = total_day + (31 + 28 + 31 + 30 + t_date)
    elif t_month == 6:
        total_day = total_day + (31 + 28 + 31 + 30 + 31 + t_date)
    elif t_month == 7:
        total_day = total_day + (31 + 28 + 31 + 30 + 31 + 30 + t_date)
    elif t_month == 8:
        total_day = total_day + (31 + 28 + 31 + 30 + 31 + 30 + 31 + t_date)
    elif t_month == 9:
        total_day = total_day + (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + t_date)
    elif t_month == 10:
        total_day = total_day + (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + t_date)
    elif t_month == 11:
        total_day = total_day + (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + t_date)
    elif t_month == 12:
        total_day = total_day + (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + t_date)
    print("Your total living day is",total_day, 'days.')