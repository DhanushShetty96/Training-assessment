import random
# s=list('abcdefghijaklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0*#$%@123456789')
import string

s=list(string.ascii_letters+string.digits+"@#$%*&")
def password_generator():
    length=int(input('Enter length\n'))
    random.shuffle(s)
    password=[]
    for j in range(length):
        random.shuffle(password)
        password.append(random.choice(s))
    random.shuffle(password)
    print("".join(password))
password_generator()