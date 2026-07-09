######### FOR ELSE ###############
# in c,c++,java there will be if else are together not for else here in python we have for else in python for a entire loop if it not works will goes for else block

i =[13,21,51,65,57]

for i in i :
    if i % 2 == 0: # here your if block checks for number divisible by 2
    	print(i)
    else :   # here else block checks for if block if there no elemnts found at if bock then else bloak activates regulary and prints not found 5 times
        print(" Not Found")
else :  # here the else block works for entire for loop and prints only else print stmt
    print("There is No NUmber Divisible By YOur Requirements")