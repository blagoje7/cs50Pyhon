#string methods

name = input("whats your name?").strip().title()

#name = name.strip().title()
#method
#strips whitespaces from right and left from input (here name)

#name = name.capitalize()
#capitalizes first letter of the string

#name = name.title()
#capitalizes every first letter after space

#lstrip, rstrip

print(f"hello, {name}")

###################################################################################################


#wont work if there is less then 2 arguments in name
#you can make that restriction here
first, last = name.split()
print(first,last)