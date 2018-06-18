temp = input ('我现在想的那个数字:')
guess = int(temp)
if guess == 8:
	print("猜中了")
else:
        if guess > 8:
                print('大了')
        else:
                print('小了')
print('游戏结束')
