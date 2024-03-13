import sys
print(sys.path)
print("-----------------------")
print(sys.platform)
print("-----------------------")
print(sys.executable)
print("-----------------------")
print(sys.modules)


for i in sys.path:
    print(i)


print(sys.version_info)