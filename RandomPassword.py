import random
# s=list('abcdefghijaklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0*#$%@123456789')
import string

s=list(string.ascii_letters+string.digits+"@#$%*&")
def password_generator():
    try:
        length=int(input('Enter length\n'))
        random.shuffle(s)
        password=[]
        for j in range(length):
            password.append(random.choice(s))
        random.shuffle(password)
        print("".join(password))
    except ValueError :
        print("input should be integer")


password_generator()