with open('input.txt', 'r') as f:
    inp = f.readlines()
    safe = 0
    for l in inp:
        l = l.replace('\n', '')
        nums = l.split(' ')
        # Use lambda to convert the list of strings to a list of integers
        nums = list(map(lambda x: int(x), nums))
        prev = nums[0]
        decreasing = False
        increasing = False
        unsafe = False
        for i in nums[1:]:
            if i < prev:
                decreasing = True
                if increasing:
                    #print("unsafe")
                    unsafe = True
                    break
                #print('decreasing')
            elif i > prev:
                increasing = True
                if decreasing:
                    #print("unsafe")
                    unsafe = True
                    break
                #print('increasing')
            else:
                #print("unsafe")
                unsafe = True
                break
            diff = abs(i - prev)
            if diff < 1 or diff > 3:
                #print("unsafe")
                unsafe = True
            prev = i
        if not unsafe:
            safe += 1
        #print('---')
    print(safe)