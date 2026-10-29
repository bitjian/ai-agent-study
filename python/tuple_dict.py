"""tuple 的「不可变」到底指什么 —— 可变性 vs 可哈希性

运行：uv run python python/tuple_dict.py
"""

LINE = "=" * 62

# ---------- 1. 纯不可变元素的 tuple：可以进 dict / set ----------
print(LINE)
print("1. (1, 2, 3) 作为 dict 的 key / set 的元素")
print(LINE)

t1 = (1, 2, 3)
d = {t1: "纯数字元组"}
s = {t1}
print("dict :", d)
print("set  :", s)
print("hash :", hash(t1))

# ---------- 2. 含 list 的 tuple：不可哈希 ----------
print()
print(LINE)
print("2. (1, [2, 3]) 作为 dict 的 key / set 的元素")
print(LINE)

t2 = (1, [2, 3])

def try_it(label, fn):
    try:
        print(f"{label:12s} -> 成功: {fn()}")
    except TypeError as e:
        print(f"{label:12s} -> TypeError: {e}")

try_it("作为dict key", lambda: {t2: "含列表的元组"})
try_it("作为set元素", lambda: {t2})
try_it("调用 hash()", lambda: hash(t2))

# ---------- 3. 原因：tuple 只是「容器不变」，元素本身可以变 ----------
print()
print(LINE)
print("3. 为什么？—— tuple 里的 list 内容是可变的")
print(LINE)

t3 = (1, [2, 3])
print("修改前     :", t3, "  id(t3[1]) =", id(t3[1]))
t3[1].append(4)      # 合法！tuple 本身没变，是里面的 list 变了
t3[1][0] = 99
print("修改后     :", t3, "  id(t3[1]) =", id(t3[1]), "(同一个 list 对象)")
print("t3 的类型  :", type(t3).__name__, "—— tuple 还是 tuple，没被替换")

# ---------- 4. 修复：把 list 换成 tuple ----------
print()
print(LINE)
print("4. 修复 —— 把内部的 list 换成 tuple")
print(LINE)

t4 = (1, (2, 3))
print({t4: "OK"}, {t4})

# ---------- 5. 底层规则 ----------
print()
print(LINE)
print("5. 底层规则")
print(LINE)

print("list.__hash__  =", list.__hash__)
print("dict.__hash__  =", dict.__hash__)
print("set.__hash__   =", set.__hash__)
print("tuple.__hash__ =", tuple.__hash__)
print()
print("1 == 1.0        ->", 1 == 1.0)
print("hash(1), hash(1.0) ->", hash(1), hash(1.0), "(相等的对象必须哈希相等)")
