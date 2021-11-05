myDict = {
    "Fast": "In a quick manner",
    "Harry": "CodeWithHarry",
    "List" : [1,2,3],
    "AnotherDict": {
        "Harrish": 'Gammer',
        "Ashmit": 'Coder'
    }
}
print(myDict)
print(myDict['Fast'])
print(myDict['Harry'])
print(myDict['List'])
print(myDict['AnotherDict'])
print(myDict['AnotherDict']['Ashmit'])

myDict['List'] = [23, 5, 22, 1, 44]
print(myDict)