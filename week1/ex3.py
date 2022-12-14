x = input("enter first number:")
y = input("enter second number:")

#casting as function instead of (int)
print(int(x) + int(y))

#you can also cast right away in definition like x = int(input("enter first number"))

#float - floating point value

#######################################################################################

x= float(input("enter first number:"))
y= float(input("enter second number:"))

print(f"{round(x+y):,}")
#rounds down


#######################################################################################

print(round(x/y,2))

print(f"{(x+y):.2f}") #f string formating numbers

