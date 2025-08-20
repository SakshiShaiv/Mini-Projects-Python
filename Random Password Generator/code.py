import random
import string

str=string.ascii_letters + string.digits + string.punctuation

password=""
length=int(input("enter length of your password"))
for i in range(length):
    print(random.choice(str),end="")