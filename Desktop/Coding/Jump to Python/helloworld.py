#hello.py
print("Hello World")

"""
Author: Hanseungpil
Date: 2020-03-20
Hello World를 출력하는 프로그램 입니다.
"""

a = 7 // 4
print(a)

food = "python's favorite food is perl"
print(food)

# 'python's favorite food is perl' // '를 표시하고 싶을 때는 ''를 사용한다(문자열을 표시하는 문구인지 아닌지를 판단하기 위해서.)

say = '"python is very easy'
print(say)

multiline = "Life is to short\nyou need python"
print(multiline)

multiline='''
Life is to short
you need python'''
print(multiline)

multiline = """
Life is to short
you need python\n"""
print(multiline)

print("=" * 50)
print("my program")
print("=" * 50)

a = "Life is too short, you need Python"
print(a[3])
print(a[-1])
print(a[0:4])
print(a[19:])
print(a[:17])

a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)  #슬라이싱으로 문자열 나누기

p = "pithon"
a = p[:1]
b = p[2:]
print(a + "y" + b)