# test.txt is encoded in cp949
with open('test.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)
