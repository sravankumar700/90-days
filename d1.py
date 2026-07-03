# variables 
a = int(5)
b= int(20)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)

X = 2
X += 3
Y = 3
Y += X
Z = 10
print(X,Y)
print(X + Z ,Y +  Z)

name = "sravan"
print(name)
name + "kumar"
print(name[5])
print(name[-4])
print(name[0:3])
# print(name[4:])    / /// there is no ending so it prints till last 
# print(name[:2])   //there is no begining so it starts printing from start
print(name[0:3] + "Kumar")

myname ="sravan kumar"
print(len(myname))


### more on variables  ###

num = 5
print(id(num))
name ="sravan"
print(id(name))
a = 10 
b = a

#### here all the variables refere to the same box which stores the data in same adddress checkfor output 
print(id(a))
print(id(b))
print(id(10))
### if we update the a value here it will updates and points other address and the remaining will remain same if we change them then it will become to new box different addresses
a=9
b=8
k=a
print(id(a))
print(id(k))
print(id(9))
print(id(b))
print(id(8))
  

#### constants in pyhton 
### we can declare constants in variable a variable constant can be declared by differenet format of representation (capital letters)
PI = 3.14
print(PI)
print(type(PI))


##### data types ######
#### none = a null a value where a variable doesnot have assigned any value####
#### numeric  4 types int , float , omplex , boolean ###

num = 2.5
print(type(num))
num = 5
print(type(num))
num = 6*8j
print(type(num))

a = 548.798485
b=int(a)
print(b)
print(type(b))
k=float(b)
print(k)
k=4
c= complex(b,k)
print(c)
print(b<k)
print(b>=k)
print(type(b>k))
print(int(True))
print(int(False))




#### list ####
#### tuple ####
#### set ####
#### string ####
#### range ####
######## these are known as sequence ##### 

lst = [1,5,48,84,541,5154]
print(type(lst))
set = {1,5,48,84,541,5154}
print(type(set))
tuple = (1,5,48,84,541,5154)
print(type(tuple))

str = "sravan kumar"
print(type(str))

range(19)
print(range(19))
print(list(range(19)))
print(list(range(0,19,2)))
print(list(range(1,19,2)))

 
#### dictionary 
# IN dictonary we store the data as key value pairs in a set eg : "sai":"samusung" ###
# from the above eg sai is the key and samusubg is the value 
# here in dictionary evry key should need to be unique otherwise it will overwrite the  value of original key ####

d = {"sravan":"redmi","kittu": "iqoo","bharadwajan":"oppo","sai":"samusung", "sai": "vivo"}
print(d)
print(d.keys())
print(d.values())
print(d.get("sravan"))
print(d["kittu"])


