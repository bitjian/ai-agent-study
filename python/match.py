age = 1
match age:
    case x if x < 10:
        print("年龄小于10岁")
    case 11:
        print("年龄11")
    case 12|13|14:
        print("年龄12-14")
    case _:
        print("未匹配")


args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
