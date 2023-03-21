import random
from tkinter import *

count = 0

first = 0
second = 0
third = 0
fourth = 0
fifth = 0
sixth = 0

firstLucky = random.randrange(1, 45)
secondLucky = random.randrange(1, 45)
thirdLucky = random.randrange(1, 45)
fourthLucky = random.randrange(1, 45)
fifthLucky = random.randrange(1, 45)
sixthLucky = random.randrange(1, 45)

bonusLucky = random.randrange(1, 45)

myLucky = [random.randrange(1, 45), random.randrange(1, 45), random.randrange(1, 45), random.randrange(1, 45),
           random.randrange(1, 45), random.randrange(1, 45)]

stat = 0
def genMyLuck():
    myLucky = [random.randrange(1, 45), random.randrange(1, 45), random.randrange(1, 45), random.randrange(1, 45),
               random.randrange(1, 45), random.randrange(1, 45)]
    myLuckyLabel.config(text=str(myLucky))




import signal
import sys

def sigint_handler(signal, frame):
    print ('KeyboardInterrupt is caught')
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

def stopGen():
    stat = 1

root = Tk()

root.title('lotto gen')
root.geometry('600x400+100+100')
root.resizable(False, False)

myLuckyLabel = Label(root, text='[]')
myLuckyLabel.pack()

genLuckButton = Button(root, width=10, text="번호 생성", overrelief="solid", command=genMyLuck)
genLuckButton.pack()

firstLabel = Label(root, text='1등 : ' + str(first) + '회', width=10)
secondLabel = Label(root, text='2등 : ' + str(second) + '회', width=10)
thirdLabel = Label(root, text='3등 : ' + str(third) + '회', width=10)
fourthLabel = Label(root, text='4등 : ' + str(fourth) + '회', width=10)
fifthLabel = Label(root, text='5등 : ' + str(fifth) + '회', width=10)
sixthLabel = Label(root, text='낙첨 : ' + str(sixth) + '회', width=10)
def runGen():
    global first
    global second
    global third
    global fifth
    global fourth
    global sixth
    global stat

    global fifthLucky
    global secondLucky
    global thirdLucky
    global fifthLucky
    global fourthLucky
    global sixthLucky
    global bonusLucky

    stat = 0
    try:
        while stat == 0:
            rank = 7
            firstNum = firstLucky in myLucky
            secondNum = secondLucky in myLucky
            thirdNum = thirdLucky in myLucky
            fourthNum = fourthLucky in myLucky
            fifthNum = fifthLucky in myLucky
            sixthNum = sixthLucky in myLucky

            if firstNum == True:
                rank = rank - 1
            if secondNum == True:
                rank = rank - 1
            if thirdNum == True:
                rank = rank - 1
            if fourthNum == True:
                rank = rank - 1
            if fifthNum == True:
                rank = rank - 1
            if sixthNum == True:
                rank = rank - 1

            if rank == 1:
                first = first + 1
                firstLabel.config(text='1등 : ' + str(first) + '회')
                firstLabel.pack()
            elif rank == 2:
                if bonusLucky in myLucky == True:
                    second = second + 1
                    secondLabel.config(text='2등 : ' + str(second) + '회')
                    secondLabel.pack()
                else:
                    third = third + 1
                    thirdLabel.config(text='3등 : ' + str(third) + '회')
                    thirdLabel.pack()
            elif rank == 3:
                fourth = fourth + 1
                fourthLabel.config(text='4등 : ' + str(fourth) + '회')
                fourthLabel.pack()
            elif rank == 4:
                fifth = fifth + 1
                fifthLabel.config(text=('5등 : ' + str(fifth) + '회'))
                fifthLabel.pack()
            else :
                sixth = sixth + 1
                sixthLabel.config(text="낙첨 : " + str(sixth) + "회")
                sixthLabel.pack()
    except KeyboardInterrupt:
        print(' ')

firstLabel.pack()
secondLabel.pack()
thirdLabel.pack()
fourthLabel.pack()
fifthLabel.pack()
sixthLabel.pack()

runButton = Button(root, width=10, text="시작", overrelief="solid", command=runGen)
runButton.pack()

stopButton = Button(root, width=10, text="중지", overrelief="solid", command=stopGen)

genLuckButton.pack()
root.mainloop()
