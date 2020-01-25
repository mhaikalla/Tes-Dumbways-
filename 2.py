lis = ['a','b','c','d']


def minmax(l):
    min = 'a'
    max = 'a'
    for i in range(0, len(l)):
        if l[i] < min:
            min = l[i]
             
    while (l.index(l[0]) < l.index(min)) and (l[0] > min):
        del l[0]
    else:
        for i in range(0, len(l)):
            if l[i] > max:
                max = l[i]   
    print("['" + min + "','"+ max +"']")   
     
minmax(lis)
