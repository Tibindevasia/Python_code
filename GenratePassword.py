import random

def gen_pass():
    """Python function to create a password, 
    declare a string of numbers + uppercase + lowercase + special characters
    and used random sample for picking the characters"""
    
    leng_pass = int(input("Enter the length of password: "))
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    pass_list = random.sample(s, leng_pass)
    print("".join(pass_list))

gen_pass()





