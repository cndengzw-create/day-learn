# if/elif/else

# ============ 条件判断 ============
age = 18
if age >= 18:               # 注意冒号 :
    print("成年了")           # 缩进 4 空格 = 属于 if 的代码块
else:
    print("未成年")


name = ""
if name:                     # 空字符串 = 假
    print("有名字")
else:
    print("空的，算 False")

nums = []
if nums:                     # 空列表 = 假
    print("有数据")
else:
    print("空列表，也算 False")


# 循环 for / while
# ============ for 循环 ============
# 遍历列表：直接拿到元素
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(fruit)

# 要数字序列？用 range()
for i in range(5):          # 0 1 2 3 4
    print(i)

for i in range(1, 6):       # 1 2 3 4 5，和切片一样顾头不顾尾
    print(i)

for i in range(0, 10, 2):   # 0 2 4 6 8，第三个是步长
    print(i)
# ============ while 循环 ============
count = 0
while count < 3:
    print(count)
    count += 1              # 不能写 count++！
# ======== break continue ============
for i in range(10):
    if i == 3:
        continue            # 跳过本次，进入下一轮
    if i == 7:
        break               # 直接结束整个循环
    print(i)                # 输出 0 1 2 4 5 6


def calc(a, b):
    return a + b

print(calc(1, 2))

def calc(a, b):
    return a - b
print(calc(1, 2))