#  函数
# Python 的样子
def add(a, b):
    return a + b

# ============ 函数基础 ============
# 无参数无返回值
def say_hello():
    print("你好，Python")

# 一个注意点： 函数必须先定义再调用（Python 从上到下执行）。你写 say_hello() 调用时，它的 def 必须在上面已经执行过。
say_hello()                  # 调用：函数名 + ()

# 有参数有返回值
def add(a, b):
    return a + b

print(add(3, 5))             # 8
print(add("Hello", "World")) # HelloWorld  同一个函数能吃不同类型

# 没写 return 的函数，调用结果是 None
def just_print():
    print("我只打印，不返回")

#just_print()
result = just_print()
print(result)                # None（≈ Java 的 null）

## Python 的独门绝技：一次返回多个值（Java 做不到，得造个对象或者返回数组）
def calc(a, b):
    return a + b, a - b, a * b      # 三个值，逗号分隔

x, y, z = calc(10, 5)
print(x, y, z)                      # 15 5 50

# 真相：它其实返回了一个 tuple (15, 5, 50)，
# 然后被解包拆给 x, y, z —— 正好用上你 Day2 学的 tuple 解包
print(calc(10, 5))                  # (15, 5, 50) 看，真是元组

## ===========参数进阶：默认参数 / 关键字参数 / 可变参数=============
# ============ 1. 默认参数（≈ Java 的重载简化版）============
def greet(name, greeting="你好"):
    print(f"{greeting}，{name}")

greet("张三")                 # 你好，张三
greet("李四", "早上好")        # 早上好，李四

def greet2(name):
    print(f"你好，" + name)
greet2("张三")
#greet2("李四", "早上好")        # 早上好，李四

# ============ 2. 关键字参数：调用时点名，不用记顺序 ============
greet(greeting="Hi", name="Tom")    # Hi，Tom

# ============ 3. 可变参数：个数不确定时用 ============
def total(*numbers):          # * 号收集成一堆，存进 tuple
    print(numbers)            # (1, 2, 3)  是个元组
    return sum(numbers)

print(total(1, 2, 3))         # 6
print(total(1, 2, 3, 4, 5))   # 15

def show_info(**info):        # ** 收集"名字=值"，存进 dict
    print(info)               # {'name': '张三', 'age': 30}  是个字典

show_info(name="张三", age=30)
show_info(a=1, b=2, c=3)
## * 和 ** 记忆法： 一个星收一堆位置参数 → tuple；两个星收一堆"名字=值" → dict。这正好用上你刚学的 tuple 和 dict。

# ❌ 错误示范
def add_item_bad(item, target=[]):
    target.append(item)
    return target

print(add_item_bad("a"))     # ['a']
print(add_item_bad("b"))     # ['a', 'b']  ← 震惊！不是 ['b']
print(add_item_bad("b", [2]))     # ['2', 'b']


# =============测验===============
print("# =============测验===============")
# 第 1 题：预测输出
for i in range(1,6):
    print(i)
# 1,2,3,4,5

# 第 2 题：预测输出（break 和 continue）
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
# 1,3

# 第 3 题：预测输出（多返回值）
def calc(a, b):
    return a + b, a * b
x, y = calc(3, 4)
print(x, y)
# 7,12

# 第 4 题：预测两行输出（今天的重点坑）
def add_item(item, taget=[]):
    taget.append(item)
    return taget

print(add_item("a")) # ['a']
print(add_item("b")) # ['a', 'b']

# 第 5 题：这行能跑通吗？不能的话报什么错
count = 0
while count < 3:
    count += 1
# count++  ## ++不行，会报错
print(count)

# 第 6 题：预测输出
prices = []
if prices:
    print("有数据")
else:
    print("空")
## 应该输出空

# 动手题
def stock_range(prices): # 我的代码
    # high = max(prices)
    # low = min(prices)
    # return max, min
    sorted_prices = sorted(prices)
    max = sorted_prices[-1]
    min = sorted_prices[0]
    return max, min

high, low = stock_range([10.5, 12.3, 9.8, 11.0])
print(f"最高 {high}，最低 {low}")   # 期望：最高 12.3，最低 9.8


