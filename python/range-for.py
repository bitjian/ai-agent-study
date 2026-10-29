
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
# 列表生成式



L1 = ['Hello', 'World', 18, 'Apple', 0]
L2 =  [x.lower()  for x in L1 if isinstance(x, str)  ]
L3 = [x.lower() if isinstance(x, str)  else -x  for x in L1  ]

# 测试:
print(L2, L3)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
