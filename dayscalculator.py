#! /usr/bin/python2.7


def isleap(year): #Check condition for leap year

    if year % 4 == 0 and year %100 != 0 or year % 400 == 0:
        months = [31,29,31,30,31,30,31,31,30,31,30,31]
        return months
    else:
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        return months


#Returns the year, month, day of the next day.
        
def NextDay(year,month,day):

    months = isleap(year)

    if month > 12 or year < 1582 or day > months[month - 1]: # Check for valid Gregorian date
        return False
    else:
        if day == months[month - 1] and month == 12:
            day = 1
            month = 1
            year += 1
        elif day == months[month - 1]:
            day = 1
            month += 1
        else:
            day += 1
    return year, month, day


# Check if year2-month2-day2 comes after year1-month1-day1

def DateIsBefore(year1,month1,day1,year2,month2,day2):

    if year1 < year2:
        return True
    elif year2 == year1:
        if month1 < month2:
            return True
        elif month2 == month1:
            return day1 < day2
    else:
        return False


#To calculate days between two dates.

def DaysBetweenDates(year1,month1,day1,year2,month2,day2):
    assert not DateIsBefore(year2, month2, day2, year1, month1, day2)   #Breaks the script is DateIsBefore is False
    days = 0
    while DateIsBefore(year1, month1, day1, year2, month2, day2):
        if NextDay(year1,month1,day1) == False:
            return "Invalid Date!"
        else:
            year1,month1,day1 = NextDay(year1,month1,day1)
            days += 1     #Keeps incrememting days until DateIsBefore condition gets false. 
    return days

if __name__ == "__main__":

    print DaysBetweenDates(2001,2,1,2001,3,1)
