translate = {'pankha' : 'fan',
            'moti': 'perl',
            'vastu': 'item'}
print("Options are: ", translate.keys())
a = input("Enter the hindi word: ");

# print("The meaning of your word is: ", translate[a]) # Will throw error if the input is not present in the translate dictionary

# An Better Secnerio - this will not throw any error if the input is not present in the translate dictionary rather it will return 'None'
print("The meaning of your word is: ", translate.get(a))

