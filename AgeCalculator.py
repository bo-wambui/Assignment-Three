from datetime import datetime

#A program to calculate age 
date = datetime.now()
year = int(date.year)
month = int(date.month)
day = int(date.day)

first_name = input("What is your first name?")
last_name = input ("What is your last name?")
user_year = int(input("What year were you born?"))
age = year - user_year

print ("Hello,"+first_name+" "+last_name+" You are", age ,"years old")

if age > 17:
    print ("You can watch an R rated movie, but don't. Do something better with your life honestly")
elif age >12 <17:
    print ("You can watch a movie rated PG-13")   
else:
    print("You can only watch PG rated movies.")    
