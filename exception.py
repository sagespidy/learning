def spam(divideby):
	try :
		return 42/divideby
	except ZeroDivisionError:
		print ('Zerodivision error')

print(spam(2))
print(spam (3))
print(spam (0))
print(spam(4))
