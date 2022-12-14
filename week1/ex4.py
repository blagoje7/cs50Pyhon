#functions must be defined before calling it.

# def main():
#     name = input("whats your name? ")
#     hello(name)

# def hello(mrk="world"):#default value in function
#     print("hello,", mrk)

# main()
#in this case every function is defined, functions are defined and we can use anything
#we still must have defined functions BEFORE calling it, here in line 12, main()
#we must have all functions defined before that.

##############################################################################################

#scope
# def main():
#   name = input("whats your name? ")
#   hello()
#
# def hello():
#   print("hello,", name)
#   
# here we are trying to take "name" out of different scope that hello() doesnt recongize

##############################################################################################

#return

def main():
    x = int(input("whats x?"))
    print("x squared is ", square(x))

def square(n):
    return n*n

main()