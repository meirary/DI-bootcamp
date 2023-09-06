import datetime

birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")

birthdate = datetime.datetime.strptime(birthdate_str, "%d/%m/%Y")

today = datetime.date.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

is_leap_year = (birthdate.year % 4 == 0 and (birthdate.year % 100 != 0 or birthdate.year % 400 == 0))

cake = '''
       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
'''

if is_leap_year:
    print(cake)
    print(cake)

candles = age % 10

if candles != 0:
    cake_with_candles = cake.replace("i", "i" * candles)
    print(cake_with_candles)
