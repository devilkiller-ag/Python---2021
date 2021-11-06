age = int(input("Enter your age: "))

if(age > 18 and age < 52):
    print("You can play with us!")
elif(age > 12 and age <= 18):
    print("You can learn how to play with us!")
else:
    print("You can watch our game!")

if(age == 12  or age == 52):
    print(age)