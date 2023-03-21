import random

count = 0

userWin = 0
comWin = 0
noWin = 0

com = random.randrange(0, 3)

while True:
    user = int(input('가위 |0 \n바위 | 1 \n보 | 2 \n\n 선택 : '))

    if user > 2:
        if count == 0:
            print('게임을 하지 않았습니다.')
            break
        print('가위바위보를 %d회 하였습니다.\n' % count)
        print('승 : %d | 패 : %d | 무 : %d' % (userWin, comWin, noWin))

    print('user= %d, com= %d' % (user, com))


    if user == com:
        noWin = noWin + 1
        print('비겼습니다!')
    elif (user == 0 and com == 2) or (user == 1 and com == 0) or (user == 2 and com == 1):
        userWin = userWin + 1
        print('user 승리')
    else:
        comWin = comWin + 1
        print('com 승리')
    count = count + 1
    com = random.randrange(0, 3)
