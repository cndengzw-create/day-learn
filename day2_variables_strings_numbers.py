# day2_variables_strings_numbers.py
# 学习日期：2026-09-07（周一）第一课 · 变量/字符串/数字 的全部练习
# 对应本地练习文件：learn-first/day1.py

# ===== 变量与类型（动态类型）=====
name = "邓智文"
years_java = 6
height = 1.78
in_learning = True

print(name)
print(type(name))
print(type(years_java))
print(type(height))
print(type(in_learning))

# 标签撕贴：变量可换类型
years_java = "六年"
print(years_java)
print(type(years_java))

# ===== 数字运算 =====
print(7 / 2)  # 3.5   真除法
print(7 // 2)  # 3     向下取整除法
print(7 % 2)  # 1      取余
print(2 ** 10)  # 1024  幂
print(-7 // 2)  # -4    负数向下取整（Java 会得 -3）
print(-7 % 2)  # 1      余数符号跟随除数（Java 会得 -1）

print(-5 % 3)  # 1
print(5 % -3)  # -1

# ===== 字符串基础 =====
poem = """床前明月光
疑是地上霜
举头望明月
低头思故乡"""
print(poem)

greeting = "Hello, Python!"
name = '邓智文'
print(greeting)
print(type(name))  # <class 'str'>，Python 没有 char

s1 = '他说："今天开始学python"'
s2 = "it's my first python day"
print(s1)
print(s2)

print("第一行\n第二行\t按一下tab")
print("反斜杠要写两个:C:\\new")
poem = '''举头望明月
低头思故乡'''
print(poem)

# ===== 字符串拼接与乘法 =====
print("张" + "三")
print("哈" * 3)
print('-' * 20)

# 报错示范（已注释）：print("我的工龄是 " + 6)  # TypeError

# ===== 类型转换 =====
print("我的工龄是 " + str(6))
print(f"我的工龄是 {6}")

age_text = "18"
print(int(age_text) + 2)     # 20
print(float(age_text) + 2)   # 20.0
print(float("3.14") + 1)     # 4.14

print(int(7.99))   # 7
print(int(-7.5))   # -7（int 朝零截断，不是四舍五入）

# ===== 取整方向验证 =====
print(int(-3.5))        # -3   朝零
print(-3.5 // 1)        # -4   朝下
print(int("18") + 2)    # 20
print(float("18") + 2)  # 20.0
print(20 == 20.0)       # True，数值相等
print(type(20), type(20.0))  # <class 'int'> <class 'float'>

# 报错示范（已注释）：print(int("18.5"))  # ValueError：int() 只认整数字符串，带小数点用 float()

# ===== 加餐：input 交互 =====
name = input("你叫什么名字？")
years = input("写 Java 几年了？")

print(f"你好，{name}！听说你写Java {years} 年了")
print("我叫邓智文" + "，很高兴认识你")

like = input("学 Python 感觉如何？(爽/一般/难)：")
if like == "爽":
    print("那太好了，保持这个感觉！")
else:
    print("没关系，前3周最容易劝退，扛过去就顺了")
