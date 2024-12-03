
with open('test.txt', 'r') as f:
    inp = f.readlines()
    for l in inp:
        print(l)
        l = l.replace('\n', '')