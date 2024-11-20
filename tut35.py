#USE OF SPLIT FUNCTION
def from_str(string):
    params=string.split("-")
    return (params[0],params[1],params[2])
print(from_str("karan-330-student"))