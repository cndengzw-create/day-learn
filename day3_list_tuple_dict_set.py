# 一、list 集合 内标支持负数，代表倒数第几个
fruits = ["苹果", "香蕉", "橙子"]
print(fruits[0])     # 苹果
print(fruits[-1])    # 橙子，-1 是倒数第一个
print(fruits[-2])    # 香蕉

### list 的增删改查
nums = [1, 2, 3]
nums.append(4)        # 末尾加 -> [1, 2, 3, 4]
nums.insert(0, 0)     # 指定位置插 -> [0, 1, 2, 3, 4]
nums.remove(2)        # 按值删除第一个 2 -> [0, 1, 3, 4]
print(nums)
a = nums.pop()            # 删除并返回末尾 -> 4，nums 变 [0, 1, 3]
print(a)
nums[0] = 100         # 修改 -> [100, 1, 3]
len(nums)             # 长度（对应 Java 的 size()）
print(nums)


if "香蕉" in fruits:
    print("有香蕉！")
# =============== 集合第一天 ==========

fruits = ["苹果", "香蕉", "橙子"]
print(fruits)
print(fruits[0], fruits[-1])
print(f"一共有{len(fruits)}种水果")

fruits.append("葡萄")
fruits.insert(1, "西瓜") # 苹果  西瓜 香蕉 橙子 葡萄
print(fruits)

fruits.remove("香蕉")
last = fruits.pop()
print(f"被拿走的最后一个是:{last}") ## 葡萄
print(fruits)

print("葡萄" in  fruits)  #  应该是false吧

for fruit in fruits:
    print(f"我爱吃{fruit}")


## 二、 tuple 元组 [和 list 几乎一样，但创建后不能改。]
point = (3,5)
print(point[0])         # 3   能读
print(point[-1])        # 5   支持负数索引
print(len(point))       # 2

# 不能改，把下面这行取消注释会报 TypeError
# point[0] = 100

solo = (42,)
print(type(solo))       # <class 'tuple'>
# 解包 unpacking（Java 没有的爽点）
x, y = point            # x=3, y=5
print(f"坐标是 ({x}, {y})")
a = 1
b = 2
a, b = b, a             # 交换两个变量，Java 要临时变量，Python 一行

# 三、dict字典 (无序，类似HashMap)
prices = {"贵州茅台": 1500, "宁德时代": 200, "招商银行": 35}

print(prices["贵州茅台"])          # 1500  取值（对应 map.get）
prices["招商银行"] = 36            # 改值
prices["腾讯"] = 300               # 加新键
print(prices)

print("腾讯" in prices)            # True  （对应 containsKey）
print("平安" in prices)            # False

# 安全取值：键不存在返回 None（≈ Java 的 null），不会报错
print(prices.get("平安"))                    # None
print(prices.get("平安", "没有这只股票"))     # 没有这只股票

# 删除
prices.pop("宁德时代")
print(prices)
print("-"*20)
# 遍历：直接 for 出来的是键
for stock in prices:
    print(f"{stock} 现在是 {prices[stock]} 元")
    # 遍历键值对用 .items()
for stock, price in prices.items():
    print(f"{stock}: {price}")

# 四、set集合 无序、不重复的容器，Java 的 HashSet。
# 花括号定义，重复元素自动去重
nums = {1, 2, 2, 3, 3, 3}
print(nums)             # {1, 2, 3}

# 增删
nums.add(4)             # 增加
nums.discard(2)         # 删除，不存在也不报错（对应 remove 的区别）
# nums.remove(2)        # remove 删不存在的会报 KeyError，所以用 discard 更安全
print(nums)
nums.add(3)
print(nums)

# 最常用的场景：list 去重，一行搞定
dups = [1, 1, 2, 3, 3, 4, 4, 4]
unique = set(dups)
print(unique)           # {1, 2, 3, 4}

# 集合运算（Java 里要写 retainAll/addAll 一堆，Python 用符号）
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)            # 交集 {3, 4}      Java: retainAll
print(a | b)            # 并集 {1,2,3,4,5,6}  Java: addAll
print(a - b)            # 差集 {1, 2}      Java: removeAll
print(a ^ b)  # 1 2 5 6
print(b - a)

#四、切片 slice   语法：容器[start:end:step]，核心口诀就一句：顾头不顾尾。
## 切片 = 从容器里按区间取出一个新的子序列（list/tuple/str 通用）。
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[2:5])     # [2, 3, 4]    从索引2取到5，不含5 ← 最容易错的地方
print(nums[:4])      # [0, 1, 2, 3] 开头省略 = 从0开始
print(nums[6:])      # [6, 7, 8, 9] 结尾省略 = 取到末尾
print(nums[::2])     # [0, 2, 4, 6, 8]  步长2，跳着取
print(nums[1:8:2])   # [1, 3, 5, 7]     从1到8，步长2
print(nums[-3:])     # [7, 8, 9]    负数 = 最后三个
print(nums[::-1])    # [9, 8, ..., 0]   反转！今天最重要的一个

## 测验
print("-" *15 + "测验" + "-" *15)
# 第 1 题：预测输出
print([1, 2, 3, 4, 5][1:4])
## [1，2,3,4,5][2,3,4]

# 第 2 题：预测输出
print((1, 2, 3)[-1])
## [1,2,3][3]

# 第 3 题：预测输出
nums = {1, 2, 2, 3}
nums2 = [1, 2, 2, 3]
print(len(nums))
print(len(nums2))
# 4

# 第 4 题：预测两行输出
d = {"a": 1}
print(d.get("b", 0))     # 这一行
#print(d["b"])            # 这一行会发生什么？
# 0
# 报错，没这个值？

# 第 5 题：预测输出
s = "Python"
print(s[::-1])
# nohtyP

## 思考题
x = [1, 2]
y = x
y.append(3)
print(x)
# [1,2,3]