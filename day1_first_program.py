# day1_first_program.py
# 2026-09-06 第一天：Python 的第一个程序（对照 Java）
# 关键点：f-string + 列表推导式

# f-string：字符串里用 {} 直接插变量（Java 里要写一堆拼接）
name = "邓智文"
years = 6
print(f"我叫{name}，写Java已{years}年")

# 列表推导式：等价于 Java 的 for + if + list.add() 三件套
nums = [x * 2 for x in range(10) if x % 2 == 0]
print(nums)   # [0, 4, 8, 12, 16]

# range(10) 生成 0~9；if x % 2 == 0 只留偶数；x * 2 翻倍
