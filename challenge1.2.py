# leap year


def isleapyear(year):
  if (year % 4 == 0):
    if (year % 100 == 0):
      if (year % 400 == 0):
        return true
      else:
        return false


year = int(input("enter a year : "))

if isleapyear(year):
  print("{} is a leap year.".format(year))
else:
  print("{} is not a leap year.".format(year))
