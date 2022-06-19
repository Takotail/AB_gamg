#git push test

import random

start = input('輸入起始值')
start = int(start)
end = input('輸入結束值')
end = int(end)

r = random.randint(start, end)
count = 0

while True:
	num = input('猜猜數字')
	num = int(num)
	count += 1
	if num == r:
		print('猜中囉！')
		print('這是你猜的第', count, '次')
		break
	elif num < r:
		print('太小')
	elif num > r:
		print('太大')
	print('這是你猜的第', count, '次')





