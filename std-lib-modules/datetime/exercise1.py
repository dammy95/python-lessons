import datetime

# this class method creates a datetime object with the current date and time
now = datetime.datetime.today()

print(now.year)
print(now.hour)
print(now.minute)

print(now.weekday())

print(now.strftime("%a, %d %B %Y"))

long_ago = datetime.datetime(1999, 3, 14, 12, 30, 58)

print(long_ago) # remember that this calls str automatically
print(long_ago < now)

difference = now - long_ago
print(type(difference))
print(difference) # remember that this calls str automatically

if __name__ == '__main__':
  
  today = datetime.datetime.today()

  day1 = today + datetime.timedelta(days=14)
  day2 = day1 + datetime.timedelta(days=14)
  day3 = day2 + datetime.timedelta(days=14)
  day4 = day3 + datetime.timedelta(days=14)
  day5 = day4 + datetime.timedelta(days=14)
  day6 = day5 + datetime.timedelta(days=14)
  day7 = day6 + datetime.timedelta(days=14)
  day8 = day7 + datetime.timedelta(days=14)
  day9 = day8 + datetime.timedelta(days=14)
  day10 = day9 + datetime.timedelta(days=14)

  print('Day 1: ', day1)
  print('Day 2: ', day2)
  print('Day 3: ', day3)
  print('Day 4: ', day4)
  print('Day 5: ', day5)
  print('Day 6: ', day6)
  print('Day 7: ', day7)
  print('Day 8: ', day8)
  print('Day 9: ', day9)
  print('Day 10: ', day10)
