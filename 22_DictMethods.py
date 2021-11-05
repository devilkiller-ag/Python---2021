myDict = {
    "fast": "In a quick manner",
    "harry": "CodeWithHarry",
    "marks": [1, 2, 3],
    "anotherDict": {
        "Harrish": 'Gammer',
        "Ashmit": 'Coder'
    },
    1: 2
}

print(type(myDict.keys()))
keyList = list(myDict.keys())
print(keyList)

print(myDict.keys())  # Prints the keys of the dictionary
print(myDict.values())  # Prints the keys of the dictionary
# Prints the (key, value) for all contents of the dictionary
print(myDict.items())
print(myDict)
updateDict = {
    'lovish': 'LAN',
    'movish': 'MAN',
    "harry": 'Dancer'
}
# Update the myDict dictionary by adding key-value pairs from updateDict
myDict.update(updateDict)
print(myDict)

print(myDict.get("harry"))  # Prints value associated with key 'harry'
print(myDict["harry"])  # Prints value associated with key 'harry'

# The difference between .get() and [] syntax in Dictionaries?

# -----> returns None as harry2 is not present in the dictionary
print(myDict.get("harry2"))
# -----> throws an error as harry2 is not present in the dictionary
print(myDict["harry2"])
