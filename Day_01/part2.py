import re

with open('input.txt', 'r') as f:
    inp = f.readlines()
    leftSide = []
    rightSide = {}
    for l in inp:
        pattern = r'(\d+)\s{3}(\d+)'
        #print(l)
        l = l.replace('\n', '')
        theMatch = re.match(pattern, l)

        if theMatch:
            x = theMatch.group(1)
            y = theMatch.group(2)
            #print(x, y)
            leftSide.append(int(x))
            if int(y) in rightSide:
                #print("y is in rightSide")
                rightSide[int(y)] = rightSide[int(y)] + 1
            else:
                rightSide[int(y)] = 1
    #print(leftSide)
    #print(rightSide)
    total = 0
    for i in leftSide:
        if i in rightSide:
            #print(i, rightSide[i])
            total += (i * rightSide[i])
    print(total)
    