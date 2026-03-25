# log.txt exists and is encoded in cp949
try:
    with open('log.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())
except UnicodeDecodeError:
    print("Encoding issue occurred.")
except FileNotFoundError:
    print("File not found.")
