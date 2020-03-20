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

print("i eat %d apples" % 3)
print("i eat %s apples" % "five")

print("Error is %d%%" % 98)

print("%10s" % "hi")

print("%10.4f" % 4.42134234)

a = "hobby"
print(a.count('b'))

b = "python is best choice"

print(b.find('b'), b.find('k'))
a = "Life is too short"
print(a.index('t'))

a=","
print(a.join('abcd'))

a = "hi"
print(a.upper())

a ="    hi my name is Han"
print(a.lstrip())  #오른쪽 공백 제거는 a.rstrip(), 양쪽 공백 제거는 a.strip

a = "Life is too short"
print(a.replace("Life", "your leg"))

a = "Life is too short"
print(a.split())

a = "Life:is:too:short"
print(a.split(':'))

a = "i eat {0} apples".format(3)
b = "i eat {0} apples".format('five')
print(a, b)

number = 3
a = "i eat {0} apples".format(number)
print(a)

number = 3
days = "Three"
a = "i eat {0} apples, {1} days".format(number, days)
print(a)

a = "오늘은 {날씨}입니다. 기온은 {온도}도입니다.".format(날씨='맑음', 온도=21)
print(a)

print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))

print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

print("{{Han}}".format())