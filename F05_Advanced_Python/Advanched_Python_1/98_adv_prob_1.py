def readFile(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f'File {filename} is not found.')
    except Exception as e:
        print(f'Your input caused an error: {e}')

readFile("F05_Advanced_Python\\f1.txt")
readFile("F05_Advanced_Python\\f2.txt")
readFile("F05_Advanced_Python\\f32.txt")