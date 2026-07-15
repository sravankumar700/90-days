from array import *
# arr = array('i',[10,20,30,40,50,60])
# print(arr)

# char  = array('u',['A','B','C','D','E'])
# for e in char :
#     print(e)

# q3 = array('i',[])
# for i in range (5): 
#     x = int(input('Enter An Element to store :'))
#     q3.append(x)
# print(q3)

# level2 = array('i',[15,25,35,45,55,65])
# i = 0 
# while i <len(level2) :
#     print(level2[i])
#     i = i+1


q5 = array('i',[])
for i in range (6): 
    x = int(input('Enter An Element to store :'))
    q5.append(x)
print(q5)
search = int(input("Enter number to search :"))
for i in range(len(q5)) :
    if q5[i] == search :
        print("Element found")
        print(i)
        break
else:
    print("not Found")
