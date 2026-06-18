#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
Author: "Student Name"
Semester: "Fall/Winter/Summer YYYY"

The python code in this file (assignment1.py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"

    if month == 2:
        if leap_year(year):
            return 29
        return 28

    days = {
        1:31, 3:31, 5:31, 7:31, 8:31, 10:31, 12:31,
        4:30, 6:30, 9:30, 11:30
    }

    return days[month]

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    lyear = year % 4
    if lyear == 0:
        feb_max = 29 # this is a leap year
    else:
        feb_max = 28 # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        feb_max = 28 # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        feb_max = 29 # this is a leap year

    mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    tmp_day = day + 1  # next day

    if tmp_day > mon_max[month]:
        to_day = tmp_day % mon_max[month]  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


def usage():
    "Print a usage message to the user"
    ...


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

    return False

def valid_date(date: str) -> bool:
    try:
        year_str, month_str, day_str = date.split('-')

        # Must be YYYY-MM-DD
        if len(year_str) != 4:
            return False

        if len(month_str) != 2:
            return False

        if len(day_str) != 2:
            return False

        year = int(year_str)
        month = int(month_str)
        day = int(day_str)

        if month < 1 or month > 12:
            return False

        if day < 1:
            return False

        if day > mon_max(month, year):
            return False

        return True

    except:
        return False

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"

    count = 0
    current = start_date

    while True:

        year, month, day = current.split('-')

        dow = day_of_week(
            int(year),
            int(month),
            int(day)
        )

        if dow == 'sun' or dow == 'sat':
            count += 1

        if current == stop_date:
            break

        current = after(current)

    return count

if __name__ == "__main__":
    ...
