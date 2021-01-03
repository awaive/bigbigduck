import random

def sj():
    csj = random.randint(1, 5)
    return csj

a = sj()
Count = 0

for i in range(10):
    try:
        x = int(input('请输入要打开的洞口编号(1-5)：'))
        Count += 1
        if x == a:
            print('玩家胜利，您共猜了：%d次'%(Count))
            break
        else:
            a += random.choice([-1, 1])
        if i == 9:
            print('玩家失败，您的次数用光了')
    except ValueError:
        print("请输入数字")