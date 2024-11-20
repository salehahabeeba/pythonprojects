#dictionary{} is nothing but key value pairs
from xml.sax.handler import property_interning_dict

d1={"harry":"burger","saleha":"pizza","seeta":"pasta"}
print(d1)
#for finding value of only one key value pair the key should bein square bracket
print(d1["harry"])
#we can also add dictionary in the dictionary
d2={"harry":"burger","saleha":"pizza","seeta":"pasta","rev":{"b":"fish","l":"roti","d":"cake"}}
print(d2)
print(d2["rev"])
print(d2["rev"]["d"])
d2["ankit"]="junk food"
d2[20]="jilebi"
del d2[20]
print(d2)
#dictionary functions
d3=d2.copy()
del d3["harry"]
print(d3)
print(d2)

print(d2.get("saleha"))

d2.update({"leena":"coke"})
print(d2)

print(d2.keys())

print(d2.items())

print(d2.values())
