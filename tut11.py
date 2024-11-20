#SETS
#list is used to make sets
s={1,2,3}
s1={3,4,5}
union_set= s.union(s1)
print(union_set)

#set=s.intersection(s1)
#print(set)

st=s.difference(s1)
print(st)

set_dis=s.isdisjoint(s1)
print(set_dis)

sett=s.issubset(s1)
print(sett)

#adding elements in an empty list

s2=set()
s2.add(2)
s2.remove(2)
print(s2)
