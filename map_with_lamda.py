#map(finction,(tuple,list,set,directory))

def muli(num):
    return num*num
result=map(lambda i:i+1,(2,4,6,8))
print(tuple(result))



def toUpper(str):
    return str.upper()
result1=map(toUpper,("saad","ansari"))
print(tuple(result1))


dict_item={"A":"Car","B":"Bike","C":"Train"}
a=map(lambda b:(b[0]+"-",b[1]),dict_item.items())
print(dict(a))



