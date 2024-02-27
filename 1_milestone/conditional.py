age = 19
number_of_visits = 6

if age > 18 and number_of_visits > 3:
    print("You will get discount of 10 %")
    if number_of_visits > 5:
        print("You will get additional 10% discount")

elif age < 18 and number_of_visits > 5:
    print("You will get discount of 20%")
else:
    print("You will not get discount")