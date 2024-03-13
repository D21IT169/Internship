import os
directory = "makkee"
parent_dir = "/home/hetvi/Documents/Hetvi_Python/OS_Modules/"
path = os.path.join(parent_dir, directory)
 
os.mkdir(path)
print("Directory '% s' created" % directory)
