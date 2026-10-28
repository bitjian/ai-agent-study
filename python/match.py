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
