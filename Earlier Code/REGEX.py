import re

pattern = "i"

text = '''load() function decodes a JSON file and returns a Python hetvi object. The decoding conversion is based on the following table. 
The . loads() function, alternatively, 
takes a JSON string and returns a Python object.'''


print(re.search(pattern, text))
print(re.findall(pattern, text))
print("-------")
print(re.finditer(pattern, text))




txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


txt = "The rain in Spain"
x = re.split("\s", txt, 2)
print(x)


#SUB FUNCTION (Will replace each i with 9)
txt = "The rain in Spain"
x = re.sub("i", "9", txt)
print(x)

#Replace the first two occurrences of a white-space character with the digit 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)