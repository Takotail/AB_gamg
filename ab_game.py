#輸入數字

print('輸入你的四個數字:')

print('第一個整數:')
num_1 = ( input('') )
while str.isdigit(num_1) != True :
 	print('請輸入整數！：')
 	num_1 = ( input('') )

print('第二個整數：')
num_2 = ( input('') )
while str.isdigit(num_2) != True :
 	print('請輸入整數！：')
 	num_2 = ( input('') )

print('第三個整數：')
num_3 = ( input('') )
while str.isdigit(num_3) != True :
 	print('請輸入整數！：')
 	num_3 = ( input('') )

print('第三個整數：')
num_4 = ( input('') )
while str.isdigit(num_4) != True :
 	print('請輸入整數！：')
 	num_4 = ( input('') )

print('你出的題目是：')
print(num_1, num_2, num_3, num_4)

import random

while(7):
	print( random.randrange(10) )