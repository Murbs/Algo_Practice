# HackerRank-LeapYear

<H1>The Problem</H1>

An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

```Python
def is_leap(year):
    leap = False
    
    # Code goes here

year = int(raw_input())
print is_leap(year)
```

<H3>Solution 1</H3>

My first idea was to write an if-else statement to check the conditions laid out in the problem. If year is divisible by 4 and 400, and NOT divisble by 100, leap evaluates to true, else leap will stay false.

```Python
def is_leap(year):
    leap = False
    
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        leap = True    
    return leap
    
year = int(raw_input())
print is_leap(year)
```

<H3>Solution 2</H3>

However, I read a helpful comment in the challenge discussions explaining the redundancies of using an if/else statement to evaluate what is already a boolean value. The 'if' condition can be removed entirely and evaluated as is using the same logic.

```Python
def is_leap(year):

    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

year = int(raw_input())
print is_leap(year)
```
