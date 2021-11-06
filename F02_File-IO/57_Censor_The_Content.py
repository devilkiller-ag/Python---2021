words = ['bewakoof', 'pagal', 'rascal', 'donkey']

with open ('censorit.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%@&^#")
    with open ('censorit.txt', 'w') as f:
        f.write(content)