######## For Loop #######


# X = ['sravan',206,2.10]
# for i in X  :
#     print(i)

# for i in range(1,21) :
#     if i% 5 != 0:
#         # print()
#         print(i)








####### break ,continue and pass the key words ########


# Available_candies= 5
# x = int(input(" HOw MAny Candies You Want "))
# i = 1
# while i <= x :
#     if i > Available_candies :
#         print("out of stock ")
#         break 
#     print("candy")
#     i +=1
# print("NO Result")

# for i in range (1,31) :

#     if i%5== 0  or i%3==0:
#         continue

#     print(i)

# print("BYe")



# for i in range(1,31):
#     if i % 2== 0 :
#         pass
#     else :
#        print(i)
# print("BYe")

      



# ####### Printing Pattrerns in Pyton using lopps and controls statements ##########

# for i in  range (4):
#     for j in range(4):
#         print("# ",end="")
#     print(i)






# for i in  range (5):
#     for j in range(i):
#         print("# ",end="")
#     i +=1
#     print()
# for i in  range (4):
#     for j in range(i+1):
#         print("# ",end="")
#     i +=1
#     print()
for i in  range (4):
    for j in range(4-i):
        print("# ",end="")
    
    print()
