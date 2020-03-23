"""
대응관계를 나타내는 자료형
연관 배열 또는 해쉬라고 한다
키값을 통해 value값을 얻는다.
"""

a = {1: 'hi'}
print(a)

a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'pay'
print(a)
del a[1]
print(a)

grade = {'pay': 10, 'julliet': 99}
print(grade['pay'])
print(grade['julliet'])

a = {'a':1, 'b':2}
print(a['a'])
print(a['b'])

dic = {'name':'han', 'age':28, 'birthday':19980801}
print(dic.keys())
for k in dic.keys():
  print(k)
  print(list(dic.keys()))
  print(dic.items())
  
dic = {'name': 'han', 'age': 28, 'birthday': 19980801}
print(dic.get('name'))
print(dic.get('bar', 'good'))
print('name' in dic)