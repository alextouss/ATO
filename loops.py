for i in [1, 2, 3, 4, 5]:
    first = i  # first line in "for i" block
    for j in [1, 2, 3, 4, 5]:
        second = j*10  # first line in "for j" block
        print(j*10 + i*1)  # last line in "for j" block
    print(i*10000)  # last line in "for i" block
print('done looping')
