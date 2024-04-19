file = open('example.txt','r',encoding='utf-8')
content = file.read(-1)
print(content)
file.close()