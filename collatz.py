def collatz(number):
	if (number % 2) == 0 :
		print ('Even number entered')
		result = number // 2
		print (result)
		return result
	elif(number % 2) == 1:
		print ('odd number entered')
		result =  3 * number + 1
		print(result)
		return result

collatz(4)
collatz(5)
