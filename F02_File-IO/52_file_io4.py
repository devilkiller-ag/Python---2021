f = open('another.txt', 'w')
f.write("Please write this to the file!")
f.close()

f = open('another.txt', 'a')
f.write("I am appending this to this file!")
f.close()
