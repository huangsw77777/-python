h = int(input('输入你的身高:'))
w = int(input('输入你的体重:'))

if  w**2/h < 18.5 :
	print('轻')
elif 18.5 < w**2/h <25:
	print('正常')
elif 25 < w**2/h < 28:
	print('过重')
elif 28 < w**2/h <32:
	print('肥胖')
else:
	print('严重肥胖')
