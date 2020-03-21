odd = [1, 3, 5, 7, 9]
print(odd)

a = [1, 2, 3]
print(a[0] + a[2])
print(a[-1])

a = [1, 2, 3, ['h', 'a', 'n']]
print(a[-1])
print(a[-1][0])
print(a[3])

a = [1, 2, ['a', 'b',['Life', 'is']]]
print(a[2][2][0])

a = [1, 2, 3, 4, 5]
print(a[0:2])

a = [1, 2, 3, 4, 5]
b = a[:2]
print(b)
c = a[2:]
print(c)

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

a = [1, 2, 3]
print(a * 3)

a = [1, 2, 3]
a[2] = 4
print(a)
print(a[1:2])
a[1:2] = ['a', 'b', 'c']
print(a)

a = [1, 2, 3]
a[1] = ['a', 'b', 'c']
print(a)

