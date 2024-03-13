import os
directory = "temp"
parent_dir = "/home/hetvi/Documents/Hetvi_Python/OS_Modules/a/b/"
path = os.path.join(parent_dir, directory)
 
os.makedirs(path)
print("Directory '% s' created" % directory)
