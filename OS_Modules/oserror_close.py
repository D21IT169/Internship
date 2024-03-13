import os
# try:
# 	filename = 'hey.txt'
# 	f = open(filename, 'r')
# 	text = f.read()
# 	f.close()

# except IOError:

# 	print('Problem reading: ' + filename)
	



filename = '/home/hetvi/Documents/Hetvi_Python/OS_Modules/hey.txt'
f = open(filename, 'r')
text = f.read()
print(text) 
#os.close(f)

