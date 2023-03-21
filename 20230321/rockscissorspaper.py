import random

com = random.randrange(0, 2)
user = int(input('가위 |0 \n바위 | 1 \n보 | 2 \n\n 선택 : '))
print('user= %d, com= %d' % (user, com))

if user == com :
    print('비겼습니다!')
elif(user == 0 and com == 2) or (user == 1 and com == 0) or (user == 2 and com == 1) :
    print('user 승리')
else :
    print('com 승리')