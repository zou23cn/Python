from sys import argv #加载argv模块函数

script, filename = argv 

txt = open(filename) #打开文件

print(f"Here's your file {filename}: ") #打印文件名
print(script)
print(txt.read())

print("Type the filename again: ")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())