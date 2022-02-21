
ml, mr, tl, tr = (('SRP').index(i) for i in input().split())



if ml == mr and (ml + 1) % 3 in (tl, tr):
    print("TK")
elif tl == tr and (tl + 1) % 3 in (ml, mr):
    print("MS")
else:
    print("?")