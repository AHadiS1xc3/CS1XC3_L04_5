def powerSet (lst):
    if len (lst) == 0:
        return [[]]
    elif len(lst) == 1:
        return [[],lst]
    else:
        p_set = powerSet(lst[1:len(lst)  ])
        print ("P:", p_set)
        power_set = []
        cur_elm = lst[0]

        for l in p_set:
            lcop = l
            print("L", l)
            elm = []
            for i in range (len(l)+1):
               
                elm  = lcop.insert (i,cur_elm)
                print ("elm", elm)
                power_set.append(elm)
            

        return power_set 

print (powerSet([1,2]))

L = [100,
54,
63,
49,
79,
11,
59,
70,
84,
17,
94,
23,
5,
90,
92,
42,
40,
54,
87,
33,
50,
62,
72,
50]

print (sum(L)/ len (L))