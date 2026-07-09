# i = 6
# if i>=10:
#     print("Platinum Bonus ")
# elif i in range(5,9):
#     print("Gold Bonus")
# elif i in range(2,4) :
#     print("Silver Bonus")
# else :
#     print("NO Bonus")

# withdraw = 12000
# balance = 15000
# if withdraw<=balance :
#     print("Transaction Successful")
# else :
#     print("Insufficient Balance")

# salary = 9
# if salary>=15 :
#     print("High Tax")
# elif salary>= 8 :
#     print("Medium Tax")
# else :
#     print("Low Tax")

# crct_username = "admin"
# crct_password = "python123"
# username = "admin"
# password = "python123"
# if username ==crct_username and password == crct_password :
#     print("Login Successfull")
# else :
#     print("Invalid Credentials")

# i = 8.4
# if i >=9.0 :
#     print("100% Scholarship")
# elif    i >=8.0 :
#     print("75% Scholarship")
# elif    i >=7.0 :
#     print("50% Scholarship")
# else :
#     print("No Scholarship")


# product_amount = 32000
# if product_amount>=50000 :
#     print("20% Discount")
# elif product_amount>=25000 :
#     print("10% Discount")
# elif product_amount in range(10000,24999):
#     print("5% Discount")
# else :
#     print("No Discount")
    

# st_marks = 68
# if st_marks>=75 :
#     print("Distinction")
# elif st_marks>=60 :
#     print("First Class")
# elif st_marks>=50 :
#     print("Second Class")
# elif st_marks>=35 :
#     print("Pass")
# else :
#     print("Fail")

# age = 21
# cgpa = 7.8
# if age >=18 and cgpa>=7.0 :
#     print("Eligible")
# else:
#     print("Not Eligible")


# experience = 2
# if experience >= 2 :
#     print("Advanced")
# if experience == 1 :
#     print("Intermediate")
# if experience == 0 :
#     print("Beginner")


# pin = 1234
# input_pin = 1234
# if pin == input_pin :
#     print("Phone Unlocked")
# else :
#     print("Incorrect Pin")


# age  = 21
# aadhar = True
# if age >=18 and aadhar == True :
#     print("Eligible to vote")
# else :
#     print("Not eligible to vote ")

# gpa = 8.1
# entrance_score = 82
# if gpa >=8.1 and entrance_score >=82 :
#     print("Admission Granted")
# else: 
#     print("No Admission")

# kids = 12
# senior_citizens  = 60
# customer = 65
# if customer <kids or customer>senior_citizens :
#     print("50% Discount")
# else :
#     print("No Discount")

# grade = 8.4
# vayasu = 21
# language = "python"
# if grade>=7.5 or vayasu>=21 and language == "python" :
#     print("Selected For Interview")
# else :
#     print("Not Selected For Interview")


# technical_score = 92
# communication = 80
# grad_year = 2027,2028
# if technical_score >=80 and communication >=80 and grad_year ==grad_year :
#     print("Hired")
# else:
#     print("Rejected")



# i =1 
# while i <11 :
#     print(i)
#     i=i+1


# i = 1
# while i <6 :
#     print("sravan",end="")
#     j= 1
#     while j<=1 :
#         print("Kumar",end="")
#         j = j+1
#     i=i+1
#     print()

# i =10 
# while i >=1 :
#     print(i)
#     i=i-1

# i =5 
# i% 5
# while i <= 50 :
#     print(i)
#     i=i+5

# # i = 1
# # while i <= 100 :
# #     print(eval(i))
# #     i =i+1


# i=1
# if i<=50 :
#     while r1 == i % 2 :
#         print("Even Count :",round(i))
#         i= i+1
# else r2 = i%1 :
#     print("ODD Number :",round(i))
#     i = i+1




# for i in range(1,21) :
#     print(i)


# for i in range (21,1) :
#     i= i-1
#     print(i)


# for i in range(1,41) :
#     if i % 4== 0:
#         print(i)


# for i in range (1,61) :
#     if i % 6 == 0 :
#         print(i)

# for i in range (1,16):
#     print(i)



for i in range (1,11):
    print(i*9)

for i in range (1,26):
    if i == 13 :
        continue
    print(i)
   
for i in range(1,101):
    if i ==51 :
        break
    print(i)

for i in range (1,51):
    if i %7 ==0 :
        continue
    print(i)

for i in range (1,31):
    if i %5 ==0 or i %3 ==0 :
        continue
    print(i)

# choco = 8
# y = (input("Choco needed :"))
# i = 1
# for i in y  :
#     if i  > choco :
#         print("Out of Stock")
#         break 
#     print(i, " chocolate")
#     i+=1


for i in range (1,101):
    if i % 2 != 0 :
        continue
    print(i)

for i in range(1,101):
    if i == 76 :
        break
    print(i)


for i in range (1,50):
    if i % 11 == 0:
        continue
    print(i)


for i in range(1,31):
    if i % 2 == 0 :
        pass
    else :
        print(i)

for i in range(1,101):
    if i % 9 ==0 :
        print(i)


for i in range(1,21):
    if i ==16 :
        break
    print(i)


for i in range (6):
    for j in range (i+1):
        print("* ",end="")
    i+=1
    print()


for i in range (6):
    for j in range (6-i):
        print("# ",end="")
    print()


for i in range (1,7):
        # print(i)
        for j in range  (i) :
            # if i ==1:
            # #     continue 
            # if i != 1 :
            #     pass
            print(i,end="")
        print()

    