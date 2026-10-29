
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
# for  for in   enumerate

def findMinAndMax(L):

    max_val = min_val = None
    for i, value in enumerate(L):
        if i == 0:
            max_val = min_val = value       # 用第一个元素初始化
        else:
            if value > max_val:
                max_val = value
            if value < min_val:
                min_val = value
    return min_val, max_val
    """一行搞定，可读性最好。

    实测 50 万元素 ×20 次：内置版 0.146s vs 一次遍历版 0.132s，
    差距很小（内置版要遍历两遍）。日常优先选这个，可读性远胜性能微差。
    """
    # return (min(L), max(L)) if L else (None, None)


def findMinAndMax_once(L):
    """一次遍历版：list 和生成器都能用（内置版对生成器会遍历失败/耗尽）"""
    it = iter(L)
    try:
        first = next(it)          # 不能用 L[0]，生成器不支持下标
    except StopIteration:
        return None, None
    max_val = min_val = first
    for value in it:              # 从第二个开始，第一个已用来初始化
        if value > max_val:
            max_val = value
        elif value < min_val:     # elif：不可能同时 >max 又 <min
            min_val = value
    return min_val, max_val
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!',1)
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!',2)
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!',3)
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
