import random
times = 3
secret = random.randint(1,10)
guess = 0
print ('我现在想的那个数字:', end = "")
while (guess != secret) and (times > 0):
        temp = input ()
        guess = int(temp)
        times = times - 1
        if guess == secret:
                print("猜中了")
        else:
                if guess > secret:
                        print('大了')
                else:
                        print('小了')
                if times > 0:
                        print('再试一次',end = "")
                else:
                        print('几会用完了')
print('游戏结束')
