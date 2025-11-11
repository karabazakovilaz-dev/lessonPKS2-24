    # Генератор списков
    data = []
    for i in range(10):
        if i % 2 ==0:
            data.append(i)
    print(data)
    ######
    data2=[i for i in range(10)]
    print(data2)
    ###### dict comprehension
    marks = {
        'gena':40,
        'alla':50,
        'bini':30,
    }
    newMarks = [v for k,v in marks.items()]
    print(newMarks)



    my_str = "a2gf4ye45gfv2yuk"
    nums = []
    temp = ''
    for i in my_str:
        if i.isdigit():
            temp+=i
        elif temp:
            nums.append(int(temp))
            temp = ''
    if temp:
        nums.append(int(temp))
    print(nums):



 