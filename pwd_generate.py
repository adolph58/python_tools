import random

repo = ['2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']

def get_pwd():
    pwd = ''
    for i in range(1, 17):
        num = random.randint(0, 54)
        pwd += repo[num]
    return pwd;

for j in range(1, 50):
    print(get_pwd())