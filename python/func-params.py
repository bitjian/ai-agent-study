"""可接收一个或多个数并计算乘积

运行：uv run python python/func-params.py
"""

# ---------- 为什么 mul(5, 6, 7=7) 不行 ----------
# 关键字参数的名字必须是「合法变量名」，数字不是标识符，
# 这不是运行时报错，而是连语法都过不了（SyntaxError）。
try:
    exec("mul(5, 6, 7=7)")
except SyntaxError as e:
    print("mul(5, 6, 7=7) -> SyntaxError:", e.msg)


# ---------- 方案 A：*args 位置可变参数（推荐） ----------
def mul(x, y=1, *args):
    """x 必填，y 默认 1，其余任意多个数都收进 args 元组"""
    res = x * y
    for num in args:
        res *= num
    return res


# ---------- 方案 B：**kwargs 关键字可变参数 ----------
def mul_kw(x, y=1, **kwargs):
    """额外的数必须用「名字=值」的形式传，收进 kwargs 字典"""
    res = x * y
    for num in kwargs.values():     # 注意：遍历字典要 .values()，直接遍历拿到的是键
        res *= num
    return res


print("\n--- 方案 A: *args ---")
print("mul(5)          =", mul(5))
print("mul(5, 6)       =", mul(5, 6))
print("mul(5, 6, 7)    =", mul(5, 6, 7))
print("mul(5, 6, 7, 9) =", mul(5, 6, 7, 9))

print("\n--- 方案 B: **kwargs ---")
print("mul_kw(5, 6)           =", mul_kw(5, 6))
print("mul_kw(5, 6, a=7)      =", mul_kw(5, 6, a=7))
print("mul_kw(5, 6, a=7, b=9) =", mul_kw(5, 6, a=7, b=9))

# ---------- 测试 ----------
print()
if mul(5) != 5:
    print("mul(5)测试失败!")
elif mul(5, 6) != 30:
    print("mul(5, 6)测试失败!")
elif mul(5, 6, 7) != 210:
    print("mul(5, 6, 7)测试失败!")
elif mul(5, 6, 7, 9) != 1890:
    print("mul(5, 6, 7, 9)测试失败!")
else:
    try:
        mul()
        print("mul()测试失败!")
    except TypeError:
        print("测试成功!")
