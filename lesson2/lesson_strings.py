
def ptype (str1, str2):
    if type(str1) is not str and type(str2) is not str:
        return(0)
    elif str1.lower() == str2.lower():
        return(1)
    elif len(str1) > len(str2):
        return(2)
    elif str1 != str2 and str2 == "learn":
        return(3)
    else:
        return(4)

print(ptype("1ка6","learn"))