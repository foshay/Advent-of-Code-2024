import re

with open('input.txt', 'r') as f:
    inp = f.readlines()
    leftList = []
    rightList = []
    for l in inp:
        pattern = r'(\d+)\s{3}(\d+)'
        #print(l)
        l = l.replace('\n', '')
        theMatch = re.match(pattern, l)

        if theMatch:
            x = theMatch.group(1)
            y = theMatch.group(2)
            #print(x, y)
            leftList.append(int(x))
            rightList.append(int(y))
    leftList.sort()
    rightList.sort()
    diffList = []
    for i in range(len(leftList)):
        diffList.append(abs(rightList[i] - leftList[i]))
    print(sum(diffList))            