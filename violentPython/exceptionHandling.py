# print(1337/0)
# ZeroDivisionError: division by zero

try:
    print(1337/0)
# Store the exception in a variable e then cast the variable e as a string.
except(Exception) as e:
    print ("[-] Error =" + str(e))
