li = [1,2,3,4,5,6,7,8,9]
aumento = 0


while True:
    aumento +=1
    if aumento == 5:
        break
    for x in range(0,len(li)):
        for y in range(0,9):
            li[y]+=1
            if li[y] == 10 or li[y] == 11 or li[y] == 12 or li[y] == 13 or li[y] == 14 or li[y] == 15:
                li[y] = 1
        print('''\n\n
    {}  |  {}  |  {}
    ----------------
    {}  |  {}  |  {}
    ----------------
    {}  |  {}  |  {}
    '''.format(li[0],li[1],li[2],li[3],li[4],li[5],li[6],li[7],li[8],))
        print('''\n\n
    {}  |  {}  |  {}
    ----------------
    {}  |  {}  |  {}
    ----------------
    {}  |  {}  |  {}
    '''.format(li[3],li[7],li[2],li[0],li[6],li[5],li[4],li[1],li[8],))
        print('''\n\n
    {}  |  {}  |  {}
    ----------------
    {}  |  {}  |  {}
    ----------------
    {}  |  {}  |  {}
    '''.format(li[4],li[6],li[8],li[3],li[1],li[5],li[0],li[7],li[2],))
        
            
