#! usr/bin/python2.7.8

months = [31,28,31,30,31,30,31,31,30,31,30,31]

def isleap(year): #Check condition for leap year
    if year % 4 == 0 and year %100 != 0 or year % 400 == 0:
        months.remove(28)
        months.insert(1,29)


#Returns the year, month, day of the next day.
        
def nextDay(year, month, day):

    isleap(year)
    
    if month > 12 or year < 1582 or day > months[month - 1]:       # Check for valid Gregorian date
        return "Invalid Date! \nPlease, Try again"
    else:
        if day == months[month - 1] and month == 12:
            day = 1
            month = 1
            year = year + 1
        elif day == months[month - 1]:
            day = 1
            month = month + 1
        else:
            day = day + 1
 
    return (year, month, day)

print nextDay(1581, 2, 29)
