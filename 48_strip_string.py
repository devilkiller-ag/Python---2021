def striper_and_replacer(string, word):
    newstr = string.strip()
    newstr = newstr.replace(word, 'world')
    return newstr

thisStr = "               Harry is     a good boy in this word.                                                   "
print(thisStr)
print(striper_and_replacer(thisStr, 'is'))