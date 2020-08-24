from random import choice
def randomStr(length):
    p ='qwertyuiopasdfghjklzxcvbnm1234567890'
    return ''.join(choice(p) for i in range(length))
    