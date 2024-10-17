name = input("what is your name?")
birth_year = input("what is the year of your birth?")

print(f"Hello,{name}!")

from datetime import datetime
this_year = datetime.now().year

print(f"you must be {int(this_year) -int(birth_year) }")