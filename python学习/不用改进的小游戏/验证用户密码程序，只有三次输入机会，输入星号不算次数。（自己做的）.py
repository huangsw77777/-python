"""psw = input('请输入密码:')
answer = '二狗大帅逼'
i = 3
while i > 0:
    
    if psw == answer:
        print('密码正确。')
        break  
    else:
        i -=1
        psw = input('从新输入')
        continue
print('没机会啦')  上面是自己做的
"""
count = 3
password = 'FishC.com'

while count:
    passwd = input('请输入密码：')
    if passwd == password:
        print('密码正确，进入程序......')
        break
    elif '*' in passwd:
        print('密码中不能含有"*"号！您还有', count, '次机会！', end=' ')
        continue
    else:
        print('密码输入错误！您还有', count-1, '次机会！', end=' ')    
    count -= 1
