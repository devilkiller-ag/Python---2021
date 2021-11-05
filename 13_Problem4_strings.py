from datetime import datetime as dt

letter = '''Dear <|NAME|>,
    Greetings from Yoga Party!
    You are selected for round 3 Yoga.
    Kindly register yourself for Round 3.
    Have a great day ahead!
    Thanks for Regards,
Yogi.                            <|DATE|>'''
# print(letter)

# date = str(dt.now())
date = str(dt.now())[:10]


name = input("Enter user name: \n")
# greet = "Good Afternoon, " + name
# print(greet)

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)

# storyDS = "This story has a  Double   Space!";
# storyNM = "This story does not have any Double Space!";
# print(storyDS.find("  "))
# print(storyDS.replace("  ", " "))
# print(storyNM.find("  "))
