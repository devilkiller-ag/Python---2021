file1 = "this.txt"
file2 = "this_copy.txt"


with open(file1) as f1:
    content1 = f1.read()

with open(file2) as f2:
    content2 = f2.read()

if(content1 == content2):
    print("files are identical!")
else:
    print("files are not identical!")
