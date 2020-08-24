from random import choice

def randomStr(length):
    p = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    a = []
    for i in range(length):
        a.append(choice(p))
    return ''.join(a)

#print(random(8))