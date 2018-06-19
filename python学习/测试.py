psw = input('请输入密码:')
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
print('没机会啦')
