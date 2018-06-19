temp = input('输入一个数字，判断奇偶数:')
while not temp.isdigit():
    temp = input('请输入一个整数:')
number = int(temp)
if(number % 2 == 1):
    print('这是奇数')
else:
    print('这是偶数')
