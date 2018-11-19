# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.


# Каждое из слов «class», «function», «method» записать в байтовом типе
str1_b = b'class'
str2_b = b'function'
str3_b = b'method'

# определить тип, содержимое и длину соответствующих переменных
print(type(str1_b)) # <class 'bytes'>
print(str1_b)       # b'class'
print(len(str1_b))  # 5

print(type(str2_b)) # <class 'bytes'>
print(str2_b)       # b'function'
print(len(str2_b))  # 8

print(type(str3_b)) # <class 'bytes'>
print(str3_b)       # b'method'
print(len(str3_b))  # 6
