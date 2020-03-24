pin = "881120-1068234"
print(pin[0:6])
print(pin[7:14])
print(pin[7])

a = [1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

a = ['Life', 'is', 'too', 'short']
print(" ".join(a))

a = (1,2,3)
print(a + (4,))

a = {'A':90, 'b':80, 'c':70}
result = a.pop('b')
print(a)
print(result)

a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

a = b = [1,2,3]
a[1] = 4
print(b)