from os import truncate


content = True
i = 0
with open('log.txt') as f:
    while content:
        content = f.readline()
        i += 1
        # print(content)
        if 'python' in content.lower():
            print("Log file contains the text 'python' at line number " + str(i) + '.');
        # else:
        #     print("Log file does not contains the text 'python'.")
    