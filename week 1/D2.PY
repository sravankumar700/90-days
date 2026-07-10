# lists in python once declard we can also update in  the middle mutable changable

nums = [15,19,62,54,87,5,47]
print(nums)
print(type(nums))
print(nums[0])
print(nums[6])
print(nums[3:6])

names =["sravan","kumar","meesala"]
print(names)

list = [4.0,"sravan",30]
print(list)

newlist = [names,list]
print(newlist)
names.append(90)
print(names)
names.insert(0,654)
print(names)
names.remove(90)
print(names)
print(newlist)
names.pop()
print(names)
del names[:3]
print(names)
names.extend([26,84,74,95,65,])
print(names)
max(names)
print(names)
nums = [15,65,45,52,14,36]
print(nums)
print(min(nums))
print(type(nums))
print(max(nums))
