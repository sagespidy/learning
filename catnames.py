cat_names= []

while True:
	print ('Enter the name of ' + str(len(cat_names)+1) + ' or enter nothing to stop')
	name = input ()
	if name == '' :
		print ('breaking out of while loop')
		break
	cat_names = cat_names + [name]
print('Names of cats are :')
for name in cat_names:
	print ( '' + name)
