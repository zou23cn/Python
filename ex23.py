import sys
script, encoding, error = sys.argv  #导入参数，argv的前面都学过，稍微有点不一样，但是结果都一样；

#定义主函数  main  ，内有三个形参
def main(language_file, encoding, errors):
    line = language_file.readline() #读取文件中的一行文本，并赋值给line，注意language_file是main主函数的实参

    if line:    #在主函数main内调用了另外一个函数 print_line
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_long = line.strip()
    raw_bytes = next_long.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<==>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")

<<<<<<< HEAD
main(language, encoding, error)


'''
	if语句，用来检测line中是否为真值，如果为真，则执行下面2行代码，如果为假，则跳过不执行；
	所以如果readling()返回包含东西，则继续执行下面2行，如果返回为null，则不执行，这是为了防止死循环；
'''

=======
main(languages, encoding, error)
>>>>>>> c53e66c87913cce5136f1abe2547099893281398
