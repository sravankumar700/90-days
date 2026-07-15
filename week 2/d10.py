###### Arrays in Python ####
### its same like list but one difference all elements in list should be similar if one belongs to int then all should be int and float all should be float like that but list store alll types of data in same way 
## it doesnot have fixed value we can strech if needed
####  
from array import *
vals = array('i',[5,8,7,1])
print(vals)
print(vals.buffer_info())
print(vals.typecode)
# print(vals.append(0))
vals.reverse()
print(vals)


for e in  vals :
	print(e)
print(vals.typecode)


##### character Usage #######

char = array('u',['a','e','i'])
for e in char:
	print(e)

newArr = array(vals.typecode,(a*a for a in vals))
for e in newArr :
	print(e)
i  = 0 
while i <len(newArr):
	print(newArr[i])
	i+=1


arr = array('i',[])
n = int(input("Enter The Length of Array :"))
for i in range(5):
	x = int(input("Enter the value "))
	arr.append(x)
print(arr)




user = int(input("Enter The Value To search"))
k =0
for e in array :
	if e == user:
		print(k)
		break

	k+=1
