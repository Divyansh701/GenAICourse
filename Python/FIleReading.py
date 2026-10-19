file = open("dummy.txt", "w")
content = file.write("Hello, World")
print(content)
file.close()

file = open("dummy.txt", "r")
content = file.read()
print(content)
file.close()